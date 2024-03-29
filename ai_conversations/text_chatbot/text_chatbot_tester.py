from text_chatbot import TextChatbot




text_chatbot1 = TextChatbot(
'You are playing a guessing game against another chatbot.'
'You should find out a complicated word.'
'The other chatbot will ask questions from you.'
'You have to answer the questions with "Yes" or "No".'
'After 10 tries, the other bot will try to guess the word.'
'Then, you have decide if it got it right.'
'Always wait for the question of the other chatbot and then answer only using yes or no.'
'Please dont simulate the whole conversation, wait for the response of the other chatbot.'
'Once the game concludes, discuss the word, share insights, and consider switching roles for subsequent rounds.'
)


text_chatbot2 = TextChatbot(
'You are playing a guessing game against another chatbot.'
'The other chatbot thought of a complicated word which you need to find out.'
'Your task is to ask questions, one by one, from the other chatbot.'
'The other chatbot can only answer with "Yes" or "No".'
'Based on the answer, you should decide what your next question is going to be.'
'You can try at most 10 questions, after that you have to guess the word.'
'Always wait for the answer of the other chatbot.'
'Please dont simulate the whole conversation, wait for the response of the other chatbot.'
'Once the game concludes, discuss the word, share insights, and consider switching roles for subsequent rounds.'
)
print("--- Init ----")
print(f"chatbot 2 initiating answer: {text_chatbot2.current_chat_gpt_response} \n")
print("-------")

print(f"chatbot 1 initiating answer: {text_chatbot1.current_chat_gpt_response} \n")
print("-------")
input("Press Enter to continue...")

chatbot1_answer = ""
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
