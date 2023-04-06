from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import render, redirect
from .models import *

menu = ['Главная', 'Как сделать заказ?', 'Доставка', 'Оплата', 'Контакты', 'Войти']
spare_parts = {'Фронтальная камера': 300,
               'Основная камера': 400,
               'Нижний шлейф': 300,
               'Шлейф кнопок': 300,
               'Корпус': 400,
               'Аккумулятор': 400,
               'Дисплей': 900,
               'Дисплей Orig': 1400,
               'Антенна NFC': 300,
               'Разговорный динамик': 300,
               'Основной динамик': 300,
               'Вибромотор': 300,
               'Внутренний корпусный элемент': 100,
               'Плата на запчасти': 1000,
               'Плата без Touch ID': 2500,
               'Плата с Touch ID': 3500,
               'Телефон': 10000}
spare_part = [i for i, j in spare_parts.items()]


def head_page(request):
    return render(request, 'details/head_page.html', {'posts': spare_part, 'menu': menu, 'title': 'Главная страница'})


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
