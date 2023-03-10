from bs4 import BeautifulSoup 
import requests
import csv

count = 0

def get_html(url: str) -> str:
    '''Получает html код определенного сайта'''
    response = requests.get(url)
    return response.text

def get_las_page(html: str) -> int:
    soup = BeautifulSoup(html, 'html.parser')
    pages = soup.find('ul', class_ = 'pagination').find_all('a',class_='page-link')
    last_page = pages[-1].get('data-page')
    return int(last_page)

def get_data(html:str) -> list:
    '''Функция парсер, получает все данные с сайта'''
    soup = BeautifulSoup(html, 'html.parser')
    catalog = soup.find('div', class_ = 'table-view-list')
    cars = catalog.find_all('div', class_ = 'list-item')
    result = []
    for car in cars:
            
        name = car.find('h2', class_ = 'name').text.strip()
        try:
            img = car.find('img', class_ = 'lazy-image').get('data-src')
        except:
            img = 'нет такого файла'
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
        fieldnames = ['№','Name', 'Price', 'Description', 'Image']
        writer = csv.DictWriter(file, fieldnames)
        global count
    
       
        for car in data:
            count += 1
            writer.writerow ({
                '№': count,
                'Name': car['name'],
                'Price': car['price'],
                'Description': car['description'],
                'Image':car['img']
            })

def prepare_cvs() -> None:
    '''функция которая подотавливает cvs файл'''
    with open('cars.cvs', 'w') as file:
        fieldnames = ['№','Name', 'Price', 'Description', 'Image']
        writer = csv.DictWriter(file, fieldnames)
        writer.writerow({
                '№': '№',
                'Name': 'Name',
                'Price': 'Price',
                'Description': 'Description',
                'Image':'Image'
            })


def main():
    i = 1
    while True:
        urls = f'https://www.mashina.kg/search/all/?page={i}'
  

        html = get_html(urls)
        last_page = get_las_page(html)
        data = get_data(html)
        write_to_csv(data)
        print(f'спарсили {i}/{last_page} страницу')
        if i == last_page:
            break
        i += 1


main()