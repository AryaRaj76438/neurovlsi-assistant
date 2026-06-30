
import json

with open(
    "data/chunks/test_chunks.jsonl",
    "r",
    encoding="utf-8"
) as f:
    count = 0
    for line in f:
        if "current mirror" in line.lower():
            count += 1
            print(line[:500])

print()
print("Matches:", count)