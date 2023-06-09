from django.http import HttpResponse, HttpResponseNotFound, JsonResponse
from django.shortcuts import render, redirect
from .models import *

menu = {'Помощь': ['Как сделать заказ?', 'Оплата', 'Доставка', 'Задать вопрос'], 'О нас': ['Контакты', 'О компании']}
details_type = ['Фронтальная камера', 'Основная камера', 'Нижний шлейф', 'Шлейф кнопок', 'Корпус', 'Аккумулятор',
                'Дисплей', 'Дисплей Orig', 'Антенна NFC', 'Разговорный динамик', 'Основной динамик', 'Вибромотор',
                'Корпусный элемент', 'Плата на запчасти', 'Плата без Touch ID', 'Плата с Touch ID', 'Телефон']
categories_details_type = sp_list = ['Антенны', 'Динамики, вибро, taptic', 'Дисплеи', 'Камера', 'Коннекторы', 'Корпуса',
                           'Корпусные части', 'Микросхемы', 'Микрофоны', 'Стекло для Apple/iPhone', 'Тачскрины',
                           'Шлейфы', 'Платы']
catalog_elements = ['Apple', 'Смартфона', 'Ноутбука', 'Планшета', 'Аксессуары',
                    'Инструменты', ]

details_model = ['iPhone 6', 'iPhone 6s', 'iPhone 7', 'iPhone 7 Plus', 'iPhone 8', 'iPhone 8 Plus', 'iPhone X', 'iPhone XR', 'iPhone XS', 'iPhone XS Max', 'iPhone 11', 'iPhone 11 Pro', 'iPhone 11 Pro Max', 'iPhone SE 2', 'iPhone 12', 'iPhone 12 Mini', 'iPhone 12 Pro', 'iPhone 12 Pro Max']
catalog_elements_dict1 = {'Apple': 'apple.png', 'Cмартфонов': 'Smartphone.png',
                          'Ноутбуков': 'Laptop.png', 'Планшетов': 'tablet.png',
                          'Аксессуары': 'accessories.png', 'Инструменты': 'insruments.png'}
catalog_elements_dict = {i: f"details/images/spare_patrs/for_cats_name/{j}" for i, j in
                         catalog_elements_dict1.items()}



def base(request):
    menu = {'Помощь': ['Как сделать заказ?', 'Оплата', 'Доставка', 'Задать вопрос'],
            'О нас': ['Контакты', 'О компании']}

    context = {
        'posts': Details.objects.all(),
        'menu': menu,
        'title': 'Главная страница',
    }

    return render(request, 'details/base.html', context)


def hi(request):
    return render(request, 'details/greeting.html')


def head_page(request):
    return render(request, 'details/head_page.html', {
        'posts': Details.objects.all()[:10],
        'menu': menu,
        'catalog_elements': catalog_elements,
        'catalog_elements_dict': catalog_elements_dict,
        'categories_details_type': categories_details_type,
        'title': 'Главная страница'})


def about(request):
    return render(request, 'details/about.html', {'title': 'О сайте'})


def full_catalog(request):
    enumerated_sp_list = enumerate(sp_list)  # Enumerate the list
    enumerate_details_model = enumerate(details_model)
    selected_models = request.POST.getlist('models[]')
    selected_types = request.POST.getlist('types[]')

    # Perform filtering on the spare parts based on the selected values
    filtered_parts = Details.objects.filter(details_model=selected_models, details_type=selected_types)

    # Create a list of filtered parts
    filtered_parts_list = []
    for part in filtered_parts:
        part_data = {
            'type': part.type,
            'model': part.model,
            'price': part.price,
            # Add other fields as needed
        }
        filtered_parts_list.append(part_data)

    return render(request, 'details/catalog.html',
                  {'posts': Details.objects.all(),
                   'menu': menu,
                   'catalog_elements': catalog_elements,
                   'catalog_elements_dict': catalog_elements_dict,
                   'categories_details_type': categories_details_type,
                   'phone_model': enumerate_details_model,
                   'sp_list': enumerated_sp_list,
                   'title': 'Главная страница'})


def categories(request):
    return render(request, 'details/index.html', {'menu': menu, 'title': ' Категории деталей'})


def details_list(request):
    return HttpResponse("Перечень всех запчастей.")


def displays(request):
    return HttpResponse(f"Дисплей на ваш любой ваш IPhone.")


def displays_exect(request, IPhone_model):
    try:
        if IPhone_model[1:] != 's' or IPhone_model[2:] != '':
            if IPhone_model[1] == 's' or IPhone_model[2] == 'P' or 'M':
                return HttpResponse(f"Дисплей на ваш IPhone {IPhone_model[0:2] + ' ' + IPhone_model[2:]}.")
            return HttpResponse(f"Дисплей на ваш IPhone {IPhone_model[0] + ' ' + 'Plus'}.")
        return HttpResponse(f"Дисплей на ваш IPhone {IPhone_model}.")
    except Exception as ex:
        return HttpResponse(f"Дисплей на любой IPhone.")


def pageNotFound(request, exception):
    # return redirect('/')
    return HttpResponseNotFound('<h1>Страница не найдена</h1>')
