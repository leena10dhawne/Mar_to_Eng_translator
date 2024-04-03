## PDF Translator using MyMemory Translation API ##
# This Streamlit web application allows users to upload a PDF file and translate its text content to different languages using the MyMemory Translation API.

## Features:
# Upload PDF File: Users can upload their PDF files using the file uploader component.
# Extract Text: The uploaded PDF file's text content is extracted using the pdfplumber library.
# Translate Text: The extracted text is then translated into the selected target language using the MyMemory Translation API.
# Select Target Language: Automaticaly translate in English,
# Display Original and Translated Text: The original text extracted from the PDF and the translated text are displayed to the user.

## Dependencies:
# streamlit: Streamlit is used to create the web application interface.
# pdfplumber: Pdfplumber is used to extract text from PDF files.
# requests: Requests library is used to make HTTP requests to the MyMemory Translation API.


## Usage:
# Upload PDF File: Click the "Upload your PDF file" button to select and upload the PDF file you want to translate.
# Select Translation Language: Choose the target language for translation from the dropdown menu.
# View Translated Text: Once the translation is complete, the original text from the PDF and its translated version will be displayed on the web interface.

## Note:
# The translation may take some time depending on the size of the uploaded PDF file and the number of pages it contains.
# In case of any errors during translation, appropriate error messages will be displayed to the user.
