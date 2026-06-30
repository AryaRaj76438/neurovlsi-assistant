class Deduplicator:
    def __init__(self, max_chunks_per_document=5):
        self.max_chunks_per_document = max_chunks_per_document

    def deduplicate(self, chunks):
        document_counts = {}
        seen_pages = set()
        filtered = []

        for chunk in chunks:
            page_key = (
                chunk.document_path,
                chunk.page
            )
            if page_key in seen_pages:
                continue

            path = chunk.document_path
            count = document_counts.get(path, 0)

            if count>=self.max_chunks_per_document:
                continue
            
            filtered.append(chunk)
            seen_pages.add(page_key)
            document_counts[path] = count+1
        
        return filtered
        