import json
import re
with open("VK_data_lentach1.json", "r", encoding ='utf-8') as f:
    text_data = json.load(f)
for i in range(0,len(text_data)):
    text_data[i]= re.sub(r'\n', ' ', text_data[i]) #удаляем символы новой строки
    text_data[i]= re.sub(r'\bhttp.+\b', ' ', text_data[i]) #удаляем ссылки
    text_data[i] = re.sub(r'vk.cc\S+',' ',text_data[i]) #удаляем ссылки вк
    text_data[i]= re.sub(r'l\.tinkoff\.ru/autolentach', ' ', text_data[i]) #удаляем спецсимволы и теги
    text_data[i]= re.sub(r'✹', ' ', text_data[i])
    text_data[i]= re.sub(r'⚡', ' ', text_data[i])
    text_data[i]= re.sub(r'•', ' ', text_data[i])
    text_data[i]= re.sub(r'\\xa0', ' ', text_data[i])
    text_data[i] = re.sub(r'\[.*\]',' ',text_data[i]) #удаляем ссылки на группы
    text_data[i] = re.sub(r'¯.+¯',' ',text_data[i]) #удаляем специальные эмодзи
    text_data[i] = re.sub(r'#Баян_из_предложки',' ',text_data[i]) #удаляем первоапрельский тэг
    text_data[i] = re.sub(r'\s{2,}'," ",text_data[i]) #удаляем образовавшиеся повторы пробелов
i=0
while i < len(text_data):#удаляем пустые элементы
    if text_data[i] == "" or text_data[i] == " ":
            del text_data[i]
    else:
        i=i+1
with open("VK_data_lentach_cleared.json", "w", encoding='utf-8') as f:
    json.dump(text_data, f, ensure_ascii=False)
f.close()