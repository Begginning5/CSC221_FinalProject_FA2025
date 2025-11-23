#Group 2 Code File.
import csv

from urlib.request import urlopen
from bs4 import BeautifulSoup

# The first part of the assignment is to pull the table off of the webpage.
# I am converting the table directly to the CSV file.
html = urlopen('https://en.wikipedia.org/wiki/Median_income')
bs = BeautifulSoup(html, 'html.parser')

# The main comparison table is currently the first table on the page.
table = bs.find('table',{'class':'wikitable'})
rows = table.findAll('tr')
csvFile = open('countries.csv','wt+')
writer = csv.writer(csvFile)
try:
  for row in rows:
    csvRow=[]
    for cell in row.findAll(['td','th']):
      csvRow.append(cell.get_text().strip())
    writer.writerow(csvRow)
finally:
  csvFile.close()

# I have 2 options I can take the information from the webpage and convert it into tables.

  
# Or I can take the information on the CSV and convert it into a webpage. 

