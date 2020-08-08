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

# Retrieve all the span tags
sum = 0
tags = soup('span')
for tag in tags:
    num = tag.string  # string method pulls out the content inside the tag as Unicode string
    sum = sum + int(num)
print('Sum', sum)
