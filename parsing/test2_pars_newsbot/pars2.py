from bs4 import BeautifulSoup as bs
import requests
import lxml
from datetime import datetime
import time
import json

def get_firts_news():
    headers = {
        "user-agent": "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.183 Mobile Safari/537.36"
    }
   
    url = 'https://www.securitylab.ru/news/'
    r = requests.get(url=url, headers=headers)

    soup = bs(r.text, 'lxml')
    articles_cards = soup.find_all('a', class_='article-card')

    news_dict = {}
    for item in articles_cards:
        article_title = item.find('h2', class_='article-card-title').text.strip()
        article_desc = item.find('p').text.strip()
        article_url = f'https://www.securitylab.ru{item.get("href")}'

        article_date_time = item.find('time').get('datetime')
        date_from_iso = datetime.fromisoformat(article_date_time)
        date_time = datetime.strftime(date_from_iso, '%Y-%m-%d %H:%M:%S')
        article_date_timestamp = time.mktime(datetime.strptime(date_time,'%Y-%m-%d %H:%M:%S').timetuple())

        article_id = article_url.split('/')[-1]
        article_id = article_id[:-4]

        # print(f'{article_title} | {article_url} | {article_date_timestamp}')

        news_dict[article_id] = {
            'article_date_timestamp': article_date_timestamp,
            'article_title': article_title,
            'article_url': article_url,
            'article_desc': article_desc
        }

    with open('new_dict.json', 'w') as file:
        json.dump(news_dict, file, indent=4, ensure_ascii=False)


def check_news_update():
    with open('new_dict.json') as file:
        news_dict = json.load(file)
    
    headers = {
        "user-agent": "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.183 Mobile Safari/537.36"
    }
   
    url = 'https://www.securitylab.ru/news/'
    r = requests.get(url=url, headers=headers)

    soup = bs(r.text, 'lxml')
    articles_cards = soup.find_all('a', class_='article-card')

    fresh_news = {}
    for item in articles_cards:
        article_url = f'https://www.securitylab.ru{item.get("href")}'
        article_id = article_url.split('/')[-1]
        article_id = article_id[:-4]

        if article_id in news_dict:
            continue
        else:
            article_title = item.find('h2', class_='article-card-title').text.strip()
            article_desc = item.find('p').text.strip()

            article_date_time = item.find('time').get('datetime')
            date_from_iso = datetime.fromisoformat(article_date_time)
            date_time = datetime.strftime(date_from_iso, '%Y-%m-%d %H:%M:%S')
            article_date_timestamp = time.mktime(datetime.strptime(date_time,'%Y-%m-%d %H:%M:%S').timetuple())

            news_dict[article_id] = {
                'article_date_timestamp': article_date_timestamp,
                'article_title': article_title,
                'article_url': article_url,
                'article_desc': article_desc
            }
            fresh_news[article_id] = {
                'article_date_timestamp': article_date_timestamp,
                'article_title': article_title,
                'article_url': article_url,
                'article_desc': article_desc
            }

    with open('new_dict.json', 'w') as file:
        json.dump(news_dict, file, indent=4, ensure_ascii=False)

    return fresh_news

def main():
    # get_firts_news()
    print(check_news_update())

if __name__ == '__main__':
    main()

