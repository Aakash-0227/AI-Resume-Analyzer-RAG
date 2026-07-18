def job_match_score(resume_text, job_description):

    resume_words = set(resume_text.lower().split())
    jd_words = set(job_description.lower().split())

    matched_skills = resume_words.intersection(jd_words)

    if len(jd_words) == 0:
        return 0

    score = (len(matched_skills) / len(jd_words)) * 100

    return round(score, 2)