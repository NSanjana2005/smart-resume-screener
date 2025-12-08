# pages/1_analyze.py - COMPLETE WITH FILES DISPLAY & DB DELETE
from utils.ats_checker import check_ats_compliance
import streamlit as st
import sys
import os
import pandas as pd



# Add path
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from utils.pdf_handler import extract_text_from_pdf
from utils.nlp_processing import calculate_match_score
from utils.data_storage import save_screening_result, load_jd_templates

st.title("🔍 Analyze Resume")

# Session state
if "batch_uploaded_files" not in st.session_state:
    st.session_state.batch_uploaded_files = []

if "batch_job_description" not in st.session_state:
    st.session_state.batch_job_description = ""

if "batch_results" not in st.session_state:
    st.session_state.batch_results = None

# Tabs
tab1, tab2 = st.tabs(["Upload Resumes", "Use Template"])

# ============================================================
# TAB 1: UPLOAD RESUMES
# ============================================================
with tab1:
    st.markdown("### 📦 Upload Multiple Resumes")
    st.markdown("Analyze multiple resumes against a single job description")
    
    # Function to add files
    def add_files_to_session(new_files):
        """Add new files to session state list"""
        if new_files:
            file_names = [f.name for f in st.session_state.batch_uploaded_files]
            for file in new_files:
                if file.name not in file_names:
                    st.session_state.batch_uploaded_files.append(file)
    
    # FILE UPLOADER
    uploaded_files = st.file_uploader(
        "Choose PDF files (select multiple by holding Ctrl/Cmd)",
        type=['pdf'],
        accept_multiple_files=True,
        help="Upload multiple resume PDFs at once",
        key="batch_upload"
    )
    
    # Add files to session
    add_files_to_session(uploaded_files)
    
    # ===== DISPLAY FILES TO PROCESS - THIS WAS MISSING =====
    st.subheader("📋 Files to Process")
    
    if len(st.session_state.batch_uploaded_files) > 0:
        st.success(f"✅ {len(st.session_state.batch_uploaded_files)} file(s) ready")
        
        # Display each file with remove button
        for i in range(len(st.session_state.batch_uploaded_files)):
            file = st.session_state.batch_uploaded_files[i]
            
            col1, col2 = st.columns([2, 1])
            
            with col1:
                st.write(f"**{i+1}.** {file.name}")
            
            with col2:
                st.write(f"{file.size/2048:.0f} KB")
            
            
        
        # Clear all button
        if st.button("🗑️ Clear Removed Files", use_container_width=True):
            st.session_state.batch_uploaded_files = []
            st.rerun()
    
    else:
        st.info("📁 No files uploaded yet")
    
    # ===== JOB DESCRIPTION =====
    st.markdown("---")
    st.subheader("📝 Job Description")
    
    jd_method = st.radio(
        "How would you like to provide the job description?",
        ["Paste Job Description", "Select Template"],
        horizontal=True,
        key="batch_jd_method_radio"
    )
    
    batch_job_description = ""
    
    if jd_method == "Paste Job Description":
        batch_job_description = st.text_area(
            "Paste your job description here",
            height=200,
            placeholder="Enter the complete job description...",
            key="batch_jd_textarea",
            value=st.session_state.batch_job_description
        )
        st.session_state.batch_job_description = batch_job_description
    
    else:  # Select Template
        templates = load_jd_templates()
        if templates:
            template_list = list(templates.keys())
            selected_template_name = st.selectbox(
                "Select a template",
                template_list,
                key="batch_template_select"
            )
            batch_job_description = templates[selected_template_name]
            st.session_state.batch_job_description = batch_job_description
            st.success(f"✅ Selected: {selected_template_name}")
        else:
            st.warning("❌ No templates available yet")
            st.info("Create templates in the 'Job Descriptions' tab")
            batch_job_description = ""
    
    # ===== ANALYZE BUTTON =====
    st.markdown("---")
    if st.button(
        "🚀 Analyze All Resumes",
        type="primary",
        use_container_width=True,
        key="batch_analyze_button"
    ):
        # Validate inputs
        if not st.session_state.batch_uploaded_files:
            st.error("❌ Please upload at least one resume")
            st.stop()
        
        if not batch_job_description.strip():
            st.error("❌ Please enter or select a job description")
            st.stop()
        
        # Process files
        progress_bar = st.progress(0)
        status_placeholder = st.empty()
        
        batch_results = []
        
        for file_idx, pdf_file in enumerate(st.session_state.batch_uploaded_files):
            # Update progress
            progress_value = (file_idx + 1) / len(st.session_state.batch_uploaded_files)
            progress_bar.progress(progress_value)
            status_placeholder.text(
                f"⏳ Processing {file_idx + 1}/{len(st.session_state.batch_uploaded_files)}: {pdf_file.name}"
            )
            
            # Extract text
            resume_text = extract_text_from_pdf(pdf_file)

            if resume_text.strip():
                ats_score, ats_issues, ats_tips = check_ats_compliance(resume_text)
                # Store or display as needed per file
            else:
                # Handle empty case
                ats_score, ats_issues, ats_tips = 0, ["No text found"], []

            ats_score, ats_issues, ats_tips = check_ats_compliance(resume_text)

            if ats_tips:
                st.markdown("**Tips:**")
                for tip in ats_tips:
                    st.info(tip)
            
            if not resume_text.strip():
                batch_results.append({
                    'Resume': pdf_file.name,
                    'Overall_Score': 0,
                    'Keyword_Score': 0,
                    'Skill_Score': 0,
                    'Status': '❌ No text found'
                })
                continue
            
            try:
                # Calculate match
                score_data = calculate_match_score(resume_text, batch_job_description)
                
                # Save to CSV
                save_screening_result(
                    filename=pdf_file.name,
                    overall_score=score_data['overall_score'],
                    keyword_score=score_data['keyword_score'],
                    skill_score=score_data['skill_score'],
                    matched_keywords=score_data['matched_keywords'],
                    missing_keywords=score_data['missing_keywords']
                )
                
                batch_results.append({
                    'Resume': pdf_file.name,
                    'Overall_Score': score_data['overall_score'],
                    'Keyword_Score': score_data['keyword_score'],
                    'Skill_Score': score_data['skill_score'],
                    'Status': '✅ Success'
                })
            
            except Exception as e:
                batch_results.append({
                    'Resume': pdf_file.name,
                    'Overall_Score': 0,
                    'Keyword_Score': 0,
                    'Skill_Score': 0,
                    'Status': '❌ Error'
                })

                ats_score, ats_issues, ats_tips = check_ats_compliance(resume_text)

        

        
        # Clear progress
        progress_bar.empty()
        status_placeholder.empty()
        
        # Store in session
        st.session_state.batch_results = batch_results
    
    # ===== DISPLAY RESULTS =====
    if st.session_state.batch_results:
        st.markdown("---")
        st.success("✅ Analysis Complete!")
        
        results_df = pd.DataFrame(st.session_state.batch_results)
        results_df = results_df.sort_values('Overall_Score', ascending=False).reset_index(drop=True)
        
        # Summary metrics
        st.subheader("📊 Summary")
        col1, col2, col3, col4 = st.columns(4)
        
        successful_count = len(results_df[results_df['Status'] == '✅ Success'])
        
        with col1:
            st.metric("Total Resumes", len(results_df))
        with col2:
            st.metric("Successfully Analyzed", successful_count)
        with col3:
            if successful_count > 0:
                avg = results_df[results_df['Status'] == '✅ Success']['Overall_Score'].mean()
                st.metric("Average Score", f"{avg:.1f}%")
            else:
                st.metric("Average Score", "N/A")
        with col4:
            if successful_count > 0:
                best = results_df[results_df['Status'] == '✅ Success']['Overall_Score'].max()
                st.metric("Best Score", f"{best:.1f}%")
            else:
                st.metric("Best Score", "N/A")
        
        # Results table
        st.markdown("---")
        st.subheader("📋 All Results")
        st.dataframe(results_df, use_container_width=True)
        
        # ===== DELETE FROM DATABASE SECTION =====
        st.markdown("---")
        st.subheader("🗑️ Remove Results from Database")
        
        st.warning("⚠️ Use this to delete records from the database:")
        
        # Show all results with checkboxes for deletion
        results_to_delete = st.multiselect(
            "Select resumes to remove from database:",
            results_df['Resume'].tolist(),
            key="delete_select"
        )
        
        if st.button("🗑️ Delete Selected Results", type="secondary"):
            if results_to_delete:
                # Load current database
                try:
                    db_df = pd.read_csv("data/screening_results.csv")
                    
                    # Remove selected resumes from database
                    db_df = db_df[~db_df['Resume_File'].isin(results_to_delete)]
                    
                    # Save updated database
                    db_df.to_csv("data/screening_results.csv", index=False)
                    
                    st.success(f"✅ Deleted {len(results_to_delete)} records from database")
                
                except Exception as e:
                    st.error(f"❌ Error deleting: {str(e)}")
            else:
                st.warning("Select at least one resume to delete")
        
        # Download options
        st.markdown("---")
        st.subheader("💾 Export Results")
        
        col_d1, col_d2, col_d3 = st.columns(3)
        
        with col_d1:
            csv_buffer = results_df.to_csv(index=False)
            st.download_button(
                "📥 Download CSV",
                csv_buffer,
                f"batch_results_{pd.Timestamp.now().strftime('%Y%m%d_%H%M%S')}.csv",
                "text/csv"
            )
        
        with col_d2:
            if st.checkbox("🏆 Show Top Candidates"):
                top_5 = results_df[results_df['Status'] == '✅ Success'].head(5)
                if len(top_5) > 0:
                    st.markdown("---")
                    for rank, (_, row) in enumerate(top_5.iterrows(), 1):
                        if row['Overall_Score'] >= 80:
                            medal = "🥇"
                        elif row['Overall_Score'] >= 60:
                            medal = "🥈"
                        else:
                            medal = "🥉"
                        st.write(f"{medal} **{rank}.** {row['Resume']} - {row['Overall_Score']}%")
        
        with col_d3:
            if st.button("🔄 Start New Analysis", use_container_width=True):
                # Clear all session state
                st.session_state.clear()
                st.rerun()



# ============================================================
# TAB 2: USE TEMPLATE
# ============================================================
with tab2:
    st.markdown("### Use Job Description Template")
    
    templates = load_jd_templates()
    
    if templates:
        selected_template = st.selectbox(
            "Select template",
            list(templates.keys()),
            key="template_select"
        )
        
        uploaded_file = st.file_uploader(
            "Upload Resume (PDF)",
            type=['pdf'],
            key="template_upload"
        )
        
        if st.button("Analyze with Template", key="template_analyze"):
            if uploaded_file:
                resume_text = extract_text_from_pdf(uploaded_file)
                scores = calculate_match_score(resume_text, templates[selected_template])
                
                st.success("✅ Analysis Complete!")
                
                m1, m2, m3 = st.columns(3)
                with m1:
                    st.metric("Overall Score", f"{scores['overall_score']}%")
                with m2:
                    st.metric("Keyword Score", f"{scores['keyword_score']}%")
                with m3:
                    st.metric("Skill Score", f"{scores['skill_score']}%")
            else:
                st.error("Upload resume first")
    else:
        st.info("No templates available. Create one in Job Descriptions tab.")
