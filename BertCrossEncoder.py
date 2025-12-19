import torch
from transformers import BertTokenizer, BertForSequenceClassification

class BertCrossEncoder:
    def __init__(self, model_name="bert-base-uncased", num_labels=1):
        self.tokenizer = BertTokenizer.from_pretrained(model_name)
        # Utilisez un modèle entraîné pour la similarité (Cross-Encoder)
        self.model = BertForSequenceClassification.from_pretrained("cross-encoder/ms-marco-TinyBERT-L-2-v2")
        self.model.eval()

    def score(self, query, documents):
        scores = []

        for doc in documents:
            inputs = self.tokenizer(
                query,
                doc,
                return_tensors="pt",
                truncation=True,
                padding=True
            )
            with torch.no_grad():
                output = self.model(**inputs)
                score = output.logits.squeeze().item()
            scores.append(score)

        return scores
