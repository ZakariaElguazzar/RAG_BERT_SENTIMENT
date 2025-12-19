import numpy as np
class SentimentRAGCrossEncoder:

    def __init__(self, retriever, cross_encoder, classifier):
        self.retriever = retriever
        self.cross_encoder = cross_encoder
        self.classifier = classifier

    def predict(self, query):
        docs, metadatas = self.retriever.retrieve(query)
        scores = self.cross_encoder.score(query, docs)

        print("Retrieved docs:")
        for d in docs:
            print("-", d)
        print("Scores:", scores)

        enriched_text = "Classify the sentiment of the 'Target Text' using the following examples as reference:\n\n"
        for i, doc in enumerate(docs):
            # Idéalement, récupérez aussi le label du document dans ChromaDB
            enriched_text += f"Example: {doc} : {metadatas[i]['emotion']} \n"

        enriched_text += f"\nTarget Text: {query}\nSentiment:"

        # Trouver l'index du score maximum
        max_score = max(scores)
        j = scores.index(max_score)

        return self.classifier.predict(enriched_text),metadatas[j]['emotion']
