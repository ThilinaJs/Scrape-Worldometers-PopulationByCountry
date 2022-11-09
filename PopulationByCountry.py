import requests
from bs4 import BeautifulSoup
import pandas as pd

url = "https://www.worldometers.info/world-population/population-by-country/"

response = requests.get(url)

soup = BeautifulSoup(response.text, 'html.parser')

rows = soup.find('table',{'id':'example2'}).find('tbody').find_all('tr')

countries_list = []

for row in rows:
    dic = {}
    dic['Country']=row.find_all('td')[1].text
    dic['Population']=row.find_all('td')[2].text.replace(',','')
    dic['Yearly Change']=row.find_all('td')[3].text
    dic['Net Change']=row.find_all('td')[4].text.replace(',','')
    dic['Density (P/SquareKm) ']=row.find_all('td')[5].text
    dic['Land Area (SquareKm) ']=row.find_all('td')[6].text.replace(',','')

    countries_list.append(dic)

print(countries_list[0])