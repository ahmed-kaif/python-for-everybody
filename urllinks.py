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

url = input('Enter - ')
html = urllib.request.urlopen(url, context=ctx).read()
soup = bs4.BeautifulSoup(html, 'html.parser')

# Retrieve all the anchor tags
count = 0
tags = soup('a')
for tag in tags:
    print(tag.get('href', None))
    count = count + 1
print(count)
