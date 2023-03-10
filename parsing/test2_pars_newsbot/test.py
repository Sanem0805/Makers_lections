# url = 'https://www.securitylab.ru/news/536184.php'
# article_id = url.split('/')[-1]
# article_id = article_id[:-4]
# print(article_id)
import json

with open('new_dict.json') as file: 
    news_dict = json.load(file)

search_id = '5361851234'

if search_id in news_dict:
    print('новость уже есть в словаре, пропускаем итерацию')
else:
    print('Свежая новость, добавляем в словарь')