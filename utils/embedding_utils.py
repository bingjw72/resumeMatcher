import openai
from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity

def get_text_embedding(text, provider="openai", model="text-embedding-3-small", local_model=None):
    """
    Compute text embedding using either OpenAI API or a local sentence-transformer model.

    Parameters:
    - text (str): Input text to embed
    - provider (str): "openai" or "local"
    - model (str): Model name for OpenAI or local
    - local_model (SentenceTransformer): Optional pre-loaded local model

    Returns:
    - List[float]: Embedding vector
    """
    if provider == "openai":
        response = openai.Embedding.create(input=text, model=model)
        return response["data"][0]["embedding"]

    elif provider == "local":
        if local_model is None:
            local_model = SentenceTransformer("all-MiniLM-L6-v2")
        return local_model.encode(text)

    else:
        raise ValueError("Invalid embedding provider. Choose 'openai' or 'local'.")

def compute_cosine_similarity(vec1, vec2):
    """
    Compute cosine similarity between two embedding vectors.

    Parameters:
    - vec1, vec2: Embedding vectors (List[float] or np.ndarray)

    Returns:
    - float: Cosine similarity score between -1 and 1
    """
    return cosine_similarity([vec1], [vec2])[0][0]

if __name__ == "__main__":
    from utils.readpdf import extract_text_from_pdf, extract_candidate_id
    import sys

    # Expecting: python embedding_utils.py path_to_resume.pdf "Job description text here"
    # if len(sys.argv) < 3:
    #     print("Usage: python embedding_utils.py <resume_path> <job_description>")
    #     sys.exit(1)

    # resume_path = sys.argv[1]
    # job_description = sys.argv[2]
    resume_path = "MLE_resume.pdf"
    job_description = """
"role_title": "Data Scientist",
  "responsibilities": [
    "Building data pipelines",
    "Creating predictive models",
    "Building dashboards"
  ],
  "required_skills": [
    "Python",
    "SQL",
    "Machine Learning"
  ],
  "preferred_skills": [
    "Experience with AWS",
    "Experience with Tableau"
  ],
  "tools": [
    "Python",
    "SQL",
    "AWS",
    "Tableau"
  ],
  "domain": "Data Science"
"""

    with open(resume_path, "rb") as f:
        resume_text = extract_text_from_pdf(f)
        candidate_id = extract_candidate_id(f, resume_text)

    jd_embedding = get_text_embedding(job_description, provider="local")
    resume_embedding = get_text_embedding(resume_text, provider="local")

    score = compute_cosine_similarity(jd_embedding, resume_embedding)

    print(f"Candidate ID: {candidate_id}")
    print(f"Similarity Score: {score:.4f}")