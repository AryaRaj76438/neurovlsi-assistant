from src.ingestion.discovery import DocumentDiscovery

discovery = DocumentDiscovery()

results = discovery.discover()

print(f"New Documents: {len(results['new'])}")
print(f"Modified Documents: {len(results['modified'])}")
print(f"Existing Documents: {len(results['existing'])}")

discovery.close()