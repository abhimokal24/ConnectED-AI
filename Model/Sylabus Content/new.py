from collections import Counter
import spacy

# Function to read terms from the .txt file
def read_terms_from_txt(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        terms = [line.strip() for line in file]
    return terms

# Function to remove stopwords and filter terms by frequency
def filter_terms(terms, stop_words, min_frequency=2, max_frequency=100):
    filtered_terms = []
    term_freq = Counter(terms)
    for term in terms:
        if term.lower() not in stop_words and min_frequency <= term_freq[term] <= max_frequency:
            filtered_terms.append(term)
    return filtered_terms

# Load English language model for spaCy
nlp = spacy.load("en_core_web_sm")

# Path to the .txt file containing extracted terms
txt_file_path = 'computer_science_terms-sem5.txt'

# Read terms from the .txt file
extracted_terms = read_terms_from_txt(txt_file_path)

# Load spaCy stopword list
stop_words = spacy.lang.en.stop_words.STOP_WORDS

# Remove stopwords and filter terms by frequency
filtered_terms = filter_terms(extracted_terms, stop_words)

# Print the filtered terms
print("Filtered terms:")
for term in filtered_terms:
    print(term)
