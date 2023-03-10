from bs4 import BeautifulSoup as bs
import requests
import csv

count = 0

def get_html(url: str) -> str:
    response = requests.get(url)
    return response.text

def get_last_page(html: str) -> int:
    soup = bs(html, 'lxml')
    pages = soup.find('div', class_='pages fl').find_all('a', class_='pages-item')
    last_page = pages[-1].get('data-ci-pagination-page')
    return int(last_page)

def get_data(html:str) -> list:
    soup = bs(html, 'lxml')
    catalog = soup.find('div', class_ = 'catalog-list')
    cars = catalog.find_all(class_="catalog-list-item")
    result = []
    for car in cars:
        
        name = car.find('span', class_='catalog-item-caption').text.strip()
        try:
            img = car.find('img', class_='catalog-item-cover-img').get('src')
        except:
            img = 'No picher'
        price = car.find('span', class_='catalog-item-price').text.strip()
        desc1 = car.find('span',class_='caption-year').text.strip()
        desc2 = car.find('span',class_='catalog-item-descr').text.strip()
        desc3 = car.find('span',class_='catalog-item-mileage').text.strip()
        description = f'{desc1}${desc3}${desc2}'

        data = {
            'name': name,
            'price': price,
            'description': description,
            'img': img
        }

        result.append(data)

    return result

def write_csv(data:dict) -> None:
    with open('cars.csv', 'a') as file:
        fieldnames = ['#', 'Name', 'Price', 'Description', 'Image']
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

def new_csv() -> None:
    with open ('cars.csv', 'a') as file:
        fieldnames = ['#', 'Name', 'Price', 'Description', 'Image']
        writer = csv.DictWriter(file, fieldnames)
        writer.writerow({
            '#': '#',
            'Name': 'Name',
            'Price': 'Price',
            'Description': 'Description',
            'Image':'Image'
            })

def main():
    i = 1
    new_csv()
    while True:
        url = f'https://cars.kg/offers/{i}'
        html = get_html(url)
        last_page = get_last_page(html)
        data = get_data(html)
        write_csv(data)
        print(f'Спарсили {i}/{last_page} страницу!')
        if i == 94:
            break
        i += 1

main()