from django.core.management.base import BaseCommand
from catalog.models import Author, Country
from django_seed import Seed


class Command(BaseCommand):
    help = 'Generate 5 random Countries and 100 random Authors'

    def handle(self, *args, **options):
        seeder = Seed.seeder()

        seeder.add_entity(Country, 5, {
            'name': lambda x: seeder.faker.country()
        })

        seeder.execute()

        countries = Country.objects.all()
        if not countries.exists():
            raise ValueError("No countries")

        seeder.add_entity(Author, 100, {
            'first_name': lambda x: seeder.faker.first_name(),
            'last_name': lambda x: seeder.faker.last_name(),
            'pseudonym': lambda x: seeder.faker.user_name(),
            'date_of_birth': lambda x: seeder.faker.date_of_birth(tzinfo=None, minimum_age=18, maximum_age=100),
            'country': lambda x: seeder.faker.random_element(elements=countries)

        })
        seeder.execute()