import time
import numpy as np
import pandas as pd
import requests
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from bs4 import BeautifulSoup
import json

def quitapp():
    time.sleep(5)
    browser.quit()



url = "https://stats.nba.com/players/traditional/?PerMode=Totals&Season=2019-20&SeasonType=Regular%20Season&sort=PLAYER_NAME&dir=-1"
option = Options()
option.headless = True
#browser = webdriver.Firefox(options=option) #silent mode
browser = webdriver.Firefox() #verbose mode

browser.get(url)

time.sleep(10)

browser.find_element_by_xpath(
    "//div[@class='nba-stat-table']//table//thead//tr//th[@data-field='PTS']").click()

element = browser.find_element_by_xpath("//div[@class='nba-stat-table']//table")
html_content = element.get_attribute('outerHTML')

soup = BeautifulSoup(html_content, 'html.parser')
table = soup.find(name='table')

df_full = pd.read_html(str(table))[0].head(10)
print (df_full)
df = df_full[['Unnamed: 0', 'PLAYER', 'TEAM', 'PTS' ]]
df.columns = ['pos', 'player', 'team', 'total']


print('imprimndo tabela top 10 pontuacao')
print(df)

