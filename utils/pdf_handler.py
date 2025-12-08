# PDF extraction functions
import pdfplumber
import streamlit as st

def extract_text_from_pdf(pdf_file):
    """Extract text from PDF file"""
    text = ""
    try:
        with pdfplumber.open(pdf_file) as pdf:
            for page in pdf.pages:
                page_text = page.extract_text()
                if page_text:
                    text += page_text + "\n"
        return text
    except Exception as e:
        st.error(f"Error reading PDF: {e}")
        return ""

def extract_email_phone(text):
    """Extract email and phone from text"""
    import re
    
    email_pattern = r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}'
    phone_pattern = r'[\+]?[(]?[0-9]{3}[)]?[-\s\.]?[0-9]{3}[-\s\.]?[0-9]{4,6}'
    
    emails = re.findall(email_pattern, text)
    phones = re.findall(phone_pattern, text)
    
    return emails, phones

def extract_name(text):
    """Extract likely name from resume"""
    lines = text.split('\n')
    # First non-empty line is usually the name
    for line in lines:
        if line.strip() and len(line.strip()) < 100:
            return line.strip()
    return "Unknown"
