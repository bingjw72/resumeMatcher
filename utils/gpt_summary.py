import openai

def generate_candidate_summary(candidate_text, jd_text, similarity, model="gpt-4"):
    prompt = f"""
    You are an AI hiring assistant tasked with evaluating a candidate resume against a specific job description.
    You are given:

    1. The full resume of a candidate
    2. The full job description they are applying to
    3. A precomputed similarity score between the two (based on vector embeddings)

    Your task is to write a clear, professional, and structured summary focused on the candidate's suitability for the job.

    Please include:
    - A concise overview of the candidate's background, total years of experience, and main areas of expertise.
    - Key strengths relevant to the job, such as overlapping skills, tools, and project experience.
    - Potential weaknesses or mismatches, such as lack of required experience, skill gaps, or inconsistent work history.
    - A final reasoning based on the similarity score ({similarity:.4f}) to conclude how well this candidate fits the job.

    Do not repeat or paraphrase the job description. You may reference the job requirements only to assess fit, but focus your writing on the candidate.

    Job Description:
    """
    {jd_text}
    """

    Resume:
    """
    {candidate_text}
    """

    Write the output in paragraphs with a professional tone.
    """

    response = openai.ChatCompletion.create(
        model=model,
        messages=[{"role": "user", "content": prompt}],
        temperature=0.3
    )
    return response["choices"][0]["message"]["content"].strip()