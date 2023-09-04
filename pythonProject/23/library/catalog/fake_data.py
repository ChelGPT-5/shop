import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'library.settings')
django.setup()

from catalog.models import Author, Country
from faker import Faker
from django_seed import Seed

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
# fake = Faker()
#
# for _ in range(20):
#     country_name = fake.country()
#     Country.objects.create(name=country_name)
#
# countries = Country.objects.all()
#
# for _ in range(100):
#     author_data = {
#         'first_name': fake.first_name(),
#         'last_name': fake.last_name(),
#         'pseudonym': fake.user_name(),
#         'date_of_birth': fake.date_of_birth(tzinfo=None, minimum_age=18, maximum_age=100),
#         'country': fake.random_element(elements=countries)
#     }
#
#     if fake.random_int(min=0, max=0):
#         author_data['date_of_death'] = fake.date_of_birth(tzinfo=None, minimum_age=1, maximum_age=40),
#
#     Author.objects.create(**author_data)
