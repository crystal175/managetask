from django.core.management.base import BaseCommand

import urllib
from bs4 import BeautifulSoup


class Command(BaseCommand):
    help = 'Show Exchange Rates'
    URL = 'http://minfin.com.ua/currency/banks/'
    URL2 = 'http://finance.i.ua/'

    def handle(self, *args, **options):

        html = self.get_html(self.URL)
        html2 = self.get_html(self.URL2)
        self.parse(html)
        self.parse2(html2)

    def get_html(self, url):
        """Get html."""
        response = urllib.urlopen(url)
        return response.read()

    def parse(self, html):
        """Parse first site."""
        soup = BeautifulSoup(html, "html.parser")
        table = soup.find(
            'table', class_='mfm-table mfcur-table-lg-banks mfcur-table-lg')

        r = table.find_all('tr')[0]
        th = r.find_all('th')
        self.stdout.write(self.style.SUCCESS(self.URL))
        head = "%s    %s    %s " % (
            th[0].get_text(),
            th[1].find('span',
                       class_='mfcur-thead-title').contents[0].strip().upper(),
            th[2].get_text())
        self.stdout.write(head)

        rows = table.find_all('tr')[1:4]
        for row in rows:
            td = row.find_all('td')
            td0 = td[0].text.strip()
            td1 = "%s/%s" % (
                td[1].contents[0].strip(), td[1].contents[2].strip())
            td2 = td[2].find(
                'span', class_='mfcur-nbu-full-wrap').contents[0].strip()
            st = "%s           %s    %s" % (td0, td1, td2)
            self.stdout.write(st)

    def parse2(self, html):
        """Parse second site."""
        soup = BeautifulSoup(html, "html.parser")
        table = soup.find_all('table')[3]

        self.stdout.write(self.style.SUCCESS(self.URL))
        rows = table.find_all('tr')[1:]
        for row in rows:
            b = row.find('b').get_text()
            td = row.find_all('big')
            td0 = "%s/%s" % (td[0].text, td[1].text)
            td1 = td[2].text
            st = "%s             %s      %s" % (b, td0, td1)
            self.stdout.write(st)