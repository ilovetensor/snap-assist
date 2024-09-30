# OCR and Keyword Highlighting App

This Streamlit application allows users to upload images and extract textual content using Optical Character Recognition (OCR) technology. It also provides functionality to highlight specified keywords within the extracted text, aiding in rapid information retrieval.

## Features

- **Image Upload**: Users can upload images in PNG, JPG, or JPEG formats.
- **Text Extraction**: Uses OCR to convert image-based text into plain text.
- **Keyword Highlighting**: Highlights user-specified keywords within the extracted text.

## Requirements

To run this application, you will need Python installed on your machine along with a few additional libraries.

### Dependencies

- Streamlit
- Pillow (PIL Fork)
- Pytesseract

You can install all the necessary libraries using the following command:

```
pip install -r requirements.txt
```

## Setup and Local Deployment

1. **Install Tesseract**: You need Tesseract-OCR installed on your system for the OCR functionalities. Installation instructions for various operating systems are as follows:

   - **Ubuntu/Debian**:
     ```
     sudo apt-get update
     sudo apt-get install tesseract-ocr
     ```
   - **Windows**:
     Download from [here](https://github.com/UB-Mannheim/tesseract/wiki) and install. Ensure the executable is in your PATH.
   - **macOS**:
     ```
     brew install tesseract
     ```

2. **Clone the Repository**: Download or clone the repository to your local machine.

3. **Install Python Dependencies**: Navigate to the cloned directory and run:
   ```
   pip install -r requirements.txt
   ```

4. **Run the Application**: From the command line, navigate to the directory containing `app.py` and run:
   ```
   streamlit run app.py
   ```

5. **Open the Application**: The application should now be running on your local machine at `http://localhost:8501`. Open this address in your web browser to interact with the app.

## Usage

Upload an image through the interface, input a keyword if desired, and click the 'Extract and Highlight Text' button to see the OCR results and highlighted text.
