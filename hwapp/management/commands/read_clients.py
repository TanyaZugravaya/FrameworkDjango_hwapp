from django.core.management.base import BaseCommand
from hwapp.models import Client


class Command(BaseCommand):
    help = "Get all users."

    def handle(self, *args, **kwargs):
        client = Client.objects.all()
        self.stdout.write(f'{client}')
