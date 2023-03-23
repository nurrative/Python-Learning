import requests,re
from bs4 import BeautifulSoup as BS
from typing import List


class BaseParser:
    BASE_URL:str 
    query_param: str = 'q'

    @staticmethod
    def get_soup(url: str)->BS:
        html = requests.get(url).text
        return BS(html, 'lxml')
    
    @staticmethod
    def format_title(title:str)->str:
        return " ".join(title.replace("\r", "").replace("\t", "").split())
    
    @staticmethod
    def format_price(price:str)->str:
        return int(re.search('\d+',price).group(0))
    
    def search(self,query:str)->list[dict]:
        "принимает поисковое слово и возвращает список со всеми результатами"
        return self.get_products(f"{self.BASE_URL}?{self.query_param}={query}")
    
    def get_products(self, url:str) -> list[dict]:
        soup = self.get_soup(url)
        products = self._get_products_list(soup)
        results=[]
        for product in products:
            product_info = self._get_product_info(product)
            results.append(product_info)
        return results

    def _get_products_list(self,soup:BS)->list[BS]:
        "метод в котором ищутся все блоки с продуктами"
        raise NotImplementedError
    
    def _get_product_info(self,soup:BS)->dict:
        'метод в котором ищется title и price продукта'
        raise NotImplementedError



class KivanoParser(BaseParser):
    BASE_URL = "https://www.kivano.kg/product/index"
    query_param='search'

    def _get_products_list(self, soup: BS) -> list[BS]:
        return soup.find_all('div',{'class':'product_listbox'})

    def _get_product_info(self, soup: BS) -> dict:
        title = soup.find('div',{'class':'listbox_title'}).text
        price = soup.find('div',{'class':'listbox_price'}).text
        return {'title':self.format_title(title),'price':self.format_price(price)}

# print(KivanoParser().search('пароварка'))

class KulikovParser(BaseParser):
    BASE_URL = "https://site.kulikov.com/katalog"

    def _get_products_list(self, soup: BS) -> List[BS]:
        return soup.find_all("div", {"class":"product-item"})
    
    def _get_product_info(self, soup: BS) -> dict:
        title = soup.find("h3", {"class":"product-item-title"}).text
        price = soup.find("span", {"class":"product-item-price-current"}).text
        return {"title":self.format_title(title),'price':self.format_price(price)}


print(KivanoParser().search("пароварка"))
print(KulikovParser().search("торт"))
