def skill_gap_analysis(resume_text, job_description):

    resume_words = set(resume_text.lower().split())
    jd_words = set(job_description.lower().split())

    matched_skills = list(resume_words.intersection(jd_words))
    missing_skills = list(jd_words - resume_words)

    return {
        "matched_skills": matched_skills,
        "missing_skills": missing_skills
    }