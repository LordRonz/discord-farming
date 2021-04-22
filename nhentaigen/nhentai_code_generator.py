#!/usr/bin/env python3

from random import randint
import requests as req
import re

latest = 1

def fetch_latest():
    global latest
    pattern = r'New Uploads[\w\W]+<a href="/g/[\d]+'
    resp = req.get('https://nhentai.net')
    latest = int(re.search(pattern, resp.text).group().split('/')[3])
    return resp.ok

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