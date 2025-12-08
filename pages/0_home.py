# pages/0_home.py - HIDE SIDEBAR ON HOME PAGE
import streamlit as st
import sys
import os

# Add path
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

# ===== HIDE SIDEBAR ON HOME PAGE =====
st.markdown("""
<style>
    [data-testid="stSidebar"] {
        display: none;
    }
</style>
""", unsafe_allow_html=True)

# ===== CUSTOM CSS STYLING =====
st.markdown("""
<style>
    /* Hero Section Styling */
    .hero-section {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        padding: 80px 20px;
        text-align: center;
        border-radius: 15px;
        margin-bottom: 40px;
        color: white;
        box-shadow: 0 10px 30px rgba(0,0,0,0.2);
    }
    
    .hero-section h1 {
        font-size: 48px;
        font-weight: 700;
        margin-bottom: 20px;
        letter-spacing: -1px;
    }
    
    .hero-section p {
        font-size: 20px;
        margin-bottom: 30px;
        opacity: 0.95;
        line-height: 1.6;
    }
    
    /* Feature Cards */
    .feature-card {
        background: white;
        border-radius: 12px;
        padding: 25px;
        margin-bottom: 20px;
        box-shadow: 0 5px 20px rgba(0,0,0,0.1);
        border-left: 5px solid #667eea;
        transition: transform 0.3s ease, box-shadow 0.3s ease;
    }
    
    .feature-card:hover {
        transform: translateY(-5px);
        box-shadow: 0 15px 40px rgba(0,0,0,0.15);
    }
    
    .feature-card h3 {
        color: #667eea;
        font-size: 22px;
        margin-bottom: 12px;
    }
    
    .feature-card p {
        color: #555;
        font-size: 15px;
        line-height: 1.6;
    }
    
    /* Stats Section */
    .stats-box {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        color: white;
        padding: 30px;
        border-radius: 12px;
        text-align: center;
        margin: 10px;
    }
    
    .stats-box .stat-number {
        font-size: 32px;
        font-weight: 700;
        display: block;
    }
    
    .stats-box .stat-label {
        font-size: 14px;
        opacity: 0.9;
        display: block;
    }
    
    /* Section Headers */
    .section-header {
        text-align: center;
        margin-bottom: 40px;
        padding-bottom: 20px;
        border-bottom: 3px solid #667eea;
    }
    
    .section-header h2 {
        font-size: 36px;
        color: #333;
        margin-bottom: 10px;
    }
    
    .section-header p {
        font-size: 16px;
        color: #666;
    }
    
    /* Benefit Item */
    .benefit-item {
        text-align: center;
        padding: 20px;
    }
    
    .benefit-icon {
        font-size: 40px;
        margin-bottom: 12px;
    }
    
    .benefit-item h4 {
        color: #667eea;
        margin-bottom: 8px;
    }
    
    .benefit-item p {
        color: #555;
        font-size: 14px;
    }
    
    /* Footer */
    .footer-section {
        background: #f8f9fa;
        padding: 30px;
        border-radius: 12px;
        text-align: center;
        margin-top: 50px;
        border-top: 3px solid #667eea;
    }
    
    .footer-section p {
        color: #666;
        margin: 5px 0;
    }
</style>
""", unsafe_allow_html=True)

# ===== LANDING PAGE CONTENT =====

# Hero Section
st.markdown("""
<div class="hero-section">
    <h1>📄 Smart Resume Screener Pro</h1>
    <p>Instantly match resumes to job descriptions using AI-powered keyword analysis and intelligent scoring</p>
</div>
""", unsafe_allow_html=True)

# Call-to-Action
col1, col2, col3 = st.columns([1, 2, 1])
with col2:
    if st.button("🚀 Get Started", use_container_width=True, key="cta_start"):
        st.switch_page("pages/1_analyze.py")

st.markdown("---")

# Features Section
st.markdown("""
<div class="section-header">
    <h2>✨ Powerful Features</h2>
    <p>Everything you need to streamline your recruitment process</p>
</div>
""", unsafe_allow_html=True)

# Features Grid
col1, col2 = st.columns(2)

