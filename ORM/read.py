import peewee
from models import Product, Category

def get_categories():
    return Category.select()
def get_all_products():
    return Product.select()

categories = get_categories()
# print(categories)
print('Категории в бд: ')
for x in categories:
    print(type(x))
    print(x)
    print(x.name)
    print(x.created_at)
    print()

products = get_all_products()
print('все товары в бд: ')
for x in products:
    print(x.title, x.price, x.category_id)
    print()