from django.core.management.base import BaseCommand
from django.core.management import call_command

class Command(BaseCommand):
    help = 'Load initial car rows'

    def handle(self, *args, **options):
        call_command('loaddata', 'car_fixture.json')