# Data storage and retrieval functions
import csv
import os
import json
from datetime import datetime
import pandas as pd
import streamlit as st

RESULTS_FILE = "data/screening_results.csv"
JD_TEMPLATE_FILE = "data/jd_templates.json"

def ensure_directories():
    """Create required directories"""
    os.makedirs("data", exist_ok=True)

def save_screening_result(filename, overall_score, keyword_score, skill_score, 
                          matched_keywords, missing_keywords):
    """Save screening result to CSV"""
    ensure_directories()
    
    row = {
        'Date': datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        'Resume_File': filename,
        'Overall_Score': overall_score,
        'Keyword_Score': keyword_score,
        'Skill_Score': skill_score,
        'Matched_Keywords': len(matched_keywords),
        'Missing_Keywords': len(missing_keywords),
        'Top_Matched': ', '.join(list(matched_keywords)[:5]),
        'Top_Missing': ', '.join(list(missing_keywords)[:5])
    }
    
    try:
        file_exists = os.path.isfile(RESULTS_FILE)
        
        with open(RESULTS_FILE, 'a', newline='', encoding='utf-8') as csvfile:
            fieldnames = ['Date', 'Resume_File', 'Overall_Score', 'Keyword_Score', 
                         'Skill_Score', 'Matched_Keywords', 'Missing_Keywords', 
                         'Top_Matched', 'Top_Missing']
            
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            
            if not file_exists:
                writer.writeheader()
            
            writer.writerow(row)
        
        return True
    except Exception as e:
        st.error(f"Error saving results: {e}")
        return False

def load_screening_results():
    """Load all screening results"""
    ensure_directories()
    
    try:
        if os.path.isfile(RESULTS_FILE):
            return pd.read_csv(RESULTS_FILE)
        else:
            return pd.DataFrame()
    except Exception as e:
        st.error(f"Error loading results: {e}")
        return pd.DataFrame()

def save_jd_template(name, description):
    """Save job description template"""
    ensure_directories()
    
    try:
        if os.path.isfile(JD_TEMPLATE_FILE):
            with open(JD_TEMPLATE_FILE, 'r') as f:
                templates = json.load(f)
        else:
            templates = {}
        
        templates[name] = description
        
        with open(JD_TEMPLATE_FILE, 'w') as f:
            json.dump(templates, f, indent=4)
        
        return True
    except Exception as e:
        st.error(f"Error saving template: {e}")
        return False

def load_jd_templates():
    """Load all JD templates"""
    ensure_directories()
    
    try:
        if os.path.isfile(JD_TEMPLATE_FILE):
            with open(JD_TEMPLATE_FILE, 'r') as f:
                return json.load(f)
        else:
            return {}
    except Exception as e:
        st.error(f"Error loading templates: {e}")
        return {}

def delete_jd_template(name):
    """Delete a JD template"""
    try:
        templates = load_jd_templates()
        if name in templates:
            del templates[name]
            with open(JD_TEMPLATE_FILE, 'w') as f:
                json.dump(templates, f, indent=4)
            return True
        return False
    except Exception as e:
        st.error(f"Error deleting template: {e}")
        return False
