#Group 2 Code File.
#<------------------------------------------------>
# Working code to take the code directly from the webpage to the file.
import csv

from urllib.request import urlopen, Request
from bs4 import BeautifulSoup


url = 'https://en.wikipedia.org/wiki/Median_income'
req = Request(url, headers = {'User-Agent':'Mozilla/5.0'})
html = urlopen(req)
bs = BeautifulSoup(html, 'html.parser')
#<---------------------------------------------------------------->
# Code to create a table 
import pandas as pd

A=[]
B=[]

for row in table.find_all('tr'):
    cells = [cell.get_text(strip=True) for cell in row.find_all(["th","td"])]
    if cells:
        A.append(cells[0])
        num_str = "".join(ch for ch in cells[1] if ch.isdigit() or ch == ".")
        B.append(float(num_str))
    
df = pd.DataFrame({'Location':A,'2021 USD':B})
df
#<-------------------------------------------------------------------->
# This should output the file using the correct directions
df.to_csv("right_file", index=False)
