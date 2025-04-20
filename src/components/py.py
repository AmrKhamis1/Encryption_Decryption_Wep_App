import json

# Load JSON from file
with open('Words.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

# Convert each word in the array to lowercase
data['commonWords'] = [word.lower() for word in data['commonWords']]

# Write the modified JSON to a new file
with open('lowercased_words.json', 'w', encoding='utf-8') as f:
    json.dump(data, f, indent=2, ensure_ascii=False)

print("Lowercased JSON written to 'lowercased_words.json'")
