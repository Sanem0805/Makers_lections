from asyncio import sleep
import random
from bs4 import BeautifulSoup as bs
import requests
import lxml
import json
import csv

# url =  "https://health-diet.ru/table_calorie/?utm_source=leftMenu&utm_medium=table_calorie"

headers = {
    'accept': '*/*',
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36'

}
# req = requests.get(url)
# src = req.text
# # print(src)
# with open('index.html', 'w') as file:
#     file.write(src)

# with open('index.html') as file:
#     src = file.read()

# soup = bs(src, 'lxml')
# all_products_href = soup.find_all(class_='mzr-tc-group-item-href')

# all_categories_dict = {}
# for item in all_products_href:
#     item_text = item.text
#     item_href = 'https://health-diet.ru' + item.get('href')

#     all_categories_dict[item_text] = item_href

# with open('all_categories_dict.json', 'w') as file: # создаем json file
#     json.dump(all_categories_dict, file, indent=4, ensure_ascii=False)

with open('all_categories_dict.json') as file: 
    all_categories = json.load(file)

iteration_count = int(len(all_categories)) - 1
count = 0
print(f'всего итераций: {iteration_count}')
for category_name, category_href in all_categories.items():

    
    rep = [",", " ", "-", "'"]
    for item in rep:
        if item in category_name:
            category_name = category_name.replace(item, '_')
    
    req = requests.get(url=category_href, headers=headers)
    src = req.text

    with open(f"data/{count}_{category_name}.html", 'w') as file:
        file.write(src)

    with open(f"data/{count}_{category_name}.html") as file:
        src = file.read()
    
    soup = bs(src, 'lxml')

    #проверка страницы на наличие таблицы с прдуктами
    alert_block = soup.find(class_='uk-alert-danger')
    if alert_block is not None:
        continue

    # собираем заголовки таблицы
    table_head = soup.find(class_='mzr-tc-group-table').find_all('th')
    product = table_head[0].text
    calories = table_head[1].text
    proteins = table_head[2].text
    fats = table_head[3].text
    carbohydrates = table_head[4].text

    with open(f"data/{count}_{category_name}.csv", 'w', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(
            (
                product,
                calories,
                proteins,
                fats,
                carbohydrates
            )
        )

    #собираем данные продуктов
    products_data = soup.find(class_='mzr-tc-group-table').find('tbody').find_all('tr')

    product_info = []
    for item in products_data:
        products_tds = item.find_all('td')

        title = products_tds[0].find('a').text
        calories = products_tds[1].text
        proteins = products_tds[2].text
        fats = products_tds[3].text
        carbohydrates = products_tds[4].text

        product_info.append(
            {
                'Title': title,
                'Calories': calories,
                'Proteins': proteins,
                'Fats': fats,
                'Carbohydrates': carbohydrates
            }
        )
        

    with open(f"data/{count}_{category_name}.csv", 'a', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(
            (
                title,
                calories,
                proteins,
                fats,
                carbohydrates
            )
        )
    with open(f'data/{count}_{category_name}.json', 'a', encoding='utf-8') as file:
        json.dump(product_info, file, indent=4, ensure_ascii=False)

    count = count + 1
    print(f'# Итерация {count}. {category_name} записан...')

    if iteration_count == 0:
        print('Работа закончена')
        break
    
    print(f'Осталось итераций: {iteration_count}')
    sleep(random.randrange(2, 4))