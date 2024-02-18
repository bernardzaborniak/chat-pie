from datetime import datetime
import os
import threading
import time
from openai import OpenAI

client = OpenAI(api_key=os.environ["OPENAI_API_KEY"])

class TextChatbot:
   
    def __init__(self, chat_character_prompt):
        # Decides whether this chatbot starts a conversation first
        # This prompt is used to shape the character of the chatbot
        self.chat_character_prompt = chat_character_prompt
        self.chat_history = []
        self.waiting_for_chat_gpt = False
        self.current_chat_gpt_response = ""
        self.chat_history = []
        self.response_number = 0

        self.OUTPUT_FOLDER = os.path.join(os.getcwd(), "outputs")
        if os.path.exists(self.OUTPUT_FOLDER):
            import shutil
            shutil.rmtree(self.OUTPUT_FOLDER)
        os.makedirs(self.OUTPUT_FOLDER)

        self.waiting_for_chat_gpt = True
        threading.Thread(target=self.get_chat_gpt_response_threaded(self.chat_character_prompt)).start()
        while self.waiting_for_chat_gpt:
            time.sleep(1)

        #self.write_text(self.current_chat_gpt_response)

        

    def write_text(self, text):
        with open(os.path.join(self.OUTPUT_FOLDER, f'output{self.response_number}.txt'), 'w') as f:
            f.write(text)
        self.response_number = self.response_number + 1


    def get_chat_gpt_response_threaded(self, input_text):
        self.chat_history.append({"role": "user", "content": input_text})
        response = client.chat.completions.create(
            model="gpt-3.5-turbo", messages=self.chat_history
            #model="gpt-4", messages=self.chat_history
        )
        self.current_chat_gpt_response = response.choices[0].message.content
        self.chat_history.append({"role": "assistant", "content": self.current_chat_gpt_response})
        self.waiting_for_chat_gpt = False


    def answer_prompt(self, prompt_to_answer):  

        self.waiting_for_chat_gpt = True
        threading.Thread(target=self.get_chat_gpt_response_threaded(prompt_to_answer)).start()

        while self.waiting_for_chat_gpt:
            time.sleep(1)

        #self.write_text(self.current_chat_gpt_response)

        return self.current_chat_gpt_response
