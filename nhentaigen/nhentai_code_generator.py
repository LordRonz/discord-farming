#!/usr/bin/env python3

from random import randint
import requests as req
import re

def read_db():
    with open('latest.txt', 'rb') as f:
        res = int(f.readline())
    return res

def update_db():
    pattern = r'New Uploads[\w\W]+<a href="/g/[\d]+'
    resp = req.get('https://nhentai.net')
    res = re.search(pattern, resp.text).group().split('/')[3]
    with open('latest.txt', 'w') as f:
        f.write(res)

update_db()
latest = read_db()

def gen_code():
    return randint(1, latest)

async def valid_url(code_only=True):
    valid = False
    url =  ''
    while not valid:
        url =  f'https://nhentai.net/g/{gen_code()}'
        r = req.get(url)
        valid = r.status_code != 404
    return url.split('/')[-1] if code_only else url