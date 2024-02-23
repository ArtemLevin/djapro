import fake as fake
from django.core.management.base import BaseCommand
from app_1.models import Product
from random import choice, randint
from faker import Faker

fake = Faker()

with open('fruits.txt', 'r', encoding='utf-8') as f:
    fruits=[]
    for line in f:
        if len(line) > 2:
            fruits.append(line.strip())

FRUITS = fruits

class Command(BaseCommand):
    help = "Create product."

    def handle(self, *args, **kwargs):
        for i in range(15):
            product = Product(
                name=choice(FRUITS),
                price=choice([i for i in range(100)]),
                description=f'description_{i}',
                add_date=fake.date()
            )

            product.save()
            self.stdout.write(f'{product}')
