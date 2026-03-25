import streamlit as st

def greeting_chatbot(msg):
    
    if any(word in msg for word in simple_message):
        return "Hi! How can i help you."
        
    elif any(word in msg for word in time_message):
        return f"{msg}! Hope you are doing well."
        
    elif any(word in msg for word in conversation_message):
        return "I'm doing well, thanks for asking!"
        
    elif any(word in msg for word in thanks_message):
        return "You're welcome!"
        
    elif any(word in msg for word in bye_message):
        return "Goodbye! See you next time."

    elif any(word in msg for word in salam):
        return "Wassalam"
        
    else:
        return "Sorry! i am just a greeting chatbot"
        

simple_message = ["hi","hello","hy","hey","hi there","hello there","hy there","hey there"]
time_message = ["good morning", "good afternoon", "good evening", "good night"]
conversation_message =["how are you", "what are you doing", "how is it going", "nice to meet you","what's up"]
thanks_message = ['thanks','thank you','thanks a lot','thank you very much', 'thank you so much','thanks for everything']
bye_message = ["bye", "by", "goodbye", "see you later", "see you soon", "take care", "exit"]
salam = "assalamualaikum"
