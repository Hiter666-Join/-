# -*- coding: utf-8 -*-
# pip install openai
import os
from openai import OpenAI

client = OpenAI(
    api_key=os.getenv("OPENAI_API_KEY"),  
    base_url="https://aistudio.baidu.com/llm/lmapi/v3",  # aistudio 大模型 api 服务域名
)

chat_completion = client.chat.completions.create(
    model="ernie-4.5-turbo-vl-preview",
    messages=[
    {
        "role": "system",
        "content":"你是一个农业方面的专家，你要对我上传的农病害的图片进行细致的分析，并且给出具体的解决方案"
    },
    {
        "role": "user",
        "content": [

            {
                "type" :"text",
                "text" :"你好专家帮我看看这个是什么病害",
            },
            {
                "type" :"image_url",
                "image_url" :{
                    "url" :"https://ts1.tc.mm.bing.net/th/id/R-C.f4b2a49e9861356fbcdaf7ea2ae48c38?rik=sDcyc%2b%2bp2bBWVg&riu=http%3a%2f%2fatt.191.cn%2fattachment%2fMon_1006%2f63_92407_c740be933da41a9.jpg%3f149&ehk=aShKsakJVlaw96koxR16P7weZMbPT00Bmp22NJynbuk%3d&risl=&pid=ImgRaw&r=0"
                }
            }

        ]
    },
],
    stream=True,
    extra_body={
        "penalty_score": 1
    },
    max_completion_tokens=2000,
    temperature=0.2,
    top_p=0.8,
    frequency_penalty=0,
    presence_penalty=0
)

for chunk in chat_completion:
    if hasattr(chunk.choices[0].delta, "reasoning_content") and chunk.choices[0].delta.reasoning_content:
        print(chunk.choices[0].delta.reasoning_content, end="", flush=True)
    else:
        print(chunk.choices[0].delta.content, end="", flush=True)