from bs4 import BeautifulSoup
import requests
import re
#import csv

############################################################
url = 'https://www.studentski-servis.com/index.php?t=prostaDela&hp=true&page=1&perPage=3016&sort=1&workType=1&keyword='
url_data = requests.get(url).content
url_data= url_data.decode('utf-8')

soup = BeautifulSoup(url_data,'html.parser')
#############################################################

##################################################
#job_patt=re.compile(
    #  r'<div class="jobItem"><div class="col jobTitle clear "><span class="title">(?P<name>.*?)</span>'
    #  r'<span class="postavka"><img src="resources/images/icons/icon_euro.png" /><strong>(?P<neto>.*?)</strong>(?P<bruto>.*?)</span>'
    #  r'<span class="lokacija"><img src="resources/images/icons/icon_job_location.png" /><strong>(?P<location>.*?)</strong>'
    #  r'<div class="jobContent col"><p>(?P<opis>.*?)</p>'
    #  r'<li><strong>*t. prostih mest:</strong>(?P<mesta>.*?)<span class="spacer">|</span></li>'
    #  r'<li><strong>Trajanje:</strong> (?P<trajanje>.*?)<span class="spacer">|</span></li>'
    #  r'<li><strong>Delovnik:</strong>(?P<delovanik>.*?)<span class="spacer">|</span></li>'
    #  r'<li><strong>*ifra:</strong>(?P<sifra>.*?)</li>'
    #  r'<p class="textcenter"><a class="button button1" href=(?P<link>.*?)target="_blank">',flags=re.DOTALL)
##############################################
# name_patt= re.compile(r'<span class="title">(?P<name>.*?)</span>',flags=re.DOTALL)
# pay_patt= re.compile(r'<span class="postavka"><strong>(?P<neto>.*?)</strong>(?P<bruto>.*?)</span>',flags=re.DOTALL)
# location_patt = re.compile(r'<span class="lokacija"><strong>(?P<location>.*?)</strong>',flags=re.DOTALL)
# opis_patt = re.compile(r'<div class="jobContentcol"><p>(?P<opis>.*?)</p>',flags=re.DOTALL)
# sifra_patt= re.compile(r'<li><strong>*ifra:</strong>(?P<sifra>.*?)<span class="sacer">|</span>',flags=re.DOTALL)
# mesta_patt=re.compile(r'<li><strong>*t. prostih mest:</strong>(?P<mesta>.*?)<span class="spacer">|</span></li>',flags=re.DOTALL)
# trajanje_patt=re.compile(r'<li><strong>Trajanje:</strong>(?P<trajanje>.*?)<span class="spacer">|</span></li>', flags=re.DOTALL)
# delovnik_patt=re.compile(r'<li><strong>Delovnik:</strong>(?P<delovnik>.*?)<span class="spacer">|</span></li>',flags=re.DOTALL)
# tip_patt=re.compile(r'<li class="naravaDela"><strong>Narava dela:</strong>(?P<tip>.*?)</li> </ul>',flags=re.DOTALL)
# link_patt=re.compile(r'<div class="col actionBlock"><p class="textcenter"><a class="button button1" href=(?P<link>.*?)target="_blank">',flags=re.DOTALL)
    
# ############################################
seznam=[]
for job in soup.findAll('div', class_ = 'jobItem'):
    name = job.div.span.text
    name= str(name.encode('utf-8'))
    pay_neto = job.div.strong.text
    
    seznam.append((name,pay_neto))












