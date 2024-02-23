from django.core.management.base import BaseCommand
from app_1.models import User
from faker import Faker

fake = Faker('ru_RU')

class Command(BaseCommand):
    help = "Create user."

    def handle(self, *args, **kwargs):
        for i in range(10):
            user = User(
                name=f'{fake.name()}',
                email=f'{fake.email()}',
                phone_number=f'{fake.phone_number()}',
                address=f'{fake.address()}'
            )

            user.save()
            self.stdout.write(f'{user}')