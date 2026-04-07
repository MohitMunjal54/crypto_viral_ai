from keybert import KeyBERT
from sklearn.feature_extraction.text import CountVectorizer

class Analyzer:

    def __init__(self):
        self.kw_model = KeyBERT()

    def extract_keywords(self, texts):
        joined = " ".join(texts)
        keywords = self.kw_model.extract_keywords(joined, top_n=10)
        return [kw[0] for kw in keywords]

    def find_patterns(self, data):
        all_texts = []

        for section in data.values():
            for item in section:
                if "title" in item:
                    all_texts.append(item["title"])
                if "content" in item:
                    all_texts.append(item["content"])

        return {
            "keywords": self.extract_keywords(all_texts),
            "raw_texts": all_texts
        }
