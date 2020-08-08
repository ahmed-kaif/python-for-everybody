# using beautiful soup
import urllib.request
import urllib.parse
import urllib.error
import bs4
import ssl

# ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter URL: ')
count = input('Enter count: ')
position = input('Enter position: ')
html = urllib.request.urlopen(url, context=ctx).read()
soup = bs4.BeautifulSoup(html, 'html.parser')

print('Retrieving:', url)
while int(count):
    tags = soup('a')
    links = list()
    for tag in tags:
        links.append(tag.get('href', None))
    url = links[int(position) - 1]
    print('Retrieving:', url)
    html = urllib.request.urlopen(url, context=ctx).read()
    soup = bs4.BeautifulSoup(html, 'html.parser')
    count = int(count) - 1
