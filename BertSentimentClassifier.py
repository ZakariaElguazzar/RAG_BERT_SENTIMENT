import torch
from transformers import BertTokenizer, BertForSequenceClassification, BertModel
class BertSentimentClassifier:
    def __init__(self, model_name="bert-base-uncased"):
        self.tokenizer = BertTokenizer.from_pretrained(model_name)
        self.model = BertForSequenceClassification.from_pretrained("bhadresh-savani/bert-base-uncased-emotion", num_labels=6)
        self.model.eval()

    def predict(self, text):
        inputs = self.tokenizer(
            text,
            return_tensors="pt",
            truncation=True,
            padding=True
        )

        with torch.no_grad():
            outputs = self.model(**inputs)

        return torch.argmax(outputs.logits, dim=1).item()