import requests
import time
import json

def insert_code(domain1, offset1, count1): #Фукция для удобной подстановки данных для запроса
        return """return API.wall.get ({
        "owner_id": "",
        "domain": "%s",
        "offset": %d,
        "count": %d,
        "filter": "owner",
        "extended": 0,
        "fields": "text",
        "v": "5.103"
    });""" % (domain1, offset1, count1)

def get_wall(domain,offset,count): #Сама функция получения данных со стены
    wall_posts=[]
    for i in range(1000):
        wall_posts.append(0)
    point=offset
    l=0 # счетчик для количества слов
    for offset in range(0,count,100): # используем цикл со смещением offset, чтобы обойти ограничение в 100 записей за раз
        response = requests.post( # Использую POST запрос, т.к. работал с ним раньше, плюс удобно передавать в нем данные запроса при работе с API
            url="https://api.vk.com/method/execute",
                data={
                    "code": insert_code(domain, offset, count),
                    "access_token": "69b24631b424eef4082d34d22b2811e8b55e3705ee93df5b0462630d42fc3299f12e834498a0e95b69056",
                    "v": "5.103"
                }
        )
        j=0
        for i in range(offset, offset+point):
            wall_posts[i]=response.json()['response']['items'][j]
            wall_posts[i]=wall_posts[i].get('text')
            s = wall_posts[i].split()
            l = len(s) + l
            j=j+1
        time.sleep(0.5)
    print('Average number of words in a post = ', round(l/count))
    print('Total number of words = ', l)
    return wall_posts

with open("VK_data_lentach.json", "w", encoding='utf-8') as f:
    json.dump(get_wall("lentach",100,1000), f, ensure_ascii=False)