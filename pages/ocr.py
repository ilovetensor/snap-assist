import streamlit as st
from PIL import Image
import pytesseract
import re

def extract_text(image):
    """ Extract text from image using OCR (Tesseract). """
    return pytesseract.image_to_string(image)

def highlight_text(text, keyword):
    """ Highlight occurrences of the keyword in text. """
    highlighted = re.sub(f'(?i)({re.escape(keyword)})', r'<mark>\1</mark>', text)
    return f"<style>mark{{background-color: yellow;}}</style>{highlighted}"

st.title('OCR and Keyword Highlighting App')

col1, col2 = st.columns(2, gap='medium')

with col1:
    uploaded_file = st.file_uploader("Choose an image...", type=['png', 'jpg', 'jpeg'])
    keyword = st.text_input("Enter the keyword to search")
    process_button = st.button('Extract and Highlight Text')

if uploaded_file is not None:
    image = Image.open(uploaded_file)

    # Create two columns: one for the image and one for text

    with col2:
        st.image(image, caption='Uploaded Image', use_column_width=True)

    if process_button:
        
        with st.spinner('Extracting and highlighting text...'):
            text = extract_text(image)
            if keyword:
                text = highlight_text(text, keyword)
            st.subheader('Processed Text')
            st.markdown(text, unsafe_allow_html=True)