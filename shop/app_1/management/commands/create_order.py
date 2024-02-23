from django.core.management.base import BaseCommand
from app_1.models import Order, User, Product
from random import choice, randint
from faker import Faker

fake = Faker()


class Command(BaseCommand):
    help = "Create Order."

    def handle(self, *args, **kwargs):
        users_list = User.objects.all()
        products_list = Product.objects.all()

        for i in range(50):
            customer_products_list = [choice(products_list) for _ in range(randint(1, 5))]
            order = Order(
                customer=choice(users_list),
                total_price=sum([i.price for i in customer_products_list]),
                order_date=fake.date_between(start_date='-1y', end_date='today'),
            )
            order.save()
            order.products.set(customer_products_list)
            self.stdout.write(f'{order}')

