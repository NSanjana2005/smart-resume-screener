# app.py - Simplified version with built-in navigation
import streamlit as st
import os
import sys
import pandas as pd

# Add current directory to path
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

# Page configuration
st.set_page_config(
    page_title="Smart Resume Screener Pro",
    page_icon="📄",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom sidebar styling

with st.sidebar:
   
    
    # Sidebar info box
    st.markdown("### 📊 Quick Stats")
    
    try:
        if os.path.exists("data/screening_results.csv"):
            df = pd.read_csv("data/screening_results.csv")
            col1, col2 = st.columns(2)
            with col1:
                st.metric("Total Analyses", len(df))
            with col2:
                st.metric("Avg Score", f"{df['Overall_Score'].mean():.1f}%")
        else:
            st.info("No data yet. Start analyzing resumes!")
    except:
        st.warning("Could not load statistics")
    
    st.markdown("---")
   
# Define pages list
pages = [
    st.Page("pages/0_home.py", title="Home", icon="🏠"),
    st.Page("pages/1_analyze.py", title="Analyze Resume", icon="🔍"),
    st.Page("pages/2_analytics.py", title="Analytics", icon="📊"),
    st.Page("pages/3_manage_jd.py", title="Job Descriptions", icon="📄"),
    st.Page("pages/4_settings.py", title="Settings", icon="⚙️"),
]

# Create and run navigation
nav = st.navigation(pages)
nav.run()
