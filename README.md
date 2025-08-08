# Candidate Recommendation Engine

This is a Streamlit-based intelligent web app that recommends top candidate resumes for a given job description based on semantic similarity.

## 🔍 Features

- Accepts a **job description** as text input
- Supports uploading **multiple candidate resumes** in PDF format
- Allows choosing between **OpenAI** and **local sentence-transformer** models for embedding
- Computes **cosine similarity** between the JD and each resume
- Displays only candidates with a similarity score > 0.2, showing the **Top 10 matches**
- ✅ When using the **OpenAI embedding model**, the app automatically generates a detailed GPT-based **summary** explaining:
  - The candidate’s experience and strengths
  - Any potential weaknesses
  - A final evaluation of fit, based on similarity score and resume content

## 🛠️ Tech Stack

- **Frontend**: Streamlit
- **Embedding**:
  - Local: SentenceTransformers (`all-MiniLM-L6-v2`)
  - OpenAI: `text-embedding-3-small`
- **Resume Parsing**: PyPDF2
- **Summarization**: GPT-4 via OpenAI ChatCompletion API

## 🗂️ File Structure

```text
├── app_main_complete.py      # Main app with summarization support
├── readpdf.py                # Resume text + ID extractor
├── embedding_utils.py        # Embedding + cosine similarity functions
├── structure_jd.py           # JD structuring (optional)
├── requirements.txt          # Dependencies
└── README.md                 # Project documentation
```

## 🚀 How to Run

1. Clone this repository and install dependencies:

```bash
conda create -n recommender python=3.10
conda activate recommender
pip install -r requirements.txt
```

2. Set your OpenAI API key (if using OpenAI models):

```bash
export OPENAI_API_KEY=your-key-here
```

3. Start the app:

```bash
streamlit run app_main_complete.py
```

## ⚙️ Notes

- **GPT-based summaries** are only generated when the "OpenAI" model is selected.
- Local embedding mode will compute similarity but skip summarization.
- Only resumes with **similarity ≥ 0.2** are considered.

## 📌 To Do

- Add `.docx` resume support
- Allow downloading of match results
- Enable custom similarity threshold from UI

## 📄 License
MIT License

## 🙋‍♂️ Contact
For questions or suggestions, feel free to open an issue or contact \[[bwang72@ur.rochester.edu](email)].


<!-- # Candidate Recommendation Engine

This is a Streamlit-based web application for matching candidate resumes against a job description using semantic similarity via text embeddings.

## 🔍 Features

* Accepts a **Job Description** (JD) as text input.
* Supports **multiple resume uploads** in PDF format.
* Allows the user to select between **local sentence-transformer embeddings** and **OpenAI embeddings**.
* Computes **cosine similarity** between the JD and each resume.
* Displays the **Top 10 candidates** with similarity **greater than 0.2**, sorted by relevance.

## 🛠️ Tech Stack

* **Frontend**: [Streamlit](https://streamlit.io/)
* **Embedding**:

  * Local: [`sentence-transformers`](https://www.sbert.net/) (`all-MiniLM-L6-v2`)
  * Cloud: [`OpenAI` Embedding API](https://platform.openai.com/docs/guides/embeddings)
* **Similarity Computation**: Cosine Similarity using `scikit-learn`
* **Resume Parsing**: `PyPDF2`

## 🗂️ File Structure

```text
├── app_main.py                # Main Streamlit interface
├── readpdf.py                 # Resume parsing and text extraction logic
├── embedding_utils.py         # Embedding + similarity functions
├── structure_jd.py            # (Optional) Structured JD parsing with OpenAI
├── requirements.txt           # Python dependencies (optional)
└── README.md                  # Project overview
```

## 🚀 Getting Started

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/candidate-recommender.git
cd candidate-recommender
```

### 2. Set up the Environment

It is recommended to use a virtual environment or conda environment.

```bash
conda create -n recommender python=3.10
conda activate recommender
pip install -r requirements.txt
```

If you are using OpenAI, also set your API key:

```bash
export OPENAI_API_KEY=your-api-key
```

### 3. Run the App

```bash
streamlit run app_main.py
```

## 🧪 Testing Locally

You can run the embedding test directly:

```bash
python embedding_utils.py path/to/resume.pdf "Your JD text here"
```

## 📝 Notes

* Only resumes with similarity score > 0.2 are considered.
* Maximum of 10 candidates will be shown.
* Support for `.docx` and GPT-based summary is planned.

## 📄 License

MIT License

## 🙋‍♂️ Contact

For questions or suggestions, feel free to open an issue or contact \[[bwang72@ur.rochester.edu](email)]. -->
