# utils/ats_checker.py

import re

def check_ats_compliance(resume_text):
    """Returns common ATS issues and a summary for the resume text."""
    issues = []
    suggestions = []
    
    # Rule: No graphics or images (PDF text only)
    # (If text extraction worked, assume OK. Warn user if text is very short)
    if len(resume_text) < 200:
        issues.append("Resume text extraction very short or empty. Make sure your PDF is not image-based or scanned.")

    # Rule: Avoid tables
    if re.search(r'\|.*\|', resume_text) or re.search(r'----+', resume_text):
        issues.append("Detected table-like formatting. Tables confuse most ATS systems. Use plain text lists instead.")

    # Rule: Avoid headers/footers (very hard for ATS to parse these)
    # You can't directly detect, but can warn for common header/footer words
    if 'header' in resume_text.lower() or 'footer' in resume_text.lower():
        issues.append("Resumes with info in headers/footers can lose critical content. Put all contacts in body.")

    # Rule: Avoid columns (very hard to auto-detect, give general warning)
    suggestions.append("Avoid columns and sidebars. ATS reads left-to-right and may mix up the order.")

    # Rule: Use standard section titles
    for section in ['Work Experience', 'Education', 'Skills']:
        if section not in resume_text:
            suggestions.append(f"Missing standard section: '{section}' - use standard titles for best results.")

    # Rule: Avoid non-standard fonts (can't detect from text, just warn)
    suggestions.append("Use simple, universal fonts like Arial, Calibri, or Times New Roman for best capatibility.")

    # Rule: File type (Check if streamlit allows .docx, and warn if not)
    # This example only handles PDF uploads.

    # Rule: Section order and keyword placement (handled by your keyword match already)

    # Warn if special characters are excessive
    if len(re.findall(r'[■◆●♦★☆☑✓✗●○•]', resume_text)) > 2:
        issues.append("Found bullet or icon characters. ATS may not recognize graphic bullets. Prefer hyphens '-' or simple dots '.' for bullet points.")

    ats_score = 100 - len(issues)*15  # Each issue reduces score by 15%
    ats_score = max(ats_score, 0)
    return ats_score, issues, suggestions
