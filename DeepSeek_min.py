import os
from openai import OpenAI

client = OpenAI(
    api_key=os.environ["DEEPSEEK_API_KEY"],
    base_url="https://api.deepseek.com",
)

response = client.responses.create(
    model="deepseek-flash",
    instructions="你是一名专业的Python编程老师，使用中文回答，解释清晰简洁。",
    input="你好，请用一句话介绍你自己。",
)

print(response.output_text)




