# NLP processing functions
import re
from collections import Counter

def clean_text(text):
    """Clean and normalize text"""
    text = text.lower()
    text = re.sub(r'\s+', ' ', text)
    text = re.sub(r'[^a-z0-9\s]', ' ', text)
    return text.strip()

def extract_keywords(text):
    """Extract important keywords from text"""
    stop_words = {
        'the', 'is', 'at', 'which', 'on', 'a', 'an', 'as', 'are', 'was', 'were',
        'been', 'be', 'have', 'has', 'had', 'do', 'does', 'did', 'will', 'would',
        'could', 'should', 'may', 'might', 'can', 'of', 'in', 'to', 'for', 'with',
        'and', 'or', 'but', 'not', 'this', 'that', 'these', 'those', 'i', 'you',
        'he', 'she', 'it', 'we', 'they', 'what', 'who', 'how', 'when', 'where',
        'why', 'all', 'each', 'every', 'both', 'few', 'more', 'most', 'some',
        'such', 'no', 'nor', 'only', 'own', 'same', 'so', 'than', 'too', 'very'
    }
    
    words = text.split()
    keywords = {word for word in words if word not in stop_words and len(word) >= 3}
    return keywords

def extract_experience(text):
    """Extract years of experience"""
    pattern = r'(\d+)\+?\s*(?:years?|yrs?)'
    matches = re.findall(pattern, text.lower())
    return matches

def extract_skills(text):
    """Extract common skills from text"""
    common_skills = {
        'python', 'java', 'javascript', 'typescript', 'react', 'angular', 'vue',
        'sql', 'mysql', 'postgresql', 'mongodb', 'aws', 'azure', 'gcp',
        'docker', 'kubernetes', 'jenkins', 'git', 'linux', 'windows', 'macos',
        'agile', 'scrum', 'jira', 'html', 'css', 'nodejs', 'express',
        'django', 'flask', 'fastapi', 'rest', 'graphql', 'microservices',
        'cloud', 'devops', 'ci/cd', 'machine learning', 'data science',
        'tensorflow', 'pytorch', 'keras', 'nlp', 'computer vision'
    }
    
    clean = clean_text(text)
    found_skills = {skill for skill in common_skills if skill in clean}
    return found_skills

def calculate_match_score(resume_text, job_description):
    """Calculate matching score with enhanced metrics"""
    clean_resume = clean_text(resume_text)
    clean_jd = clean_text(job_description)
    
    resume_keywords = extract_keywords(clean_resume)
    jd_keywords = extract_keywords(clean_jd)
    
    resume_skills = extract_skills(clean_resume)
    jd_skills = extract_skills(clean_jd)
    
    # Keyword matching
    matched_keywords = resume_keywords.intersection(jd_keywords)
    missing_keywords = jd_keywords - resume_keywords
    
    # Skill matching
    matched_skills = resume_skills.intersection(jd_skills)
    missing_skills = jd_skills - resume_skills
    
    # Calculate scores
    keyword_score = (len(matched_keywords) / len(jd_keywords)) * 100 if jd_keywords else 0
    skill_score = (len(matched_skills) / len(jd_skills)) * 100 if jd_skills else 0
    
    # Overall score (weighted average)
    overall_score = (keyword_score * 0.6 + skill_score * 0.4)
    
    return {
        'overall_score': round(overall_score, 2),
        'keyword_score': round(keyword_score, 2),
        'skill_score': round(skill_score, 2),
        'matched_keywords': matched_keywords,
        'missing_keywords': missing_keywords,
        'matched_skills': matched_skills,
        'missing_skills': missing_skills
    }
