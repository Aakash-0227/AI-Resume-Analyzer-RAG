import streamlit as st
import os
from dotenv import load_dotenv
import google.generativeai as genai

from modules.pdf_reader import extract_text_from_pdf
from modules.ats_score import calculate_ats_score
from modules.job_match import job_match_score
from modules.skill_gap import skill_gap_analysis
from modules.interview_questions import generate_interview_questions


# ---------------------------
# Load Gemini API Key
# ---------------------------

load_dotenv()
api_key = os.getenv("GEMINI_API_KEY")

genai.configure(api_key=api_key)


# ---------------------------
# Streamlit UI
# ---------------------------

st.title("AI Resume Analyzer with RAG")
st.write("Upload your resume and paste the job description below.")


# Upload Resume

resume_file = st.file_uploader(
    "Upload Resume (PDF)",
    type=["pdf"]
)


# Job Description

job_description = st.text_area(
    "Paste Job Description"
)


# ---------------------------
# Analyze Resume
# ---------------------------

# -------------------------------
# MAIN ANALYSIS
# -------------------------------

if resume_file is not None and job_description:

    # Extract Resume Text
    resume_text = extract_text_from_pdf(resume_file)

    # ATS SCORE
    ats = calculate_ats_score(
        resume_text,
        job_description
    )

    st.subheader("ATS Score")
    st.progress(int(ats))
    st.write(f"{ats}%")

    # JOB MATCH SCORE
    match_score = job_match_score(
        resume_text,
        job_description
    )

    st.subheader("Job Match Score")
    st.progress(int(match_score))
    st.write(f"{match_score}%")

    # SKILL GAP ANALYSIS
    skills = skill_gap_analysis(
        resume_text,
        job_description
    )

    # MATCHED SKILLS
    st.subheader("Matched Skills")

    if skills["matched_skills"]:
        for skill in skills["matched_skills"]:
            st.success(f"✓ {skill.title()}")
    else:
        st.info("No Matched Skills Found.")

    # MISSING SKILLS
    st.subheader("Missing Skills")

    if skills["missing_skills"]:
        for skill in skills["missing_skills"]:
            st.warning(f"✗ {skill.title()}")
    else:
        st.success("No Missing Skills.")

    # INTERVIEW QUESTIONS
    st.subheader("Interview Questions")

    questions = generate_interview_questions(
        resume_text,
        job_description
    )

    if questions:
        for i, question in enumerate(questions, start=1):
            st.write(f"{i}. {question}")
    else:
        st.info("No Interview Questions Generated.")


# -------------------------------
# WARNING MESSAGES
# -------------------------------

elif resume_file is not None and not job_description:

    st.warning("Please paste the Job Description.")


elif resume_file is None and job_description:

    st.warning("Please upload your Resume.")