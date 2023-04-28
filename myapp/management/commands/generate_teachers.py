from django.core.management.base import BaseCommand
from myapp.models import Teacher
from faker import Faker


class Command(BaseCommand):
    help = 'Generates random teachers.'

    def add_arguments(self, parser):
        parser.add_argument('--number', type=int, default=100, help='Number of teachers to generate.')

    def handle(self, *args, **kwargs):
        number = kwargs['number']
        fake = Faker()
        for i in range(number):
            first_name = fake.first_name()
            last_name = fake.last_name()
            email = fake.email()
            phone_number = fake.phone_number()
            Teacher.objects.create(first_name=first_name, last_name=last_name, email=email, phone_number=phone_number)
        self.stdout.write(self.style.SUCCESS(f'Successfully generated {number} teachers.'))


