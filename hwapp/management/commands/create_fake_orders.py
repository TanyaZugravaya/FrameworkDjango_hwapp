from django.core.management.base import BaseCommand
from faker import Faker
from hwapp.models import Client, Product, Order
import random

fake = Faker()


class Command(BaseCommand):
    help = 'Populate tables with random data'

    def handle(self, *args, **kwargs):
        clients = Client.objects.all()
        products = Product.objects.all()

        for _ in range(30):
            client = random.choice(clients)
            order = Order.objects.create(
                customer=client,
                total_price=0
            )
            for _ in range(random.randint(1, 5)):
                product = random.choice(products)
                order.products.add(product)
                order.total_price += product.price
            order.save()

        self.stdout.write(self.style.SUCCESS('Data populated successfully'))
