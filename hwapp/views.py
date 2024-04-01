import logging

from django.http import HttpResponse
from django.shortcuts import render

# Создайте пару представлений в вашем первом приложении:
# главная и о себе.
# � Внутри каждого представления должна быть переменная
# html - многострочный текст с HTML вёрсткой и данными о
# вашем первом Django сайте и о вас.
# � *Сохраняйте в логи данные о посещении страниц


logger = logging.getLogger(__name__)

home_html = """
    <html>
    <head><title>Главная страница</title></head>
    <body>
    <h1>Добро пожаловать на мой первый Django сайт!</h1>
    <p>Здесь вы найдете информацию о моем первом Django проекте.</p>
    </body>
    </html>
    """
about_html = """
    <html>
    <head><title>О себе</title></head>
    <body>
    <h1>Обо мне</h1>
    <p>Здесь вы найдете информацию обо мне.</p>
    </body>
    </html>
    """


def about(request):
    logger.info('Посетили страницу "О себе"')
    return HttpResponse(about_html)


def home(request):
    logger.info('Посетили главную страницу')
    return HttpResponse(home_html)
