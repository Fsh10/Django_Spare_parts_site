from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import render, redirect
from .models import *

menu = ['Главная', 'Как сделать заказ?', 'Доставка', 'Оплата', 'Контакты', 'Войти']
details_type= ['Фронтальная камера', 'Основная камера', 'Нижний шлейф', 'Шлейф кнопок', 'Корпус', 'Аккумулятор', 'Дисплей', 'Дисплей Orig', 'Антенна NFC', 'Разговорный динамик', 'Основной динамик', 'Вибромотор', 'Корпусный элемент', 'Плата на запчасти', 'Плата без Touch ID', 'Плата с Touch ID', 'Телефон']

details_model = ['6','6s','7','8', 'X']

def base(request):
    return render(request, 'details/base.html', {
        'posts': Details.objects.all(),
        'menu': menu,
        'title':'Главная страница'})


def head_page(request):
    return render(request, 'details/head_page.html', {
        'posts': Details.objects.all()[295:],
        'menu': menu,
        'categories_details_type': details_type,
        'categories_details_model': [" ".join(i.split("_")) for i in details_model],
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
