import json
import nltk
from nltk import edit_distance
with open("tokens.json", "r", encoding ='utf-8') as f:
    clear_tokens = json.load(f)
def find_word(word,clear_tokens):
    flag = 0
    numbers = []
    for j in range(len(clear_tokens)):
        for i in range(len(clear_tokens[j])):
            if word == clear_tokens[j][i]:
                flag = 1
                numbers.append(j)
    if flag == 1:
        print(f'слово \'{word}\' есть в документах {numbers}')
    else:
        print(f'слово \'{word}\' нет в документе')
        e_d = 40 #тк в самом длинном слове в русском языке 35 букв, не имеет смысла брать сильно больше
        min_words = []
        for j in range(len(clear_tokens)):
            for i in range(len(clear_tokens[j])):
                e_d1 = edit_distance(word, clear_tokens[j][i])
                if e_d1 < e_d:
                    e_d = e_d1
                    min_word = clear_tokens[j][i]
        min_words.append(min_word)
        for j in range(len(clear_tokens)):
            for i in range(len(clear_tokens[j])):
                e_d1 = edit_distance(word, clear_tokens[j][i])
                if e_d1 == e_d:
                    min_words.append(clear_tokens[j][i])
        print(f'похожие слова с расстоянием {e_d} это {set(min_words)}')
    pass
find_word('новости', clear_tokens)
find_word('пандем', clear_tokens)