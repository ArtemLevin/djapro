from django.core.management.base import BaseCommand
from app_1.models import User


class Command(BaseCommand):
    def handle(self, *args, **kwargs):
        for user in User.objects.all():
            user.delete()
