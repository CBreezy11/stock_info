import requests
from bs4 import BeautifulSoup

page = requests.get('https://www.insider-monitor.com/insider_stock_trading_report.html')
soup = BeautifulSoup(page.text, 'html.parser')
base = soup.find(class_='table table-condensed')
ticker = base.find_all('a')
for a in ticker:
    print(a.text)




