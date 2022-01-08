
import requests

adress = input('Enter adress ')

respond = requests.get(adress)

data = respond.content

with open('file_browser.bin','wb') as f:
    f.write(data)

