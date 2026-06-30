from src.ingestion.pdf_loader import PDFLoader

loader = PDFLoader()
pdf_path = "/Users/arya/Desktop/Machine Learning/neurovlsi/data/raw/books/Design-of-Analog-CMOS-Integrated-Circuits.pdf"

pages = loader.load(pdf_path)
print("Pages:", len(pages))
print()
print(pages[0]["text"][:1000])