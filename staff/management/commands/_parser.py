from bs4 import BeautifulSoup
import urllib


URL = 'http://minfin.com.ua/currency/banks/'
URL2 = 'http://finance.i.ua/'


def get_html(url):
        """Get html."""
        response = urllib.urlopen(url)
        return response.read()


def parse(html):
    """Parse first site."""
    soup = BeautifulSoup(html, "html.parser")
    table = soup.find(
        'table', class_='mfm-table mfcur-table-lg-banks mfcur-table-lg')

    r = table.find_all('tr')[0]
    th = r.find_all('th')
    head = "%s    %s    %s " % (
        th[0].get_text(),
        th[1].find('span',
                   class_='mfcur-thead-title').contents[0].strip().upper(),
        th[2].get_text())

    rows = table.find_all('tr')[1:4]
    data = []
    data.append(head)
    for row in rows:
        td = row.find_all('td')
        td0 = td[0].text.strip()
        td1 = "%s/%s" % (
            td[1].contents[0].strip(), td[1].contents[2].strip())
        td2 = td[2].find(
            'span', class_='mfcur-nbu-full-wrap').contents[0].strip()
        st = "%s           %s    %s" % (td0, td1, td2)
        data.append(st)
    return data


def parse2(html):
    """Parse second site."""
    soup = BeautifulSoup(html, "html.parser")
    table = soup.find_all('table')[3]

    data = []
    rows = table.find_all('tr')[1:]
    for row in rows:
        b = row.find('b').get_text()
        td = row.find_all('big')
        td0 = "%s/%s" % (td[0].text, td[1].text)
        td1 = td[2].text
        st = "%s             %s      %s" % (b, td0, td1)
        data.append(st)
    return data
