from django.core.management.base import BaseCommand
from makeup.models import Makeup
from django.db.models import Count

class Command(BaseCommand):
    help = 'Remove duplicate makeup entries based on name'

    def handle(self, *args, **options):
        # Find duplicates
        duplicates = Makeup.objects.values('name').annotate(count=Count('id')).filter(count__gt=1)

        total_deleted = 0
        for dup in duplicates:
            name = dup['name']
            makeups = Makeup.objects.filter(name=name).order_by('id')
            # Keep the first one
            keep = makeups.first()
            deleted_count = makeups.exclude(id=keep.id).delete()[0]
            total_deleted += deleted_count
            self.stdout.write(f"Removed {deleted_count} duplicates for '{name}'")

        self.stdout.write(self.style.SUCCESS(f'Total duplicates removed: {total_deleted}'))
