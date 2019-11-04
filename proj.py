# coding: 'utf8'

from bs4 import BeautifulSoup
import requests
import csv
# import re
############################################################
url = 'https://www.studentski-servis.com/index.php?t=prostaDela&hp=true&page=1&perPage=3016&sort=1&workType=1&keyword='
url_data = requests.get(url).content
soup = BeautifulSoup(url_data,'html.parser', from_encoding='utf-8')
#############################################################
jobs = soup.findAll('div',{'class':'jobItem'})
ime = soup.findAll('span', {'class':'title'})
placa = soup.findAll('span',{'class':'postavka'})
lokacija = soup.findAll('span',{'class':'lokacija'})
opis = soup.findAll('div',{'class':'jobContent col'})

dataset = [(a.text,b.text,c.text,d.text) for a,b,c,d in zip( ime,placa,lokacija,opis)]


with open('estudent.csv','w') as csvfile: 
    writer = csv.writer(csvfile)
    for touple in dataset:
        for niz in touple:
            
            niz.replace('\u20ac', 'EUR')
            niz.replace('\u010d','č' )
            niz.replace('\u010c','Č')
            niz.replace('\u0160','š')
            niz.replace('\u0161','Š')
            niz.replace('\u017d','Ž')
            niz.replace('\u017d','ž')
            niz.encode('utf-8')
           
            writer.writerow(touple).encode('utf-8',errors='strict')
        




