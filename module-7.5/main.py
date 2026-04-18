import streamlit as st
from google import genai
from dotenv import load_dotenv
import os
from PIL import Image


def uploadImage():
    imgFile = st.file_uploader("Upload your screenshot containing the error for debugging:", type=["jpg", "jpeg", "webp", "png"], accept_multiple_files=False, max_upload_size=5)
    if imgFile:
        return Image.open(imgFile)


def debug(client, img):
    aiResponse = client.models.generate_content(
        model = "gemini-3-flash-preview", contents = [img, "Debug the issue, then explain the problem and its solution line by line in a clear, easy-to-understand tone. Provide a detailed explanation wherever necessary."]
    )
    return aiResponse


load_dotenv()

apiKey = os.environ.get("ApiKey")
client = genai.Client(api_key=apiKey)
st.title("Debugger AI", text_alignment="center", anchor=False)
pilImage = uploadImage()
debugButton = st.button("Debug", type="secondary",width="stretch", icon="🔧", icon_position="left")
st.divider()

if pilImage != None and debugButton != False:
    debugSolution = debug(client=client, img=pilImage)
    st.markdown(f"### Solution:\n {debugSolution.text}")
elif pilImage == None and debugButton == True:
    st.warning("An image is required to provide a solution!")
else:
    st.markdown("### Solution:")

st.divider()
resetButton = st.button("Clear All", type="secondary",width="content")
if resetButton:
    debugSolution = None