import json

def remove_duplicates(file_path):
    with open(file_path, 'r', encoding='utf8') as file:
        data = json.load(file)
        word_set = set()
        duplicates = 0
        clean_list = []
        
        for item in data:
            word = item['word']
            if word not in word_set:
                word_set.add(word)
                clean_list.append(word)  # append the word, not the dictionary
            else:
                duplicates += 1

        print(f"Total number of duplicates: {duplicates}")

    clean_list.sort()

    with open('cleaned_words.json', 'w', encoding='utf8') as file:
        json.dump(clean_list, file, ensure_ascii=False, indent=4)

remove_duplicates('prueba.json')