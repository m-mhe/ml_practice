from google import genai
import os
from dotenv import load_dotenv
import streamlit as st
load_dotenv()
apikey = os.environ.get("ApiKey")

client = genai.Client(api_key=apikey)


st.header("Ask Anything")
userInput = st.text_input("What you want to know?", value=None)
st.divider()
if userInput:
    genContent = client.models.generate_content(
        model = "gemini-3-flash-preview", contents = userInput
    )
    st.markdown(genContent.text)