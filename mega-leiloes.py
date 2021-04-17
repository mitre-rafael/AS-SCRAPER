from lxml import html
from bs4 import BeautifulSoup
import requests
from typing import NamedTuple

class Realty:
     def __init__(self, price, desc, realtyNumber, locality, batch, auctionStatus):
         self.price = price
         self.desc = desc
         self.realtyNumber = realtyNumber
         self.locality = locality
         self.batch = batch
         self.auctionStatus = auctionStatus

def getCityInState(state):
    page = requests.get('https://www.megaleiloes.com.br/imoveis/apartamentos/' + state)

    soup = BeautifulSoup(page.content, 'html.parser')
    result = set()
    for city in soup.find_all('a', class_='card-locality'):
        result.add(city.contents[0])
        
    return result

def getRealtyData(state):
    page = requests.get('https://www.megaleiloes.com.br/imoveis/apartamentos/' + state)

    soup = BeautifulSoup(page.content, 'html.parser')  
    result = []
    for realty in soup.find_all('div', class_="card open"):
        toInsert = Realty(realty.find('div', class_= "card-price").contents[0],
                        realty.find('a', class_= "card-title").contents[0],
                        realty.find('div', class_= "card-number").contents[0],
                        realty.find('a', class_= "card-locality").contents[0],
                        realty.find('div', class_= "card-batch-number").contents[0],
                        realty.find('div', class_= "card-status").contents[0])
        result.append(toInsert)
    return result
        

print(getCityInState('rj'))
print(getRealtyData('rj')[0].price)
