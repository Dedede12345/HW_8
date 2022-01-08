import requests
import re

respond = requests.get('https://web.ics.purdue.edu/~gchopra/class/public/pages/webdesign/05_simple.html')

data = respond.content

print(data)

for i in data:
    if ord('a') <= i <= ord('z') or ord('A') <= i <= ord('Z'):
        print(i, end=' ')

line = data.decode()

regex = re.compile('<.*?>')

tags = set(regex.findall(line))

#value = []
#line_2 = line.split
#for i in line_s:
#   if i.startswith('<') and i .endswith('>'):
#       value.append(i)
#value = set(value)

print('\n',tags)

