from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import render, redirect
from .models import *

menu = {'Помощь': ['Как сделать заказ?', 'Оплата', 'Доставка', 'Задать вопрос'], 'О нас': ['Контакты', 'О компании']}
details_type = ['Фронтальная камера', 'Основная камера', 'Нижний шлейф', 'Шлейф кнопок', 'Корпус', 'Аккумулятор',
                'Дисплей', 'Дисплей Orig', 'Антенна NFC', 'Разговорный динамик', 'Основной динамик', 'Вибромотор',
                'Корпусный элемент', 'Плата на запчасти', 'Плата без Touch ID', 'Плата с Touch ID', 'Телефон']
categories_details_type = ['Антенны', 'Динамики, вибро, taptic', 'Дисплеи', 'Камера', 'Коннекторы', 'Корпуса',
                           'Корпусные части', 'Микросхемы', 'Микрофоны', 'Стекло для Apple/iPhone', 'Тачскрины',
                           'Шлейфы']
catalog_elements = ['Apple', 'Смартфона', 'Ноутбука', 'Планшета', 'Аксессуары',
                    'Инструменты', ]

details_model = ['6', '6s', '7', '8', 'X']


def base(request):
    menu = {'Помощь': ['Как сделать заказ?', 'Оплата', 'Доставка', 'Задать вопрос'],
            'О нас': ['Контакты', 'О компании']}

    context = {
        'posts': Details.objects.all(),
        'menu': menu,
        'title': 'Главная страница',
    }

    return render(request, 'details/base.html', context)


def head_page(request):
    catalog_elements_dict1 = {'Apple': 'apple.png', 'Cмартфонов': 'Smartphone.png',
                              'Ноутбуков': 'Laptop.png', 'Планшетов': 'tablet.png',
                              'Аксессуары': 'accessories.png', 'Инструменты': 'insruments.png'}
    catalog_elements_dict = {i: f"details/images/spare_patrs/for_cats_name/{j}" for i, j in
                             catalog_elements_dict1.items()}
    return render(request, 'details/head_page.html', {
        'posts': Details.objects.all()[:5],
        'menu': menu,
        'catalog_elements': catalog_elements,
        'catalog_elements_dict': catalog_elements_dict,
        'categories_details_type': categories_details_type,
        'title': 'Главная страница'})


def about(request):
    return render(request, 'details/about.html', {'title': 'О сайте'})


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
