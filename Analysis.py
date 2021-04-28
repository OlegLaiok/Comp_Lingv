import json
import numpy as np
with open("final_dict.json", "r", encoding ='utf-8') as f:
    final_dict = json.load(f)
list_of_quant = []
for i in range(len(final_dict)):# создаем список словарей каждого доккумента, где каждое слово в документе имеет поля: слово, часть речи и частота появления в доккументе
    a = {'NOUN': 0, 'ADJF': 0, 'ADJS': 0, 'COMP': 0, 'VERB': 0, 'INFN': 0, 'PRTF': 0, 'PRTS': 0, 'GRND': 0, 'NUMR': 0, 'ADVB': 0, 'NPRO': 0, 'PRED': 0, 'PREP': 0, 'CONJ': 0, 'PRCL': 0, 'INTJ': 0, 'number_of_words': 0}
    for j in range(len(final_dict[i])):
        if final_dict[i][j]['p_of_s'] != None:
            a[final_dict[i][j]['p_of_s']] = a[final_dict[i][j]['p_of_s']] + final_dict[i][j]['freq']
            a['number_of_words'] = a['number_of_words'] + final_dict[i][j]['freq']
    list_of_quant.append(a)
string = ('NOUN', 'ADJF', 'ADJS', 'COMP', 'VERB', 'INFN', 'PRTF', 'PRTS', 'GRND', 'NUMR', 'ADVB', 'NPRO', 'PRED', 'PREP', 'CONJ', 'PRCL', 'INTJ')
for docs in list_of_quant:
    for obj in string:
        docs[obj] =round(docs[obj] / docs['number_of_words'],2)
print(list_of_quant)
std_a ={'NOUN': [], 'ADJF': [], 'ADJS': [], 'COMP': [], 'VERB': [], 'INFN': [], 'PRTF': [], 'PRTS': [], 'GRND': [], 'NUMR': [], 'ADVB': [], 'NPRO': [], 'PRED': [], 'PREP': [], 'CONJ': [], 'PRCL': [], 'INTJ': [], 'number_of_words': []}
for docs in list_of_quant:
    for obj in string:
        std_a[obj].append(docs[obj])
medium_a = dict(std_a)
for obj in string:
        medium_a[obj] = round(np.average(std_a[obj]), 2)
print("средние значение", medium_a)
for obj in string:
    std_a[obj] = round(np.std(std_a[obj]), 2)
print('стандартные отклонение', std_a)
for i in range(len(list_of_quant)):
    for j in string:
        if list_of_quant[i][j] > (medium_a[j] + std_a[j]*2):
            print(f'документ номер {i} нетипичный из-за того что {j} превышает среднеквадратичное отклонение в {round((list_of_quant[i][j] - medium_a[j])/std_a[j], 2)} раз(а)')
            print(final_dict[i])