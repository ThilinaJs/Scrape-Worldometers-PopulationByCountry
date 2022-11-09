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
    dic['Density (P/SquareKm)']=row.find_all('td')[5].text
    dic['Land Area (SquareKm)']=row.find_all('td')[6].text.replace(',','')
    dic['Migrants (net)']=row.find_all('td')[7].text.replace(',','')
    dic['Fert. Rate']=row.find_all('td')[8].text
    dic['Med. Age']=row.find_all('td')[9].text
    dic['Urban Pop %']=row.find_all('td')[10].text
    dic['World Share']=row.find_all('td')[11].text

    countries_list.append(dic)

dataset = pd.DataFrame(countries_list)

dataset.to_excel("PopulationByCountry.xlsx", index=False)