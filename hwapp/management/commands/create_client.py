from django.core.management.base import BaseCommand
from hwapp.models import Client


class Command(BaseCommand):
    help = 'Create client'

    def handle(self, *args, **kwargs):
        client = Client(name='Misha', email='misha@example.com', phone_number=8321654789, address='avenue 547')
        client.save()
        self.stdout.write(f'{client}')


