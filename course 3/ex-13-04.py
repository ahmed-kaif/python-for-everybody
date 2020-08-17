import urllib.request
import urllib.parse
import urllib.error
import json

url = input('Enter location: ')
print('Retriveing', url)

uh = urllib.request.urlopen(url)
data = uh.read().decode()
print('Retrieved', len(data), 'characters.')
js = json.loads(data)
count = 0
sum = 0
i = 0
for item in js:
    while i < len(js["comments"]):
        sum = sum + int(js["comments"][i]["count"])
        i = i+1
        count = count + 1
print('Count:', count)
print('Sum', sum)
