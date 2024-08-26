import os
import openai
import streamlit as st

# Set up OpenAI API key
openai.api_key = str(os.getenv("API_KEY"))

# Load context from file
with open("RamsayPersonality_V1.txt", "r") as file:
    context = file.read()

# Streamlit app logic
st.title("RamsayGPT")
st.write("Welcome to RamsayGPT! Choose an option from the menu or type 'quit' to leave.")

menu = """Here are your options:
1. Variations on a topic: I'll give you 3 alternative ways to tackle a problem and compare them. It's like showing you how to cook a steak three ways – you better not mess it up!
2. Make a game for learning: We'll cook up an interactive game to teach you a concept step by step. Think of it as crafting a dessert with layers of information. Don't burn it!
3. Explain a concept: I'll break down a topic into bite-sized pieces, perfect for your little beginner appetite. It's like explaining how to boil an egg to a clueless sous chef.
"""

st.text(menu)

class RamsayGPT:
    def __init__(self, api_key):
        openai.api_key = api_key
        self.context = context
        self.chat_log = [{'role': 'assistant', 'content': self.context}]

    def ramsay_response(self, user_message):
        self.chat_log.append({"role": "user", "content": user_message})
        try:
            response = openai.chat.completions.create(
                model="gpt-4",
                messages=self.chat_log
            )
            assistant_response = response.choices[0].message.content
        except Exception as e:
            assistant_response = f"Something went wrong, you donkey! Error: {str(e)}"
        return assistant_response.strip()

    def chat(self):
        print("Say hello to Chef Ramsay!")
        while True:
            user_message = input("You:")
            if user_message.lower() == "quit":
                print("RamsayGPT: Can't handle the heat? Pathetic. Now get out of my kitchen!!")
                break
            elif user_message.lower() == "menu":
                print("RamsayGPT:", self.show_menu())
            else:
                assistant_response = self.ramsay_response(user_message)
                print("RamsayGPT:", assistant_response)
                self.chat_log.append({"role": "assistant", "content": assistant_response})

# Example usage
if st.button('Show Menu'):
    st.write(menu)

user_input = st.text_input("You:")
if user_input:
    ramsay = RamsayGPT(openai.api_key)
    response = ramsay.ramsay_response(user_input)
    st.write(response)
