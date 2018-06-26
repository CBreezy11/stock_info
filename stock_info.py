import requests
from bs4 import BeautifulSoup
import boto3
import datetime

class DynamoStock(object):
    def __init__(self):
        self.dynamodb_resource = boto3.resource('dynamodb')

    def add_item(self, data_dict):
        self.dynamodb_resource.Table('InsiderTrading').put_item( Item = data_dict)
        
class Traders(DynamoStock):
    def __init__(self):
        super().__init__()
        self.url = 'https://finance.yahoo.com/quote/{}/press-releases?p={}'
        self.stock_list =["FB", "AAPL", "GOOG", "MSFT", "BABA", "NFLX", "NVDA", "INTC",]
        self.timenow = datetime.datetime.now().strftime("%m-%d-%Y")

    def compile(self):
        for stock in self.stock_list:
            self.get_traders(stock)
            

    def get_traders(self, stock_name):
        url = self.url.format(stock_name, stock_name)
        page = requests.get(url)
        soup = BeautifulSoup(page.text, 'html.parser')
        base = soup.find('u')
        news = base.find_next()
        item_dict = {'{} News'.format(self.timenow):news.text}
        item_dict.update({'company_name': stock_name})
        self.add_item(item_dict)
   