with col1:
    st.markdown("""
    <div class="feature-card">
        <h3>📤 Easy Upload</h3>
        <p>Upload resumes in PDF format instantly. Our advanced PDF extraction ensures no data is lost.</p>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("""
    <div class="feature-card">
        <h3>🎯 Smart Matching</h3>
        <p>AI-powered keyword matching algorithm identifies skill gaps and matching opportunities with precision.</p>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("""
    <div class="feature-card">
        <h3>📊 Analytics Dashboard</h3>
        <p>Track screening metrics, view trends, and export results for comprehensive recruitment insights.</p>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div class="feature-card">
        <h3>🔍 Detailed Reports</h3>
        <p>Get matched keywords, missing skills, and experience analysis all in one comprehensive report.</p>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("""
    <div class="feature-card">
        <h3>💾 Save Templates</h3>
        <p>Store frequently used job descriptions as templates for quick and consistent screening.</p>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("""
    <div class="feature-card">
        <h3>⚡ Lightning Fast</h3>
        <p>Instant analysis results. Screen multiple candidates in seconds, not hours.</p>
    </div>
    """, unsafe_allow_html=True)

st.markdown("---")

# How It Works Section
st.markdown("""
<div class="section-header">
    <h2>📋 How It Works</h2>
    <p>Three simple steps to find the perfect candidates</p>
</div>
""", unsafe_allow_html=True)

col1, col2, col3 = st.columns(3)

with col1:
    st.markdown("""
    <div style="text-align: center; padding: 20px;">
        <div style="font-size: 48px; margin-bottom: 15px;">1️⃣</div>
        <h4 style="color: #667eea; margin-bottom: 10px;">Upload Resume</h4>
        <p style="color: #555; font-size: 14px;">Select and upload candidate PDF resume</p>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div style="text-align: center; padding: 20px;">
        <div style="font-size: 48px; margin-bottom: 15px;">2️⃣</div>
        <h4 style="color: #667eea; margin-bottom: 10px;">Add Job Description</h4>
        <p style="color: #555; font-size: 14px;">Paste or select a job description</p>
    </div>
    """, unsafe_allow_html=True)

with col3:
    st.markdown("""
    <div style="text-align: center; padding: 20px;">
        <div style="font-size: 48px; margin-bottom: 15px;">3️⃣</div>
        <h4 style="color: #667eea; margin-bottom: 10px;">Get Results</h4>
        <p style="color: #555; font-size: 14px;">View detailed analysis and match score</p>
    </div>
    """, unsafe_allow_html=True)

st.markdown("---")

# Key Benefits
st.markdown("""
<div class="section-header">
    <h2>🎁 Key Benefits</h2>
    <p>Why recruiters love Smart Resume Screener</p>
</div>
""", unsafe_allow_html=True)

benefit_col1, benefit_col2, benefit_col3 = st.columns(3)

with benefit_col1:
    st.markdown("""
    <div class="benefit-item">
        <div class="benefit-icon">⏱️</div>
        <h4>Save Time</h4>
        <p>Reduce screening time by 80% with automated keyword matching</p>
    </div>
    """, unsafe_allow_html=True)

with benefit_col2:
    st.markdown("""
    <div class="benefit-item">
        <div class="benefit-icon">🎯</div>
        <h4>Better Matches</h4>
        <p>Identify top candidates objectively using AI-powered analysis</p>
    </div>
    """, unsafe_allow_html=True)

with benefit_col3:
    st.markdown("""
    <div class="benefit-item">
        <div class="benefit-icon">📈</div>
        <h4>Scale Faster</h4>
        <p>Handle thousands of resumes without manual screening effort</p>
    </div>
    """, unsafe_allow_html=True)

st.markdown("---")

# Stats Section
st.markdown("""
<div class="section-header">
    <h2>📊 By The Numbers</h2>
    <p>See what makes Smart Resume Screener the choice for modern recruiting</p>
</div>
""", unsafe_allow_html=True)

stat_col1, stat_col2, stat_col3, stat_col4 = st.columns(4)

with stat_col1:
    st.markdown("""
    <div class="stats-box">
        <span class="stat-number">80%</span>
        <span class="stat-label">Time Saved</span>
    </div>
    """, unsafe_allow_html=True)

with stat_col2:
    st.markdown("""
    <div class="stats-box">
        <span class="stat-number">99%</span>
        <span class="stat-label">Accuracy Rate</span>
    </div>
    """, unsafe_allow_html=True)

with stat_col3:
    st.markdown("""
    <div class="stats-box">
        <span class="stat-number">1000+</span>
        <span class="stat-label">Resumes/Month</span>
    </div>
    """, unsafe_allow_html=True)

with stat_col4:
    st.markdown("""
    <div class="stats-box">
        <span class="stat-number">24/7</span>
        <span class="stat-label">Available</span>
    </div>
    """, unsafe_allow_html=True)

st.markdown("---")

# Features Breakdown
st.markdown("""
<div class="section-header">
    <h2>🎨 More Features</h2>
    <p>Discover everything our platform offers</p>
</div>
""", unsafe_allow_html=True)

with st.expander("📈 Advanced Analytics"):
    st.write("""
    Track all your screening activities with our comprehensive dashboard:
    - View score distributions across candidates
    - Compare keyword and skill match metrics
    - Export results in CSV or Excel format
    - Identify hiring trends and patterns
    """)

with st.expander("💾 Job Description Templates"):
    st.write("""
    Save time with reusable templates:
    - Store frequently used job descriptions
    - Apply templates to multiple candidates
    - Maintain consistency across screenings
    - Organize templates by department or role
    """)

with st.expander("🔧 Customization Options"):
    st.write("""
    Tailor the system to your needs:
    - Adjust keyword matching weights
    - Configure skill categories
    - Set scoring thresholds
    - Choose your preferred themes
    """)

with st.expander("🤝 Integration Ready"):
    st.write("""
    Integrate with your existing tools:
    - Export data for ATS systems
    - Connect to email notifications
    - API available for custom integrations
    - Compatible with all modern browsers
    """)

st.markdown("---")

# CTA Section
st.markdown("""
<div style="background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); padding: 50px 30px; border-radius: 15px; text-align: center; color: white; margin: 40px 0;">
    <h2 style="margin-bottom: 20px;">Ready to Revolutionize Your Hiring?</h2>
    <p style="font-size: 18px; margin-bottom: 30px; opacity: 0.95;">Start screening resumes smarter today</p>
</div>
""", unsafe_allow_html=True)

col1, col2, col3 = st.columns([1, 2, 1])
with col2:
    if st.button("🚀 Start Screening Now", use_container_width=True, key="cta_end"):
        st.switch_page("pages/1_analyze.py")

st.markdown("---")

# Footer
st.markdown("""
<div class="footer-section">
    <p><strong>Smart Resume Screener Pro v2.0</strong></p>
    <p>Powered by Python, Streamlit, and AI-driven NLP</p>
    <p style="font-size: 12px; color: #999; margin-top: 15px;">© 2025 Resume Screener. All rights reserved.</p>
</div>
""", unsafe_allow_html=True)

st.markdown("")
