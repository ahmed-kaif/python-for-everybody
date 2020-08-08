import urllib.request
import urllib.parse
import urllib.error
import xml.etree.ElementTree as ET
import ssl

# ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter Location: ')
data = urllib.request.urlopen(url, context=ctx).read()

print('Retrieving', url)
print('Retrieved', len(data), 'characters')
tree = ET.fromstring(data)
counts = tree.findall('.//count')  # this is a list of all count tags
sum = 0
for count in counts:
    num = count.text
    sum = sum + int(num)
print('Count:', len(counts))
print('Sum', sum)
