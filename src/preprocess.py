import pandas as pd
import nltk
import re
import spacy

# Download NLTK stopwords and punkt (first time only)
nltk.download("punkt")
nltk.download("stopwords")

from nltk.corpus import stopwords
from nltk.tokenize import sent_tokenize, word_tokenize

# Load dataset
df = pd.read_csv("../data/crawled_data.csv")

# English stopwords
stop_words = set(stopwords.words("english"))

processed_sentences = []

for text in df["text"].dropna():
    # Step 1: Sentence Tokenization
    sentences = sent_tokenize(text)

    for sentence in sentences:
        # Step 2: Lowercase
        sentence = sentence.lower()

        # Step 3: Remove special characters/numbers
        sentence = re.sub(r"[^a-zA-Z\s]", "", sentence)

        # Step 4: Tokenize words
        words = word_tokenize(sentence)

        # Step 5: Remove stopwords
        words = [w for w in words if w not in stop_words]

        # Step 6: Rejoin words into cleaned sentence
        cleaned_sentence = " ".join(words)

        if len(cleaned_sentence.split()) > 5:  # keep meaningful sentences
            processed_sentences.append(cleaned_sentence)

# Save to new CSV
processed_df = pd.DataFrame(processed_sentences, columns=["cleaned_text"])
processed_df.to_csv("../data/processed_data.csv", index=False, encoding="utf-8")

print(f"✅ Preprocessing complete! {len(processed_df)} cleaned sentences saved to data/processed_data.csv")
