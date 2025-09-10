from django.core.management.base import BaseCommand
from makeup.models import Makeup

class Command(BaseCommand):
    help = 'List all makeup names'

    def handle(self, *args, **options):
        makeups = Makeup.objects.all().order_by('name')
        for makeup in makeups:
            self.stdout.write(f"{makeup.name}")
