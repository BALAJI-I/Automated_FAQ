from dotenv import load_dotenv
import os
import streamlit as st

load_dotenv() #env variable will be created

GROQ_API_KEY = os.getenv('GROQ_API_KEY')

from langchain_groq import ChatGroq
from langchain_core.prompts import PromptTemplate

# Define prompt
prompt_template = """
I have a product description below. Based on this description, generate a list of frequently asked questions (FAQs) that potential customers might have. Ensure the questions cover various aspects of the product, including its features, usage, benefits, maintenance, and any other relevant information. Here is the product description:

{text}

Please provide the FAQs along with their respective answers.
FAQs:
"""
prompt = PromptTemplate.from_template(prompt_template)

model = ChatGroq(
    temperature=0,
    model="llama3-70b-8192",
)
article = """<YOUR DESCRIPTION>"""

chain = prompt | model

def summerise_article(article):
    return chain.invoke({"text": article}).content

st.title('FAQ Generator')

uploaded_file = st.file_uploader("Upload your FAQ in .txt format", type="txt")

if uploaded_file is not None:
    file_content = uploaded_file.read().decode("utf-8")

    st.text_area("Your Product Description", file_content, height=200)

    if st.button("Generate FAQs"):
    
        sum_article = summerise_article(file_content)
        st.text_area("Frequently Asked Question", sum_article, height=400)