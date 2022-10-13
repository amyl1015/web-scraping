import requests
from bs4 import BeautifulSoup
import pandas as pd

page1 = requests.get('https://www.newyorkschools.com/districts/nyc-district-15.html')
page2 = requests.get('https://www.marketwatch.com/tools/markets/stocks/country/argentina')

# Create a BeautifulSoup object
soup1 = BeautifulSoup(page1.text, 'html.parser')
soup2 = BeautifulSoup(page2.text, 'html.parser')

# print pretty
# print(soup1.prettify())
# print(soup2.prettify())

schoolname_soup1 = soup1.find_all('div',class_='pp-col-40')
schoolname_output_descriptions = []
for i in schoolname_soup1: #for x in y: 
    # print(i.text)
    data = i.text
    schoolname_output_descriptions.append(data)
    

descriptions_soup1 = soup1.find_all('div',class_='pp-col-20')
output_descriptions = []
for i in descriptions_soup1: #for x in y: 
    # print(i.text)
    data = i.text
    output_descriptions.append(data)


output_descriptions = output_descriptions[0:42]
#print(len(output_descriptions))
#print(len(schoolname_output_descriptions)) 
df = pd.DataFrame({'school_name':schoolname_output_descriptions,'descriptions':output_descriptions})
df.to_csv('./bk.csv')




# soup2

a_soup2 = soup2.find_all('table',class_='table table-condensed')
a_output_descriptions = []
b_output_descriptions = []
c_output_descriptions = []
for i in a_soup2: #for x in y: 
    tr_a = i.find_all('tr')
    # print(tr_a)
    for j in tr_a:
        x = j.text.split('\n')
        a_output_descriptions.append(x[1])
        b_output_descriptions.append(x[2])
        c_output_descriptions.append(x[3])


df1 = pd.DataFrame({'ticker':a_output_descriptions,'something':b_output_descriptions, 'somethingelse':c_output_descriptions})

df1.to_csv('./something.csv')
  



