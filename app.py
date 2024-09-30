import streamlit as st 
import pandas as pd
from streamlit_extras.switch_page_button import switch_page 

st.set_page_config(page_icon="🧬", layout="wide")


def add_blank_space(n: int) -> None:
    """Generate n blank spaces"""
    for _ in range(n):
        st.write(" ")



st.title("SnapScript 🧬")
st.subheader(":grey[Your very own OCR and Doc Search Tool]")

add_blank_space(4)
desc_cols = st.columns(2)
with desc_cols[0]:
#     st.markdown("""Now it is easy to generate flowchart using LLMs. You can now generate complete flow diagrams for either your strategies, or steps or your code if you want to understand. We use **:green[Mermaid.js]** and **:orange[OpenAI]** to generate beautiful flowcharts for your informations. 
#                 """)
    st.markdown("""Upload an image file for OCR processing. Display the extracted text from the image. Enter keywords to search within the extracted text. Display search results on the same page, highlighting the matching sections.
                """)
add_blank_space(3)

get_started = st.button("**Get Started**", type="primary")

if get_started:
    switch_page("ocr")


st.info("Features like Qwen2Vl require GPU support. Couldn't implement it on Streamlit Sharing. Please run it locally to experience all features.")