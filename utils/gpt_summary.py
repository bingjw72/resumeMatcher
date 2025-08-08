import openai

def generate_candidate_summary(candidate_text, jd_text, similarity, model="gpt-4"):
    prompt = f"""
    You are an assistant that evaluates job candidate resumes based on a job description.
    Given the following similarity score and texts, summarize why this candidate is a good match for the job, including both strengths and potential weaknesses.
    Make your summary clear, professional, and focused on alignment with job needs.

    Job Description:
    """
    {jd_text}
    """

    Resume:
    """
    {candidate_text}
    """

    Similarity Score: {similarity:.4f}

    Summary:
    """

    response = openai.ChatCompletion.create(
        model=model,
        messages=[{"role": "user", "content": prompt}],
        temperature=0.3
    )
    return response["choices"][0]["message"]["content"].strip()