from dotenv import load_dotenv
load_dotenv()

import streamlit as st
import os
import google.generativeai as genai

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))


model=genai.GenerativeModel("gemini-pro")
def gemini_response(question):
    response=model.generate_content(question)
    return response.text

st.set_page_config(page_title="q&a demo")

st.header("gemini llm")

question = st.text_input("Ask a question:",key="input")

submit=st.button("Submit")

if submit:
    response=gemini_response(question)
    st.write(response)

