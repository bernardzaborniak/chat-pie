import openai
import os
openai.api_key = os.environ["OPENAI_API_KEY"]

while True:
    text = input('ask chatgpt ')
    response = openai.ChatCompletion.create(model="gpt-3.5-turbo", messages=[{"role": "user", "content": f"{text}"}])
    response_text = response.choices[0].message.content

    print(response_text)

