from src.ingestion.register_documents import DocumentRegistrar

registrar = DocumentRegistrar()

summary = registrar.run()

print("\nRegistration Summary")
print("-" * 50)
print(f"New Documents      : {summary['new']}")
print(f"Modified Documents : {summary['modified']}")
print(f"Existing Documents : {summary['existing']}")

registrar.close()