from pathlib import Path
from pypdf import PdfReader

class PDFLoader:
    def load(self, file_path):
        try:
            pdf_path = Path(file_path)
            reader = PdfReader(pdf_path)
            pages = []

            for page_num,page in enumerate(reader.pages, start=1):
                text = page.extract_text()
                if not text:
                    continue
                
                pages.append({
                    "page": page_num,
                    "text": text,
                    "source": pdf_path.name
                })

            return pages

        except Exception as e:
            print(f"Error loading PDF {file_path}: {e}")
            return None