import PyPDF2
import re
import os

def extract_text_from_pdf(file_obj):
    """
    Extract all text from a PDF file.
    """
    reader = PyPDF2.PdfReader(file_obj)
    text = ""
    for page in reader.pages:
        page_text = page.extract_text()
        if page_text:
            text += page_text + "\n"
    return text

def extract_candidate_id(file_obj, extracted_text):
    """
    Extract candidate name or ID from file name or first lines of content.
    """
    lines = extracted_text.splitlines()
    for line in lines[:5]:
        line = line.strip()
        # Common ID or name patterns: uppercase name, or lines in big font etc.
        match = re.match(r"^[A-Z][A-Za-z\s\-\.]{3,50}$", line)
        if match:
            return line
    return "Unknown Candidate"

def extract_sections(text):
    """
    Extract sections such as skills and experience from resume text.
    """
    sections = {}
    current_section = None
    lines = text.splitlines()

    for line in lines:
        line_strip = line.strip()

        if re.match(r"(Skills|Technical Skills|Work Experience|Projects|Education)", line_strip, re.IGNORECASE):
            current_section = line_strip.lower()
            sections[current_section] = []
        elif current_section and line_strip:
            sections[current_section].append(line_strip)

    return sections

# Example usage (if run independently)
if __name__ == "__main__":
    with open("MLE_resume.pdf", "rb") as f:
        text = extract_text_from_pdf(f)
        candidate_id = extract_candidate_id(f, text)
        sections = extract_sections(text)

    print("Candidate ID:", candidate_id)
    print("Sections:")
    for section, content in sections.items():
        print(f"\n[{section.upper()}]")
        for item in content:
            print("-", item)