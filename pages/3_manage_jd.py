# Job description template management
import streamlit as st
import sys
sys.path.append('..')

from utils.data_storage import save_jd_template, load_jd_templates, delete_jd_template

st.title("📄 Job Description Templates")

tab1, tab2 = st.tabs(["View Templates", "Create Template"])

with tab1:
    st.markdown("### Saved Templates")
    
    templates = load_jd_templates()
    
    if templates:
        for name, description in templates.items():
            with st.expander(f"📋 {name}"):
                st.write(description)
                
                col1, col2 = st.columns([3, 1])
                with col2:
                    if st.button(f"Delete", key=f"del_{name}"):
                        delete_jd_template(name)
                        st.success(f"Deleted: {name}")
                        st.rerun()
    else:
        st.info("No templates yet. Create one to get started.")

with tab2:
    st.markdown("### Create New Template")
    
    template_name = st.text_input("Template Name", placeholder="e.g., Senior Python Developer")
    template_description = st.text_area("Job Description", height=300, 
                                       placeholder="Paste complete job description...")
    
    if st.button("Save Template", type="primary", use_container_width=True):
        if template_name and template_description:
            if save_jd_template(template_name, template_description):
                st.success(f"✅ Template saved: {template_name}")
        else:
            st.error("Enter name and description")
