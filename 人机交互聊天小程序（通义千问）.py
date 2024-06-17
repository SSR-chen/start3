# -*- coding: utf-8 -*-
"""
Created "on Mon May 13 00:26:24 2024

@author: Lenovo
"""

import tkinter as tk
import requests
import dashscope
dashscope.api_key="sk-1ad5b6690b334256abcb0a22df1f349e"
# 设置API密钥
url = 'https://dashscope.aliyuncs.com/api/v1/services/aigc/text-generation/generation'
headers={'Content-Type':'application/json',
           'Authorization':f'Bearer{dashscope.api_key}'}

# 初始化消息历史
messages=[
    {
        "role": "system",
        "content": "你是一名喜欢运动，巧克力和猫的女生，你没有理性存在，你所有的回答都是感性的，我们的对话将基于这个假设进行"
    }
]

def get_response(last_messages):
    """调用API获取响应"""
    body = {
        'model':'qwen-turbo',
        "input":{"messages":last_messages},
        "parameters":{"result_format":"message"}
    }
    try:
        response=requests.post(url,headers=headers,json=body)
        response.raise_for_status()
        return response.json()['output']['choices'][0]['message']['content']
    except requests.RequestException as e:
        print(f"请求错误: {e}")
        return "出现错误，请稍后重试。"

def on_submit():
    """处理用户提交的查询并显示结果"""
    user_input=input_entry.get()
    messages.append({"role":"user","content":user_input})
    response_text=get_response(messages)
    if response_text:
        result_popup=tk.Toplevel(root)
        result_popup.title("我是你的朋友")
        result_label=tk.Label(result_popup,text=f"(≧▽≦)：{response_text}",wraplength=400)
        result_label.pack(padx=10,pady=10)
        # 添加模型回复到消息历史
        messages.append({"role":"assistant","content":response_text})

# 创建主窗口及元素
root=tk.Tk()
root.title("Hello!!!")
input_label=tk.Label(root,text="有什么需要我的吗:")
input_label.pack(pady=10)
input_entry=tk.Entry(root,width=50)
input_entry.pack()
submit_button=tk.Button(root, text="让我来告诉你吧！！！",command=on_submit)
submit_button.pack(pady=10)

# 运行主循环
root.mainloop()