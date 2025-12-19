class ChromaRetriever:
    def __init__(self, collection, k=5):
        self.collection = collection
        self.k = k

    def retrieve(self, query):
        results = self.collection.query(
            query_texts=[query],
            n_results=self.k,
            include=["documents", "metadatas"]
        )

        print("Retrieved documents and metadata:")
        for i, (doc, meta) in enumerate(zip(results["documents"][0], results["metadatas"][0])):
            print(f"  {i+1}. Document: {doc}, Metadata: {meta['emotion']}")
        return results["documents"][0], results["metadatas"][0]