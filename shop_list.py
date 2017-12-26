# cook_book = {
#     'яичница': [
#         {'ingredient_name': 'яйца', 'quantity': 2, 'measure': 'шт.'},
#         {'ingredient_name': 'помидоры', 'quantity': 100, 'measure': 'гр.'}
#     ],
#     'стейк': [
#         {'ingredient_name': 'говядина', 'quantity': 300, 'measure': 'гр.'},
#         {'ingredient_name': 'специи', 'quantity': 5, 'measure': 'гр.'},
#         {'ingredient_name': 'масло', 'quantity': 10, 'measure': 'мл.'}
#     ],
#     'салат': [
#         {'ingredient_name': 'помидоры', 'quantity': 100, 'measure': 'гр.'},
#         {'ingredient_name': 'огурцы', 'quantity': 100, 'measure': 'гр.'},
#         {'ingredient_name': 'масло', 'quantity': 100, 'measure': 'мл.'},
#         {'ingredient_name': 'лук', 'quantity': 1, 'measure': 'шт.'}
#     ]
# }


def get_cook_book_from_file(file):
    cook_book = {}
    with open(file, encoding='utf-8') as f:
        for line in f:
            dish = line.strip().lower()
            ingredient_number = int(f.readline().strip())
            ingredients = []
            for i in range(ingredient_number):
                ingredients.append({})
                ingredient_properties = f.readline().strip().lower().split(' | ')
                ingredients[i]['ingredient_name'] = ingredient_properties.pop(0)
                ingredients[i]['quantity'] = int(ingredient_properties.pop(0))
                ingredients[i]['measure'] = ingredient_properties.pop(0)
            f.readline()

            cook_book[dish] = ingredients

    return cook_book


def get_shop_list_by_dishes(cook_book, dishes, person_count):
    shop_list = {}
    for dish in dishes:
        for ingredient in cook_book[dish]:
            new_shop_list_item = dict(ingredient)

            new_shop_list_item['quantity'] *= person_count
            if new_shop_list_item['ingredient_name'] not in shop_list:
                shop_list[new_shop_list_item['ingredient_name']] = new_shop_list_item
            else:
                shop_list[new_shop_list_item['ingredient_name']]['quantity'] += new_shop_list_item['quantity']

    return shop_list


def print_shop_list(shop_list):
    for shop_list_item in shop_list.values():
        print('{} {} {}'.format(shop_list_item['ingredient_name'], shop_list_item['quantity'],
                                shop_list_item['measure']))


def create_shop_list():
    person_count = int(input('Введите количество человек: '))
    dishes = input('Введите блюда в расчёте на одного человека (через запятую): ') \
        .lower().split(', ')
    cook_book = get_cook_book_from_file('cook_book.txt')
    shop_list = get_shop_list_by_dishes(cook_book, dishes, person_count)
    print_shop_list(shop_list)


create_shop_list()
