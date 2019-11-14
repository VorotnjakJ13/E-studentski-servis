# -*- coding: utf-8 -*-

from bs4 import BeautifulSoup
import requests 
import re
import csv
import pandas

############################################################
url = 'https://www.studentski-servis.com/index.php?t=prostaDela&hp=true&page=1&perPage=3016&sort=1&workType=1&keyword='
       
url_data=requests.get(url).content

soup = BeautifulSoup(url_data,'html.parser')

#############################################################
## SEZNAMI:
jobs = soup.findAll('div',{'class':'jobItem'})
ime = soup.findAll('span', {'class':'title'})
placa = soup.findAll('span',{'class':'postavka'})
lokacija = soup.findAll('span',{'class':'lokacija'})
opis = soup.findAll('div',{'class':'jobContent col'})
opiss= soup.findAll('p')
sifre=[]
for i in range(len(jobs)):
    sifra = jobs[i].li.parent.li.next_sibling.next_sibling.next_sibling.next_sibling.next_sibling.next_sibling
    sifre.append(sifra.text)

dataset= [(s,i.text,p.text,l.text,op.text) for s,i,p,l,op in zip( sifre,ime,placa,lokacija,opis)]



with open('estudent.csv','w+',encoding='utf-8') as csvfile: 
    writer = csv.writer(csvfile)
   
    for tuple in dataset:
        if tuple[0] is csvfile.read():
            None
        else:
            writer.writerow(tuple)

