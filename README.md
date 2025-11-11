# Red Text Converter

A simple Streamlit app that converts all text from uploaded documents to red font color.

## Features

- Upload PDF, DOCX, or TXT files
- Extract text from documents
- Convert all text to red color
- Download the converted document as an HTML file

## Installation

1. Clone this repository:
```bash
git clone <your-repo-url>
cd "Cursor Test"
```

2. Install the required dependencies:
```bash
pip install -r requirements.txt
```

## Usage

1. Run the Streamlit app:
```bash
streamlit run app.py
```

2. Open your browser and navigate to the URL shown in the terminal (usually `http://localhost:8501`)

3. Upload a document (PDF, DOCX, or TXT)

4. Preview the red text conversion

5. Click the download button to save the HTML file with red text

## Supported File Formats

- **PDF** (.pdf)
- **Word Documents** (.docx)
- **Plain Text** (.txt)

## Requirements

- Python 3.7+
- Streamlit
- PyPDF2
- python-docx

## License

MIT License

