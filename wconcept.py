import requests
from bs4 import BeautifulSoup

my_header = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36',
    'x-requested-with': 'XMLHttpRequest',
    'accept': 'application/json, text/javascript, */*; q=0.01'
}

print("Start Parsing")
resp = requests.get('https://www.wconcept.co.kr/Search?type=direct&kwd=%EC%A1%B0%EB%8D%98', headers=my_header)
resp.encoding = ''
bs = BeautifulSoup(resp.text, 'lxml')

soup = bs.find('div',class_='thumbnail_list')
divs = soup.find_all('li')

product_db = dict()
for div in divs:
    img = div.find('div', class_='img').img['src'].lstrip('//').replace('?RS=300', '')
    title = div.find('div', class_='product ellipsis multiline').text.strip()
    price = div.find('span', class_='discount_price').text.strip()
    productLink = 'https://www.wconcept.co.kr' + div.find('a', class_='')['href'].strip().replace('?rccode=pc_search', '')
    
    product_db[3] = [title, price, img] 

    print(productLink)
