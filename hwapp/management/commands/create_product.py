from datetime import date
from random import randint

from django.core.management.base import BaseCommand
from hwapp.models import Product


class Command(BaseCommand):
    help = 'Create product'

    def handle(self, *args, **kwargs):
        for i in range(10):
            product = Product(name=f'Product{i}', description=f'description of product{i}',
                              price=2 * i * randint(1, 5), quantity=randint(0, 50), date_added=date.day)
            product.save()
            self.stdout.write(f'{product}')
