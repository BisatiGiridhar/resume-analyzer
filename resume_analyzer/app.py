import streamlit as st
from resume_parser import extract_text_from_pdf
from ats_score import clean_text, calculate_ats_score
from skill_matcher import extract_skills
from suggestions import generate_suggestions

# ---------------- Page Settings ----------------
st.set_page_config(
    page_title="Smart Resume Analyzer",
    page_icon="📄",
    layout="centered"
)

# ---------------- CSS ----------------
st.markdown("""
<style>
html, body, [class*="css"] {
    background-color: #0f172a;
}

.block-container {
    background-color: #f8fafc;
    padding: 2.5rem;
    border-radius: 20px;
    max-width: 900px;
    margin-top: 40px;
}

h1 {
    color: #1e3a8a;
    text-align: center;
    font-size: 48px;
    font-weight: 800;
}

.subtitle {
    text-align: center;
    color: gray;
    margin-bottom: 30px;
    font-size: 18px;
}

.stButton > button {
    background: linear-gradient(to right, #2563eb, #1d4ed8);
    color: white;
    border-radius: 12px;
    height: 50px;
    width: 100%;
    font-size: 20px;
    border: none;
    margin-top: 10px;
}

.stTextArea textarea {
    border-radius: 12px;
    border: 2px solid #2563eb;
}

.stFileUploader {
    border-radius: 12px;
    border: 2px solid #2563eb;
}

.card {
    background: white;
    padding: 20px;
    border-radius: 15px;
    box-shadow: 0px 4px 15px rgba(0,0,0,0.1);
    margin-top: 20px;
}

.score {
    font-size: 50px;
    font-weight: 900;
    color: #1e40af;
    text-align: center;
}
</style>
""", unsafe_allow_html=True)

# ---------------- Title ----------------
st.markdown("<h1>🧠 Smart Resume Analyzer</h1>", unsafe_allow_html=True)
st.markdown("<div class='subtitle'>AI-powered ATS Resume Screening System</div>", unsafe_allow_html=True)

# ---------------- Inputs ----------------
st.markdown("### 📄 Upload Resume")
resume_file = st.file_uploader("Upload Resume (PDF only)", type=["pdf"])

st.markdown("### 📋 Job Description")
job_desc = st.text_area("Paste Job Description Here")

# ---------------- Analyze Button ----------------
if st.button("🚀 Analyze Resume"):
    if resume_file and job_desc:

        with st.spinner("Analyzing your resume..."):
            resume_text = extract_text_from_pdf(resume_file)
            resume_clean = clean_text(resume_text)
            job_clean = clean_text(job_desc)

            resume_skills = extract_skills(resume_clean)
            job_skills = extract_skills(job_clean)

            ats_score = calculate_ats_score(resume_clean, job_clean)
            suggestions = generate_suggestions(resume_skills, job_skills)

        # ---------------- ATS Score ----------------
        st.markdown("<div class='card'>", unsafe_allow_html=True)
        st.markdown("<h2 style='text-align:center;'>📊 ATS Score</h2>", unsafe_allow_html=True)
        st.progress(int(ats_score))
        st.markdown(f"<div class='score'>{ats_score}%</div>", unsafe_allow_html=True)
        st.markdown("</div>", unsafe_allow_html=True)

        # ---------------- Columns ----------------
        col1, col2 = st.columns(2)

        with col1:
            st.markdown("<div class='card'>", unsafe_allow_html=True)
            st.markdown("### ✅ Matched Skills")
            if resume_skills:
                for skill in resume_skills:
                    st.success(skill)
            else:
                st.warning("No matching skills found")
            st.markdown("</div>", unsafe_allow_html=True)

        with col2:
            st.markdown("<div class='card'>", unsafe_allow_html=True)
            st.markdown("### 📌 Suggestions")
            for s in suggestions:
                st.info(s)
            st.markdown("</div>", unsafe_allow_html=True)

    else:
        st.warning("⚠ Please upload resume and paste job description")
