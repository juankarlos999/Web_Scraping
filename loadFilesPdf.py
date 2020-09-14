#!/usr/bin/python3
import requests
from bs4 import BeautifulSoup

url = 'https://dapre.presidencia.gov.co/normativa/normativa/'
page = requests.get(url)
soup = BeautifulSoup(page.text, 'lxml')
recursos = soup.find_all('div', attrs={'class': "ms-vb itx"})
url2 = 'https://dapre.presidencia.gov.co'
links = []
for recurso in recursos:
    links.append(recurso.a.get('href'))
toget = []
for link in links:
    toget.append(url2 + link)
for i, get in enumerate(toget):
    variable = "./rengifo"+ str(i) + ".pdf"
    pdf = requests.get(get)
    with open(variable, 'wb') as f:
        f.write(pdf.content)
