from bs4 import BeautifulSoup as bs
import requests
import lxml


URL = 'https://www.kivano.kg/'

def get_html(url):
    response = requests.get(url)
    return response.text# html

def get_data(html, URL): # resultat verhnei funchii  -html eto
    soup = bs(html, 'lxml') #'html'.parser -odno i toje
    blog_products = soup.find('div', class_ = 'product_vitrina')
    products = blog_products.find_all('div', class_ = 'product_box')
    list_ = []
    for product in products:
        title = product.find('div', class_ = 'product_title').text
        price = product.find('div', class_ = 'product_price').text.replace('\n', '')
        img_div = product.find('div', class_ = 'product_img')
        img = img_div.find('img').get('src')

        list_.append({'title': title, 'price': price, 'image':f"{URL}+{img.replace('/', '', 1)}"})
    return list_ #list_[-1]

html = get_html(URL)
print(get_data(html, URL))

#№ 3
# from bs4 import BeautifulSoup
# import requests
# import csv 
# source = requests.get('https://www.wikipedia.org/').text
# my_page = BeautifulSoup(source, 'lxml')
# blog_lang = my_page.find('div', class_ = 'central-featured-lang lang4')
# print(blog_lang.text)

# from bs4 import BeautifulSoup
# import requests
# import csv 

# with open('index2.html') as file:
#     src = file.read()
    
# soup = BeautifulSoup(src, 'lxml')
# title = soup.title
# print(title)
# page_h1 = soup.find('h1')
# print(page_h1)
# all_pages_h1 = soup.find_all('h1')
# print(all_pages_h1)
# # list2 = []
# for page_h1 in all_pages_h1:
#     print(page_h1.text)
# user_name = soup.find('div', class_='user__name').find('span').text.strip()
# print(user_name)
# user_name2 = soup.find(('div', {'class': 'user_name', 'id': 'aaa'})).find('span').text
# print(user_name2)
# find_all_spans_in_un = soup.find(class_='user__info').find_all('span')
# print(find_all_spans_in_un[1].text)
# links = soup.find(class_='social__networks').find('ul').find_all('a')
# print(links)
# all_a = soup.find_all('a')
# print(all_a)

# for i in all_a:
#     item_text = i.text
#     item_url = i.get('href')
#     print(f'{item_text}: {item_url}')

# post_div = soup.find(class_='post__text').find_parent('div', 'user__post')
# print(post_div)

# post_divs = soup.find(class_='post__text').find_parents()
# print(post_divs)

# next_el = soup.find(class_='post__title').find_next().text
# print(next_el)
# next_sib = soup.find(class_='post__title').find_next_sibling()
# print(next_sib)
# prev_sib = soup.find(class_='post__date').find_previous_sibling().find_next()
# print(prev_sib.text)

# links = soup.find(class_='some__links').find_all('a')
# for link in links:
#     links_href = link.get('href')
#     links_data = link.get('data-attr')
#     print(links_href)
#     print(links_data)

# links = soup.find(class_='some__links').find_all('a')
# print(links)
# for link in links:
#     links_href = link['href']
#     links_data = link['data-attr']
#     print(links_href)
#     print(links_data)

# find_a_by_text = soup.find('a', text=re.compile('Одежда'))
# print(find_a_by_text)
