#import chromadb
#import os
#from dotenv import load_dotenv
#import pandas as pd
#import uuid

#load_dotenv()

# -----------------------------
# Chroma Cloud client
# -----------------------------
#Client = chromadb.CloudClient(
    #api_key=os.getenv("CHROMA_API_KEY"),
    #tenant=os.getenv("CHROMA_TENANT"),
    #database=os.getenv("CHROMA_DATABASE")
#)

#print("Creating or Getting collection 'emotions'")
#collection = Client.get_or_create_collection(name="emotions")

#df = pd.read_csv("../emotions.csv")

#print("Inserting data into the collection")
#for i in range(14000, len(df), 300):
    #collection.add(
        #ids=[str(uuid.uuid4()) for _ in range(300)],
        #documents=df["text"].tolist()[i:i+300],
        #metadatas=[{"emotion": emotion, "line": i+j} for j, emotion in enumerate(df["label"].tolist()[i:i+300])]
    #)


#BATCH_SIZE = 300
#offset = 0

#all_ids = []
#all_docs = []

#while True:
    #batch = collection.get(
        #include=["documents"],
        #limit=BATCH_SIZE,
        #offset=offset
    #)

    #if not batch["ids"]:
        #break

    #all_ids.extend(batch["ids"])
    #all_docs.extend(batch["documents"])

    #offset += BATCH_SIZE


#seen = set()
#duplicate_ids = []

#for doc, doc_id in zip(all_docs, all_ids):
    #normalized = doc.strip().lower()

    #if normalized in seen:
        #duplicate_ids.append(doc_id)
    #else:
        #seen.add(normalized)

#DELETE_BATCH_SIZE = 300

#for i in range(0, len(duplicate_ids), DELETE_BATCH_SIZE):
    #batch_ids = duplicate_ids[i:i + DELETE_BATCH_SIZE]

    #collection.delete(ids=batch_ids)

    #print(f"🗑️ Deleted {len(batch_ids)} duplicates ({i} → {i + len(batch_ids)})")

#print("✅ All duplicates removed successfully")

