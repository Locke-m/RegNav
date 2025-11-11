import streamlit as st
import PyPDF2
import docx
from io import BytesIO

st.set_page_config(page_title="Red Text Converter", page_icon="🔴", layout="centered")

st.title("🔴 Red Text Converter")
st.markdown("Upload a document and convert all text to red font!")

# File uploader
uploaded_file = st.file_uploader(
    "Choose a document file",
    type=['pdf', 'docx', 'txt'],
    help="Supported formats: PDF, DOCX, TXT"
)

if uploaded_file is not None:
    try:
        # Extract text based on file type
        text = ""
        
        if uploaded_file.type == "application/pdf":
            pdf_reader = PyPDF2.PdfReader(uploaded_file)
            for page in pdf_reader.pages:
                text += page.extract_text() + "\n"
        
        elif uploaded_file.type == "application/vnd.openxmlformats-officedocument.wordprocessingml.document":
            doc = docx.Document(uploaded_file)
            for paragraph in doc.paragraphs:
                text += paragraph.text + "\n"
        
        elif uploaded_file.type == "text/plain":
            text = str(uploaded_file.read(), "utf-8")
        
        if text.strip():
            # Display preview with red text
            st.subheader("Preview (Red Text)")
            st.markdown(f'<div style="color: red; font-family: Arial, sans-serif;">{text.replace(chr(10), "<br>")}</div>', unsafe_allow_html=True)
            
            # Create HTML file with red text
            html_content = f"""<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <title>Red Text Document</title>
    <style>
        body {{
            font-family: Arial, sans-serif;
            padding: 20px;
            color: red;
        }}
        pre {{
            white-space: pre-wrap;
            word-wrap: break-word;
        }}
    </style>
</head>
<body>
    <pre>{text}</pre>
</body>
</html>"""
            
            # Download button
            st.download_button(
                label="📥 Download Red Text (HTML)",
                data=html_content,
                file_name="red_text_document.html",
                mime="text/html"
            )
            
            # Also provide plain text version with instructions
            st.info("💡 The downloaded HTML file will display all text in red when opened in a web browser.")
        else:
            st.warning("⚠️ No text could be extracted from the document.")
    
    except Exception as e:
        st.error(f"❌ Error processing file: {str(e)}")
        st.info("Please make sure the file is not corrupted and is in a supported format.")

else:
    st.info("👆 Please upload a document to get started!")

