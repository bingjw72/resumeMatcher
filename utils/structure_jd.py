# structure_jd.py
import openai
import os
import textwrap

def structure_job_description(jd_text, model="gpt-4"):
    """
    Use OpenAI API to structure a job description into key fields.

    Parameters:
    - jd_text (str): Raw job description text input
    - model (str): OpenAI model to use (default: gpt-4)

    Returns:
    - str: JSON-like structured output (as string)
    """
    openai.api_key = os.getenv("OPENAI_API_KEY")
    prompt = textwrap.dedent(f"""
    You are a helpful assistant tasked with analyzing job descriptions.

    Please extract the following structured fields from the job description below and return in clean JSON format:
    - role_title: the job title
    - responsibilities: a list of core responsibilities
    - required_skills: a list of skills or qualifications explicitly required
    - preferred_skills: a list of nice-to-have or preferred skills (if any)
    - tools: a list of technologies, frameworks, or platforms mentioned
    - domain: (optional) the industry or business context

    Job Description:
    {jd_text}

    Only return JSON.
    """)

    response = openai.ChatCompletion.create(
        model=model,
        messages=[{"role": "user", "content": prompt}],
        temperature=0.2
    )

    return response["choices"][0]["message"]["content"].strip()

# Example usage
if __name__ == "__main__":
    example_jd = """
We are looking for a Data Scientist with strong experience in Python, SQL, and machine learning. 
Responsibilities include building data pipelines, predictive models, and dashboards. 
Experience with AWS and Tableau is a plus. 
"""
    print(structure_job_description(example_jd))