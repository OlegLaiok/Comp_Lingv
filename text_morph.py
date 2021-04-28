import json
import pymorphy2
with open("tokens.json", "r", encoding ='utf-8') as f:
    clear_tokens = json.load(f)
analyzer = pymorphy2.MorphAnalyzer()
normalized = []
for tokens in clear_tokens:#лемматизация токенов
    tokens = [analyzer.parse(word)[0].normal_form for word in tokens]
    normalized.append(tokens)
word_count = []
for tokens in normalized:#ранжирование по частоте
    tokens = [(word, tokens.count(word)) for word in set(tokens)]
    word_count.append(tokens)
for words in word_count:
    words.sort(key=lambda pair:pair[1], reverse=True)
print(word_count)
final_dict=[]
for i in range(len(word_count)):
    final_dict.append([])
    for j in range(len(word_count[i])):
        final_dict[i].append({'word': word_count[i][j][0], 'p_of_s': analyzer.parse(word_count[i][j][0])[0].tag.POS, 'freq': word_count[i][j][1]})
print(final_dict)
with open("final_dict.json", "w", encoding ='utf-8') as f:
    json.dump(final_dict, f, ensure_ascii=False)
f.close()

