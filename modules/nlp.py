
import spacy

# Load NLP model
nlp = spacy.load("en_core_web_sm")

# Function to process command
def process_command(command):
    doc = nlp(command)
    return doc
