import streamlit as st
from langchain.prompts import PromptTemplate
from langchain_community.llms import CTransformers


def getLLamaresponse(input_text, no_words, blog_style):
    llm= CTransformers(model="model\llama-2-7b-chat.ggmlv3.q8_0.bin", device=0, model_type="llama",
                       config = {
                           "temperature": 0.7, 
                           "max_new_tokens" :256})
    
    template = """
    Write a {blog_style} blog on {input_text} that is {no_words} words long.
    """

    prompt = PromptTemplate(input_variables=["blog_style","input_text", "no_words" ], template=template)

        
    response = llm(prompt.format(blog_style=blog_style, input_text=input_text, no_words=no_words))
    print(response)
    return response

st.set_page_config(
    page_title="Generate Blogs",
    page_icon="📝",
    layout="centered",
    initial_sidebar_state="collapsed"
)

st.header("Generate Blogs")

input_text = st.text_input("Enter the Blog topic")

col1, col2 = st.columns([5,5])
with col1:
    no_words = st.text_input("Enter number of words")
with col2:
    blog_style = st.selectbox("Writing the blog for", ("Researcher", "Data Scientist", "common Peole"), index = 0)	

submit = st.button("Generate")

if submit:
    st.write(getLLamaresponse(input_text, no_words, blog_style))

