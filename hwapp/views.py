import logging
from django.utils import timezone
from datetime import timedelta

from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import ListView

from .models import Order, Product, Client

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


class OrderList(ListView):
    model = Order
    template_name = 'order_list.html'

    def get_queryset(self):
        client_id = self.kwargs['client_id']
        return Order.objects.filter(customer_id=client_id)


def client_orders(request, client_id):
    client = Client.objects.get(id=client_id)
    orders = Order.objects.filter(customer=client).order_by('-date_ordered')

    # Выбираем товары заказов за последние 7 дней
    orders_last_week = orders.filter(date_ordered__gte=timezone.now() - timedelta(days=7)).distinct()
    last_week_products = Product.objects.filter(order__in=orders_last_week).distinct()

    # Выбираем товары заказов за последние 30 дней
    orders_last_month = orders.filter(date_ordered__gte=timezone.now() - timedelta(days=30)).distinct()
    last_month_products = Product.objects.filter(order__in=orders_last_month).distinct()

    # Выбираем товары заказов за последние 365 дней
    orders_last_year = orders.filter(date_ordered__gte=timezone.now() - timedelta(days=365)).distinct()
    last_year_products = Product.objects.filter(order__in=orders_last_year).distinct()

    return render(request, 'client_orders.html', {
        'client': client,
        'last_week_products': last_week_products,
        'last_month_products': last_month_products,
        'last_year_products': last_year_products,
    })
