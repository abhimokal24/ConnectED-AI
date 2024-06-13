import PyPDF2
import spacy

# Function to extract text from PDF file
def extract_text_from_pdf(pdf_path):
    text = ""
    with open(pdf_path, 'rb') as file:
        reader = PyPDF2.PdfReader(file)
        num_pages = len(reader.pages)
        for page_num in range(num_pages):
            page = reader.pages[page_num]
            text += page.extract_text()
    return text

# Load English language model for spaCy
nlp = spacy.load("en_core_web_sm")

# Function to extract technical terms related to computer science
def extract_technical_terms(text):
    doc = nlp(text)
    technical_terms = set()
    for token in doc:
        # Check if the token is a noun and has a specific tag indicating technical terms
        if token.pos_ == "NOUN" and ("NN" in token.tag_ or "JJ" in token.tag_):
            technical_terms.add(token.text)
    return technical_terms

# Path to the PDF syllabus file
pdf_path = 'sem6 syllabus.pdf'

# Extract text from PDF
syllabus_text = extract_text_from_pdf(pdf_path)

# Extract technical terms related to computer science
computer_science_terms = extract_technical_terms(syllabus_text)

# Write the extracted terms to a .txt file
output_file_path = 'computer_science_terms.txt'
with open(output_file_path, 'w', encoding='utf-8') as output_file:
    output_file.write("Technical terms related to computer science:\n")
    for term in computer_science_terms:
        output_file.write(term + '\n')

print("Extracted terms saved to:", output_file_path)
