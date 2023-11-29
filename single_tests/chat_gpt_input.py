import openai
openai.api_key='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'

while True:
    text = input('ask chatgpt ')
    response = openai.ChatCompletion.create(model="gpt-3.5-turbo", messages=[{"role": "user", "content": f"{text}"}])
    response_text = response.choices[0].message.content

    print(response_text)

