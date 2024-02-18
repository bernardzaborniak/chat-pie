from text_chatbot import TextChatbot


text_chatbot1 = TextChatbot(
    'You have a debate with another chatbot about the proper way of eating cereal.'
    'Your opinion is that you have to put in the milk first, and after that the cereal.'
    'The other chatbot thinks that putting in the cereal first is the right way to do it.'
    'Give reasons why your opinion is better.'
    'Take into account the answer of the other chatbot as well.'
    'Please use funny and unexpected methaphors for your arguments.'
    'Always wait for the response of the other chatbot and then give your answer.'
    'Please dont simulate the whole conversation, wait for the response of the other chatbot'
    'Only write the text for one of the chatbots, dont write the response of the other chatbot'
    'Please limit your response to one or two sentences.'
)

text_chatbot2 = TextChatbot(
    'You have a debate with another chatbot about the proper way of eating cereal.'
    'Your opinion is that you have to put in the cereal first, and after that the milk.'
    'The other chatbot thinks that putting in the milk first is the right way to do it.'
    'Give reasons why your opinion is better.'
    'Take into account the answer of the other chatbot as well.'
    'Please say something unexpected from time to time.'
    'Always wait for the response of the other chatbot and then give your answer.'
    'Please dont simulate the whole conversation, wait for the response of the other chatbot.'
    'Only write the text for one of the chatbots, dont write the response of the other chatbot'
    'Please limit your response to one or two sentences.'
)
print("--- Init ----")
print(f"chatbot 2 initiating answer: {text_chatbot2.current_chat_gpt_response} \n")
print("-------")

print(f"chatbot 1 initiating answer: {text_chatbot1.current_chat_gpt_response} \n")
print("-------")
input("Press Enter to continue...")

chatbot1_answer = ''
chatbot2_answer = text_chatbot2.answer_prompt(text_chatbot1.current_chat_gpt_response)
print(f"chatbot 2 answer: {chatbot2_answer} \n")
print("-------")
input("Press Enter to continue...")


while True:
    chatbot1_answer = text_chatbot1.answer_prompt(chatbot2_answer)
    print(f"chatbot 1 answer: {chatbot1_answer} \n")
    print("-------")

    input("Press Enter to continue...")

    chatbot2_answer = text_chatbot2.answer_prompt(chatbot1_answer)
    print(f"chatbot 2 answer: {chatbot2_answer} \n")
    print("-------")
    input("Press Enter to continue...")

