import time
import pandas as pd
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.by import By


url = 'https://www.cbf.com.br/futebol-brasileiro/competicoes/campeonato-brasileiro-serie-a'


option = Options()
option.headless = True
driver = webdriver.Edge()


driver.get(url)
time.sleep(3)


# Tabela Brasileirão

element1 = driver.find_element(
    by=By.XPATH, value='//*[@id="menu-panel"]/article/div[1]/div/div/section/div[1]/table')
html_content1 = element1.get_attribute('outerHTML')

soup1 = BeautifulSoup(html_content1, 'html.parser')
table1 = soup1.find(name='table')

df_full = pd.read_html(str(table1))[0]
tabela = df_full[['Posição', 'PTS', 'J', 'V', 'D', 'E', 'SG']]
tabela.columns = ['posição', 'pontos', 'jogos',
                  'vitórias', 'derrotas', 'empates', 'saldo de gols']
print(tabela)
time.sleep(5)


# Artilharia

driver.find_element(
    by=By.XPATH, value='//*[@id="menu-panel"]/article/section[2]/div/div/div/table/tbody/tr[131]/td/a/b').click()

element = driver.find_element(
    by=By.XPATH, value='//*[@id="menu-panel"]/article/section[2]/div/div/div/table')
html_content = element.get_attribute('outerHTML')


soup = BeautifulSoup(html_content, 'html.parser')
table = soup.find(name='table')

df_full = pd.read_html(str(table))[0].head(10)
df = df_full[['Nome', 'Apelido', 'Gols']]
print(df)


driver.quit()
