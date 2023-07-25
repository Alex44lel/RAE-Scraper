import json

with open("./words_with_definitions.json",encoding="utf-8") as f:
    data_definitions = json.load(f)
with open("./cleaned_words.json",encoding="utf-8") as f:
    data_words = json.load(f)

# Ensure words are consistently formatted (lower case, no leading/trailing white spaces)
data_words = [word.strip().lower() for word in data_words]

data_definitions=[word["word_name"] for word in data_definitions]

print(len(data_definitions),len(data_words))

missing = []

for word in data_words:
    if word not in data_definitions:

        missing.append(word)

print(missing)

with open("missing.json","w",encoding="utf-8") as f:
    json.dump(missing,f)