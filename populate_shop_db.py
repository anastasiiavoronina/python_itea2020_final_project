from models.extra_models import *
from models.shop_models import *

if __name__ == '__main__':

    pass

    # n = News(title='Discounts available', body='New products added to the sale')
    # n.save()
    # n = News(title='Laptops added', body='New category Laptops was added')
    # n.save()
    # n = News(title='Mobile phones added', body='New category Mobile phones was added')
    # n.save()
    # n = News(title='Discounts for new customers', body='New customers will get 5% discount')
    # n.save()
    # n = News(title='Discounts available', body='Check products with discounts')
    # n.save()
    # n = News(title='Boilers added', body='New category Boilers phones was added')
    # n.save()
    # n = News(title='Furniture added', body='New category Furniture was added')
    # n.save()

    # news = News.objects().order_by('-modified')[:5]
    # for n in news:
    #     print(n.title)

    # category_devices = Category.objects.get(title='Devices')
    # p = Product(title='Boiler LG', description='Boils water', in_stock=True, discount=5, price=300,category=category_devices)
    # p.save()
    # p = Product(title='Boiler Atiston', description='Boils water', in_stock=True, discount=14, price=234,category=category_devices)
    # p.save()
    # p = Product(title='Boiler Whirlpool', description='Boils water', in_stock=False, discount=0, price=321,category=category_devices)
    # p.save()
    # p = Product(title='Boiler LG 2', description='Boils water', in_stock=True, discount=40, price=580,category=category_devices)
    # p.save()
    #
    # category_devices = Category.objects.get(title='Microvaves')
    # p = Product(title='Microwave LG', description='Microwave device LG', in_stock=True, discount=5, price=45, category=category_devices)
    # p.save()
    # p = Product(title='Microwave Atiston', description='Microwave device Atiston', in_stock=True, discount=0, price=100,category=category_devices)
    # p.save()
    #
    # category_devices = Category.objects.get(title='Washing machine')
    # p = Product(title='Washing machine Whirlpool', description='Washing machine', in_stock=False, discount=0, price=780,category=category_devices)
    # p.save()
    # p = Product(title='Washing machine LG', description='Washing machine', in_stock=True, discount=3, price=647,category=category_devices)
    # p.save()