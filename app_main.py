import streamlit as st
import tempfile
from utils.readpdf import extract_text_from_pdf, extract_candidate_id
from utils.embedding_utils import get_text_embedding, compute_cosine_similarity
from utils.gpt_summary import generate_candidate_summary


st.set_page_config(page_title="Candidate Recommender", layout="centered")
st.title("Candidate Recommendation Engine")

# --- Step 1: Input JD ---
st.subheader("Step 1: Paste Job Description")
jd_input = st.text_area("Job Description", height=200)

# --- Step 2: Upload Resumes ---
st.subheader("Step 2: Upload Candidate Resumes (PDF only)")
resume_files = st.file_uploader("Upload one or more PDF resumes", type=["pdf"], accept_multiple_files=True)

# --- Step 3: Select Embedding Model ---
st.subheader("Step 3: Choose Embedding Model")
embedding_choice = st.radio("Which embedding model do you want to use?", ["OpenAI", "Local(Not recommended)"])

# --- Step 4: Run Matching ---
if st.button("Run Matching"):
    if not jd_input or not resume_files:
        st.warning("Please provide both a job description and at least one resume.")
    else:
        with st.spinner("Processing..."):
            results = []
            if embedding_choice == "OpenAI":
                modelchoice = "openai"
            else:
                modelchoice = "local"
            jd_embedding = get_text_embedding(jd_input, provider=modelchoice)

            for file in resume_files:
                file.seek(0)
                text = extract_text_from_pdf(file)
                candidate_id = extract_candidate_id(file, text)
                resume_embedding = get_text_embedding(text, provider=modelchoice)
                similarity = compute_cosine_similarity(jd_embedding, resume_embedding)

                if similarity >= 0.2:
                    summary = ""
                    if modelchoice == "openai":
                        try:
                            summary = generate_candidate_summary(text, jd_input, similarity)
                        except Exception as e:
                            summary = f"Error generating summary: {str(e)}"
                    results.append({
                        "name": candidate_id,
                        "score": round(similarity, 4),
                        "summary": summary
                    })

            # Sort and filter top 10
            sorted_results = sorted(results, key=lambda x: x["score"], reverse=True)[:10]

        # --- Step 5: Display ---
        st.subheader("Top Matches (Score > 0.2)")
        if not sorted_results:
            st.info("No candidates matched with a similarity score above 0.2.")
        else:
            for i, r in enumerate(sorted_results):
                st.markdown(f"**{i+1}. {r['name']}** — Similarity: `{r['score']}`")
                # if r.get("summary"):
                #     st.markdown(f"Candidate Summary: {r['summary']}")
                st.markdown("---")

