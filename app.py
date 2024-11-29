from dotenv import load_dotenv
load_dotenv()
import streamlit as st
import os
import google.generativeai as genai
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

#model = genai.GenerativModel("gemini-flash-1.5")
model = genai.GenerativeModel("gemini-pro")

def my_output(query):
    response= model.generate_content(query)
    return response.text

## UI Development using stramlit

st.set_page_config(page_title="SMART_BOT")
st.header("SMART_BOT")
input=st.text_input("Input",key="input")
submit=st.button("Ask Your Query")

if submit:
    response=my_output(input)
    st.subheader("The Response is:")
    st.write(response)
    