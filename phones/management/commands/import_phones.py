import csv

from django.core.management.base import BaseCommand
from phones.models import Phone


class Command(BaseCommand):
    def handle(self, *args, **options):
        file_path = 'phones.csv'
        with open(file_path, 'r') as csvfile:
            reader = csv.DictReader(csvfile, delimiter=';')
            for row in reader:
                Phone.objects.create(
                    name=row['name'],
                    price=row['price'],
                    image=row['image'],
                    release_date=row['release_date'],
                    lte_exists=row['lte_exists']
                )
        self.stdout.write(self.style.SUCCESS('Phones imported successfully'))
