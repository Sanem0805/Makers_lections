import peewee 
from models import Category, Product
import random

def add_category(name):
    try:
        data = Category(name=name.lower().strip())
        data.save()
        print(f'сохранили категорию {name.strip()}!')
    except (peewee.IntegrityError, peewee.InternalError):
        print('такая категория уже существует!')
# add_category('   платья   ')
# add_category('джинсы')
# add_category('футболки')
# add_category('свитер')
# add_category('обувь')

def add_product(name, price, caterogy_name):
    try:
        category_id = Category.get(name=caterogy_name.lower().strip())
    except peewee.DoesNotExist:
        category_id = None

    if category_id:
        data = Product(title=name, price=price, category_id=category_id)
        data.save()
        print(f'сохронили товар {name}')
    else:
        print(f'Категории {caterogy_name} не существует')

add_product('Zara t-short', 300, 'футболки')
add_product('Pilow', 100, 'подушки')
add_product('Jeans', 500, 'джинсы')
add_product('Iphone 15', 1800, 'телефоны')
