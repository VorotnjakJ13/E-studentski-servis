# To add a new cell, type '# %%'
# To add a new markdown cell, type '# %% [markdown]'
# %%
# -*- coding: utf-8 -*-


# %%
from bs4 import BeautifulSoup
import requests 
import re
import csv
import pandas as pd


# %%
url = 'https://www.studentski-servis.com/index.php?t=prostaDela&hp=true&page=1&perPage=3016&sort=1&workType=1&keyword='
       
url_data=requests.get(url).content

soup = BeautifulSoup(url_data,'html.parser')


# %%
# SEZNAMI:
jobs = soup.findAll('div',{'class':'jobItem'})
ime = soup.findAll('span', {'class':'title'})
placa = soup.findAll('span',{'class':'postavka'})
lokacija = soup.findAll('span',{'class':'lokacija'})
opis = soup.findAll('div',{'class':'jobContent col'})
opiss= soup.findAll('p')
sifre=[]
for i in range(len(jobs)):
    sifra = jobs[i].li.parent.li.next_sibling.next_sibling.next_sibling.next_sibling.next_sibling.next_sibling
    sifre.append(sifra.text.strip('Šifra: ').strip(' |'))


dataset= [(s,i.text.strip('\n'),p.text.strip('\n').strip('\r\n\t\t\t\t\t'),l.text.strip('\n'),op.text.replace('|\n','. ').replace('\n','').replace('\r','')) for s,i,p,l,op in zip( sifre,ime,placa,lokacija,opis)]


# %%
with open('estudent.csv','w+',encoding='utf-8') as csvfile: 
    writer = csv.writer(csvfile)
    writer.writerow(['sifra','naziv','placa','lokacija','opis'])
    for tuple in dataset:
        if tuple[0] is csvfile.read():
            None
        else:
            writer.writerow(tuple)


# %%
data=pd.read_csv('estudent.csv')
pd.options.display.max_rows = 20
data


# %%
vzorec_neto = re.compile(r"(?P<neto>.*?)+€\/h neto",flags=re.DOTALL)


# %%



# %%



# %%



