import hashlib

def generate_chunk_id(document_path, page_number, text):
    context = (
        f"{document_path}|"
        f"{page_number}|"
        f"{text}"
    )
    return hashlib.sha256(
        context.encode("utf-8")
    ).hexdigest()