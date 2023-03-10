from bs4 import BeautifulSoup as bs
import requests
import csv

count = 0

def get_html(url: str) -> str:
    '''Получает html код определенного сайта'''
    response = requests.get(url)
    return response.text

def get_last_page(html: str) -> int:
    soup = bs(html, 'html.parser')
    pages = soup.find('ul', class_='pagination').find_all('a', class_='page-link')
    last_page = pages[-1].get('data-page')
    return int(last_page)

def get_data(html:str) -> list:
    '''Функция парсер, получает все данные с сайта'''
    soup = bs(html, 'html.parser')
    catalog = soup.find('div', class_ = 'table-view-list')
    cars = catalog.find_all('div', class_ = 'list-item')
    result = []
    for car in cars:
        
        name = car.find('h2', class_ = 'name').text.strip()
        try:
            img = car.find('img', class_ = 'lazy-image').get('data-src')
        except:
            img = 'No picher'
        price = car.find('p').find('strong').text
        desc1 = car.find('p', class_ = 'year-miles').text.strip()
        desc2 = car.find('p', class_ = 'body-type').text.strip()
        desc3 = car.find('p', class_ = 'volume').text.strip()
        description = f'{desc1} {desc2} {desc3}'

        data = {
            'name': name,
            'price': price,
            'description': description,
            'img': img
        }

        result.append(data)

    return result

def write_to_csv(data:dict) -> None:
    '''Функция для записи всех данных в CSV файл'''
    with open('cars.csv', 'a') as file:
        fieldnames = ['#', 'Name']
        writer = csv.DictWriter(file, fieldnames)
        global count
      
       
        for car in data:
            count += 1
            writer.writerow ({
                '#': count,
                'Name': car['name'],
                'Price': car['price'],
                'Description': car['description'],
                'Image':car['img']
            })

def prepare_csv() -> None:
    '''Функция которая подготовит csv файл'''
    with open ('cars.csv', 'w') as file:
        fieldnames = ['#', 'Name']
        writer = csv.DictWriter(file, fieldnames)
        writer.writerow({
            '#': '#',
            'Name': 'Name'
            })

def main():
    i = 1
    prepare_csv()
    while True:
        url = 'https://vesti.kg/'
        html = get_html(url)
        data = get_data(html)
        write_to_csv(data)
        print(f'Спарсили {i}/{last_page} страницу!')
        if i == 15:
            break
        i += 1