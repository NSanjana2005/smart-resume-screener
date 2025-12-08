# Settings page
import streamlit as st

st.title("⚙️ Settings & Preferences")

st.markdown("### Display Settings")
theme = st.selectbox("Theme", ["Light", "Dark", "Auto"])
st.success(f"Theme set to: {theme}")

st.markdown("### Analysis Settings")
col1, col2 = st.columns(2)

with col1:
    keyword_weight = st.slider("Keyword Match Weight (%)", 0, 100, 60)

with col2:
    skill_weight = st.slider("Skill Match Weight (%)", 0, 100, 40)

st.markdown("### Data Management")

col1, col2, col3 = st.columns(3)

with col1:
    if st.button("Clear All Results"):
        import os
        if os.path.exists("data/screening_results.csv"):
            os.remove("data/screening_results.csv")
            st.success("Results cleared")

with col2:
    if st.button("Clear Templates"):
        import os
        if os.path.exists("data/jd_templates.json"):
            os.remove("data/jd_templates.json")
            st.success("Templates cleared")

with col3:
    st.info("ℹ️ Settings auto-save")

st.markdown("---")
st.markdown("**App Version:** 2.0 Pro | **Last Updated:** 2025")
