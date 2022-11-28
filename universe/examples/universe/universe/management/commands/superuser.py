from django.contrib.auth.models import User
from django.core.management import BaseCommand


class Command(BaseCommand):

    def handle(self, *args, **options):
        User.objects.create_superuser('devlev', 'rheingoldgalaxy@gmail.com', 'Gfctrf-12')
