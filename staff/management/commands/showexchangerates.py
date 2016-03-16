from django.core.management.base import BaseCommand
from ._parser import URL, URL2, get_html, parse, parse2


class Command(BaseCommand):
    help = 'Show Exchange Rates from two sites'

    def handle(self, *args, **options):
        html = get_html(URL)
        data = parse(html)
        self.stdout.write(self.style.SUCCESS(URL))
        for d in data:
            self.stdout.write(d)

        html2 = get_html(URL2)
        data2 = parse2(html2)
        self.stdout.write(self.style.SUCCESS(URL2))
        for d in data2:
            self.stdout.write(d)
