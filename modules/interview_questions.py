def generate_interview_questions(resume_text, job_description):

    questions = []

    resume_text = resume_text.lower()
    job_description = job_description.lower()

    if "python" in resume_text:
        questions.append(
            "Explain Python's advantages in AI applications."
        )

    if "machine learning" in resume_text:
        questions.append(
            "Explain one Machine Learning project you have worked on."
        )

    if "langchain" in job_description:
        questions.append(
            "What is LangChain and where is it used?"
        )

    if "rag" in job_description:
        questions.append(
            "Explain Retrieval-Augmented Generation."
        )

    if "streamlit" in job_description:
        questions.append(
            "Why do we use Streamlit in AI applications?"
        )

    if "nlp" in job_description:
        questions.append(
            "What is NLP and how is it used in Generative AI?"
        )

    if len(questions) == 0:
        questions.append(
            "Tell me about yourself and your AI projects."
        )

    return questions