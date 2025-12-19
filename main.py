from ChromaRetriever import ChromaRetriever
from BertCrossEncoder import BertCrossEncoder
from BertSentimentClassifier import BertSentimentClassifier
from SentimentRAGCrossEncoder import SentimentRAGCrossEncoder
import chromadb
import os
from dotenv import load_dotenv
from LABEL_MAP import LABEL_MAP

load_dotenv()

# -----------------------------
# Chroma Cloud client
# -----------------------------
Client = chromadb.CloudClient(
    api_key=os.getenv("CHROMA_API_KEY"),
    tenant=os.getenv("CHROMA_TENANT"),
    database=os.getenv("CHROMA_DATABASE")
)

print("Creating or Getting collection 'emotions'")
collection = Client.get_or_create_collection(name="emotions")

retriever = ChromaRetriever(collection,k=2)
cross_encoder = BertCrossEncoder()
classifier = BertSentimentClassifier()

rag = SentimentRAGCrossEncoder(
    retriever,
    cross_encoder,
    classifier
)

queries = [
    "I am feeling great today!",
    "I am so scared right now.",
    "This is the best day of my life!",
    "I am really disappointed with the service.",
    "I am feeling very anxious.",
    "I am so surprised by the news.",
    "I love this song!",
    "This is a terrible movie.",
    "I am so excited about the concert!",
    "I feel very sad about the news.",
    "I feel very angry.",
    "I am so happy today!",
    "This is a sad story.",
    "I am excited about the future.",
    "I am feeling anxious about the exam.",
    "I love spending time with my family.",
    "I am so surprised by the gift.",
    "i feel shocked to realize that whatever were talking about were both seeing understanding in the same way",
    "i am very happy with the results of my exam",
    "i am extremely sad about the loss of my pet",
    "i am furious about the way i was treated",
    "i am scared to walk alone at night",
    "i love the way you make me feel",
]



for q in queries:
    pred = rag.predict(q)
    print(f"Text: {q}")
    print(f"Emotion: {LABEL_MAP[pred]}\n")
