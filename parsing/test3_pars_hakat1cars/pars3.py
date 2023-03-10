from bs4 import BeautifulSoup as bs
import requests
import lxml
import csv
# ТЕХНИЧЕСКОЕ ЗАДАНИЕ(сложность: средняя)
# ● Спарсить cars.kg, категорию:
# 1.Название всех моделей.
# 2.Цену всех моделей
# 3.Изображение всех моделей
# 4.Краткое описание всех моделей
# 5.Записать все в csv файл
count = 0
url = 'https://cars.kg/offers'
headers = {
    'accept': '*/*',
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36'
}
# req = requests.get(url,headers=headers)
# src = req.text
# # print(src)
# with open('index.html', 'w') as file:
#     file.write(src)

with open('index.html') as file:
    src = file.read()

def get_last_page(src: str) -> str:
    soup = bs(src, 'lxml')
    pages = soup.find('div', class_='pages fl').find_all('a', class_='pages-item')
    last_page = pages[-1].get('data-ci-pagination-page')
    return int(last_page)

def get_cars(src:str) -> list:
    soup =bs(src, 'lxml')
    all_cars = soup.find_all(class_="catalog-list-item")
    result = []
    for item in all_cars:
        # item_text = item.text
        name = item.find('span', class_='catalog-item-caption').text.split()
        url_car = 'https://cars.kg'+ item.get('href')
        price = item.find('span', class_='catalog-item-price').text
        veiw = item.find('span',class_='catalog-item-views').text
        year = item.find('span',class_='caption-year').text
        miles = item.find('span',class_='catalog-item-mileage').text.strip()
        try:
            image = item.find('img', class_='catalog-item-cover-img').get('src')
            info = item.find('span',class_='catalog-item-info').text.strip()
        except:
            image = 'No picture'
            info = 'No info'
        description = f'{year}{miles}{veiw}{info}'
        # print(f"{item_href},{item_name},{item_text},{item_price},{item_veiw},{item_info},{item_year},{item_id}")
        cars_dict = {
            'name': name,
            'image': image,
            'description': description,
            'url': url_car,
            'price': price,
        }
        result.append(cars_dict)
    write_csv(cars_dict)

    return result

def write_csv(cars_dict: dict) -> None:
    with open('cars2.csv', 'a') as file:
        title_name = ['*', 'Name', 'Image', 'Description','Url', 'Price']
        writer = csv.DictWriter(file, title_name)
        global count
        
        for item in cars_dict:
            count += 1
            writer.writerow({
                '*':count,
                'Name': item['name'],
                'Image': item['price'],
                'Description': item['description'],
                'Url': item['url'],
                'Price': item['image']
            })
def new_csv() -> None:
    with open('cars2.csv' 'a') as file:
        title_name = ['*', 'Name', 'Image', 'Description','Url', 'Price']
        writer = csv.DictWriter(file, title_name)
        writer.writerow({
            '*':'*',
            'Name': 'name',
            'Image': 'Price',
            'Description': 'Description',
            'Url': 'Url',
            'Price': 'Image'
        })

def main():
    i = 1
    while True:
        url = f'https://cars.kg/offers/{i}'
        last_page = get_last_page(src)
        cars_dict = get_cars(src)
        write_csv(cars_dict)
        print(f'Спарсили {i}/{last_page} строаницу!')
        if i == 94:
            break
        i += 1
        
main()
        
        