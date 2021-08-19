import requests
from time import sleep
import random

BASE_URL = 'http://18.205.159.66'

product_pages = [
    'product01.html',
    'product02.html',
    'product03.html',
    'product04.html',
    'product05.html',
    'product06.html',
    'product07.html',
    'product08.html',
    'product09.html',
    'product10.html',
    'product11.html',
    'product12.html',
    'product13.html',
    'product14.html',
    'product15.html',
    'product16.html',
    'product17.html',
    'product18.html',
    'product19.html',
    'product20.html',
]


def get_address(page='index.html'):
    response = requests.get(f'{BASE_URL}/{page}')
    print(response)

while True:
    page = random.choice(product_pages)
    get_address(page)
    sleep(2)
