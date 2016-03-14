from django.core.management.base import BaseCommand, CommandError
from staff.models import Document


class Command(BaseCommand):
    help = 'Show people who has specified education'

    def add_arguments(self, parser):
        parser.add_argument('mess', nargs=1)

    def handle(self, *args, **options):
        for item in options['mess']:
            doc = Document.objects.filter(education__icontains=item)
            if doc.exists():
                for d in doc:
                    self.stdout.write("%s" % d.people_id.name)
            else:
                raise CommandError('Education "%s" does not exist' % item)
