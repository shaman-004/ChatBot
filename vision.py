from dotenv import load_dotenv
load_dotenv()

import streamlit as st
import os
import google.generativeai as genai
from PIL import Image
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))


model=genai.GenerativeModel("gemini-pro-vision")
def gemini_response(question,image):
    if question!="":
        response=model.generate_content([question,image])
    else:
        response=model.generate_content(image)
    return response.text

st.set_page_config(page_title="qemini image demo")

st.header("gemini llm")

question = st.text_input("Ask a question:",key="input")



upload_file= st.file_uploader("choose an image",type=["jpg","jpeg","png"])
image=None
if upload_file is not None:
    image=Image.open(upload_file)
    st.image(image,caption="uploaded image",use_column_width=True)

submit=st.button("tell me about the image!")

if submit:
    response=gemini_response(question,image)
    st.subheader("the response is")
    st.write(response)