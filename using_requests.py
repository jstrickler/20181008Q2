#!/usr/bin/env python
import requests
from subprocess import run

# response = requests.get('URL', ....)
Q2_URL = "https://www.q2labsolutions.com/"

response = requests.get(Q2_URL)
for k, v in response.headers.items():
    print(k, v)

if response.status_code == requests.codes.OK:
    print(response.content.decode()[100:500])

url = "https://imgs.xkcd.com/comics/exploits_of_a_mom.png"

response = requests.get(url)


raw_pdf = response.content

with open('exploits.png', 'wb') as exploits_out:
    exploits_out.write(raw_pdf)

run('open exploits.png'.split())

