import openai
openai.api_key='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'

text = "can you please tell me in which year the moon landing took place?"
response = openai.ChatCompletion.create(model="gpt-3.5-turbo", messages=[{"role": "user", "content": f"{text}"}])
response_text = response.choices[0].message.content

print(response_text)

