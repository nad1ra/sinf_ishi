import random
from django.core.management.base import BaseCommand
from faker import Faker
from products.models import Product

class Command(BaseCommand):
    help = "Seeds the database with fake products"

    def handle(self, *args, **kwargs):
        fake = Faker()
        products = []

        for _ in range(50):  # Generate 50 products
            products.append(Product(
                name=fake.company(),
                desc=fake.text(),
                price=round(random.uniform(10, 500), 2)
            ))

        Product.objects.bulk_create(products)  # Bulk insert for performance
        self.stdout.write(self.style.SUCCESS(f'Successfully added {len(products)} products!'))
