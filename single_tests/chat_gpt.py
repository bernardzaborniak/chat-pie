import openai
import os
openai.api_key = os.environ["OPENAI_API_KEY"]


text = "can you please tell me in which year the moon landing took place?"
response = openai.ChatCompletion.create(model="gpt-3.5-turbo", messages=[{"role": "user", "content": f"{text}"}])
response_text = response.choices[0].message.content

print(response_text)

