import streamlit as st
import pdfplumber
import requests


# Dictionary mapping language names to their corresponding codes
language_codes = {
    'English': 'en',
    'Marathi': 'mr' 
}

st.title("Welcome To PDF Translator")
st.header("Upload a Marathi PDF file and translate it to English")

# Function to translate text using MyMemory translation service
def translate_text(text, target_language):
    url = 'https://api.mymemory.translated.net/get'
    translated_chunks = []
    chunk_size = 500  # Maximum allowed query length

    # Split the text into chunks
    for i in range(0, len(text), chunk_size):
        chunk = text[i:i + chunk_size]

        data = {
            'q': chunk,
            'langpair': f'mr|{target_language}'
        }

        try:
            response = requests.post(url, data=data)
            response.raise_for_status()  # Raise an exception for HTTP errors
            translated_text = response.json()['responseData']['translatedText']
            translated_chunks.append(translated_text)
        except Exception as e:
            st.error(f"Error occurred during translation: {e}")
            return None

    # Combine translated chunks into a single string
    translated_text = ' '.join(translated_chunks)
    return translated_text


# Function to extract text from a PDF file
def extract_text_from_pdf(file):
    text = ""
    with pdfplumber.open(file) as pdf:
        for page_number, page in enumerate(pdf.pages, 1):
            try:
                page_text = page.extract_text()
                text += page_text
            except Exception as e:
                st.warning(f"Failed to extract text from page {page_number}: {e}")
    return text

# Upload PDF file
uploaded_file = st.file_uploader('Upload your PDF file', type=['pdf'])

if uploaded_file is not None:
    # Extract text from PDF
    original_text = extract_text_from_pdf(uploaded_file)
    
    # Display original text
    st.subheader('Original Marathi PDF File:')
    st.write(original_text)
    
    # Translate text
    translated_text = translate_text(original_text, 'en')
    
    # Display translated text
    st.subheader('Translated Text:')
    st.write(translated_text)