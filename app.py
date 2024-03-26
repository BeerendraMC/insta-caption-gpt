import os
from apikey import apikey

import streamlit as st
from langchain.llms import OpenAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain

os.environ['OPENAI_API_KEY'] = apikey

# App framework
st.title('💥 Instagram Caption GPT')
st.markdown('Crafted with ❤️ by [Beerendra](https://github.com/beerendramc)')
prompt = st.text_input('Enter the post details to which you need a caption')

# Prompt templates
caption_template = PromptTemplate(
    input_variables=['post_info'],
    template='write me a caption for an instagram post about {post_info}'
)

# Llms
llm = OpenAI(temperature=0.9)
caption_chain = LLMChain(llm=llm, prompt=caption_template)

# Show output
if prompt:
    response = caption_chain.run(post_info=prompt)
    st.write(response)
