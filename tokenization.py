import json
import string
import nltk
from nltk import word_tokenize
from nltk.corpus import stopwords
with open("VK_data_lentach_cleared.json", "r", encoding ='utf-8') as f:
    text_data = json.load(f)
raw_tokens = []
for text in text_data:
    raw_tokens.append(word_tokenize(text))
punct = string.punctuation + "—" + "«" + "»"
clear_tokens = []
for tokens in raw_tokens:
    tokens = [token.lower() for token in tokens if token not in punct]
    clear_tokens.append(tokens)
stopwords_list = stopwords.words("russian")
stopwords_list.append(stopwords.words('english'))
cleared_tokens = []
for tokens in clear_tokens:
    tokens = [word for word in tokens if word not in stopwords_list]
    cleared_tokens.append(tokens)

with open("tokens.json", "w", encoding='utf-8') as f:
    json.dump(cleared_tokens, f, ensure_ascii=False)
f.close()