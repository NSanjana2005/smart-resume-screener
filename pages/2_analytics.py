# pages/2_analytics.py - ANALYTICS PAGE - FIXED
import streamlit as st
import sys
import os
from io import BytesIO

# Add path
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import pandas as pd
import plotly.express as px
from utils.data_storage import load_screening_results

st.title("📊 Analytics Dashboard")

# Load data
df = load_screening_results()

if df.empty:
    st.info("No data available. Analyze resumes to see analytics.")
else:
    # Overview metrics
    st.markdown("### 📈 Overview")
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        st.metric("Total Analyses", len(df))
    with col2:
        st.metric("Avg Overall Score", f"{df['Overall_Score'].mean():.1f}%")
    with col3:
        st.metric("Highest Score", f"{df['Overall_Score'].max():.1f}%")
    with col4:
        st.metric("Lowest Score", f"{df['Overall_Score'].min():.1f}%")
    
    st.markdown("---")
    
    # Charts
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("### Score Distribution")
        fig = px.histogram(df, x='Overall_Score', nbins=10, 
                          title="Overall Score Distribution")
        st.plotly_chart(fig, use_container_width=True)
    
    with col2:
        st.markdown("### Score Types Comparison")
        fig = px.box(df[['Overall_Score', 'Keyword_Score', 'Skill_Score']],
                    title="Score Comparison")
        st.plotly_chart(fig, use_container_width=True)
    
    # Detailed table
    st.markdown("---")
    st.markdown("### 📋 Detailed Results")
    st.dataframe(df, use_container_width=True)
    
    # Download options
    st.markdown("---")
    st.markdown("### 💾 Export Results")
    
    col1, col2 = st.columns(2)
    
    with col1:
           # Download as Excel - FIXED
        try:
            excel_buffer = BytesIO()
            with pd.ExcelWriter(excel_buffer, engine='openpyxl') as writer:
                df.to_excel(writer, sheet_name='Results', index=False)
            excel_buffer.seek(0)
            
            st.download_button(
                label="📥 Download Excel",
                data=excel_buffer.getvalue(),
                file_name=f"analytics_{pd.Timestamp.now().strftime('%Y%m%d_%H%M%S')}.xlsx",
                mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
            )
        except Exception as e:
            st.warning("⚠️ Excel export not available. Use CSV instead.")
            st.write(f"Error: {str(e)}")
        
    
    
