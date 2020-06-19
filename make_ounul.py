import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
driver = webdriver.Chrome('C:\\Users\\nick0\\Desktop\\chromedriver')
import time
import random


from pymongo import MongoClient           # pymongo를 임포트 하기(패키지 인스톨 먼저 해야겠죠?)
client = MongoClient('localhost', 27017)  # mongoDB는 27017 포트로 돌아갑니다.
db = client.dbikea



ounul_sofa = {
    '일반소파' : 'https://ohou.se/store/category?category=0_1_0_3',
    '빈백소파' : 'https://ohou.se/store/category?category=0_1_0_4',
    '좌식소파' : 'https://ohou.se/store/category?category=0_1_0_5',
    '소파베드' : 'https://ohou.se/store/category?category=0_1_0_6',
    '소파스툴' : 'https://ohou.se/store/category?category=0_1_0_7'


}
ounul_chair = {
'일반의자' : 'https://ohou.se/store/category?category=0_1_11_0',
'좌식의자' : 'https://ohou.se/store/category?category=0_1_11_1',
'안락의자' : 'https://ohou.se/store/category?category=0_1_11_2'
}
ounul_desk = {
    '일반형책상(일자형)' : 'https://ohou.se/store/category?category=0_5_1_4',
    '코너형책상(L자형)' : 'https://ohou.se/store/category?category=0_5_1_0',
    '컴퓨터형책상(H형)' : 'https://ohou.se/store/category?category=0_5_1_1',
    '좌식책상' : 'https://ohou.se/store/category?category=0_5_1_2',
    '스탠딩책상' : 'https://ohou.se/store/category?category=0_5_1_3'
}
ounul_img = 'https://ohou.se'
def make_ounul_sofa():
    for i, j in ounul_sofa.items():
        type_ = i
        driver.get(j)
        for i in range(7):
            driver.find_element_by_tag_name('body').send_keys(Keys.END)
            driver.implicitly_wait(10)
            time.sleep(5)

        req = driver.page_source
        soup = BeautifulSoup(req, 'html.parser')

        # select를 이용해서, tr들을 불러오기
        sofas = soup.select('div.virtualized-list > div ')

        for sofa in sofas:
            a_href = sofa.select_one('article.production-item')
            if a_href is not None:
                href = ounul_img + a_href.select_one('a')['href']


                real_href = ounul_img + href
                name1 = a_href.select_one('div.production-item__content > h1 ')
                brand = name1.select_one('span.production-item__header__brand').text
                name = name1.select_one('span.production-item__header__name').text

                if a_href.select_one('div.production-item__image > img') is None:
                    continue

                img_url = a_href.select_one('div.production-item__image > img')['src']
                price = a_href.select_one('div.production-item__content > span.production-item-price > span.production-item-price__price').text.strip()
                print(brand)
                print(name)
                print(price)
                print(href)
                print(img_url)

                # ##### DB에 추가하기,
                doc = {
                    'brand': brand,
                    'type': type_,
                    'name': name,
                    'price': price,
                    'url': href,
                    'img': img_url,
                    'like': 0
                }
                db.sofas.insert_one(doc)
        print('*' * 80)

def make_ounul_chair(): 
    for i,j in ounul_chair.items():
        type_ = i
        driver.get(j)
        for i in range(7):
            driver.find_element_by_tag_name('body').send_keys(Keys.END)
            driver.implicitly_wait(10)
            time.sleep(5)

        req = driver.page_source
        soup = BeautifulSoup(req, 'html.parser')

        # select를 이용해서, tr들을 불러오기
        sofas = soup.select('div.virtualized-list > div ')

        for sofa in sofas:
            a_href = sofa.select_one('article.production-item')
            if a_href is not None:
                href = ounul_img + a_href.select_one('a')['href']


                real_href = ounul_img + href
                name1 = a_href.select_one('div.production-item__content > h1 ')
                brand = name1.select_one('span.production-item__header__brand').text
                name = name1.select_one('span.production-item__header__name').text

                if a_href.select_one('div.production-item__image > img') is None:
                    continue

                img_url = a_href.select_one('div.production-item__image > img')['src']
                price = a_href.select_one('div.production-item__content > span.production-item-price > span.production-item-price__price').text.strip()
                print(brand)
                print(name)
                print(price)
                print(href)
                print(img_url)

                # ##### DB에 추가하기,
                doc = {
                    'brand': brand,
                    'type': type_,
                    'name': name,
                    'price': price,
                    'url': href,
                    'img': img_url,
                    'like': 0
                }
                db.chairs.insert_one(doc)
        print('*' * 80)

def make_ounul_desk(): 
    for i,j in ounul_desk.items():
        type_ = i
        driver.get(j)
        for i in range(7):
            driver.find_element_by_tag_name('body').send_keys(Keys.END)
            driver.implicitly_wait(10)
            time.sleep(5)

        req = driver.page_source
        soup = BeautifulSoup(req, 'html.parser')

        # select를 이용해서, tr들을 불러오기
        sofas = soup.select('div.virtualized-list > div ')

        for sofa in sofas:
            a_href = sofa.select_one('article.production-item')
            if a_href is not None:
                href = ounul_img + a_href.select_one('a')['href']


                real_href = ounul_img + href
                name1 = a_href.select_one('div.production-item__content > h1 ')
                brand = name1.select_one('span.production-item__header__brand').text
                name = name1.select_one('span.production-item__header__name').text

                if a_href.select_one('div.production-item__image > img') is None:
                    continue

                img_url = a_href.select_one('div.production-item__image > img')['src']
                price = a_href.select_one('div.production-item__content > span.production-item-price > span.production-item-price__price').text.strip()
                print(brand)
                print(name)
                print(price)
                print(href)
                print(img_url)

                # ##### DB에 추가하기,
                doc = {
                    'brand': brand,
                    'type': type_,
                    'name': name,
                    'price': price,
                    'url': href,
                    'img': img_url,
                    'like': 0
                }
                db.desks.insert_one(doc)
        print('*' * 80)



# 기존 sofas 콜렉션을 삭제하고, 출처 url들을 가져온 후, 크롤링하여 DB에 저장합니다.
def make_ounul():
      
    make_ounul_sofa()
    print('*'*80)
    make_ounul_chair()
    print('*'*80)
    make_ounul_desk()
    print('*'*80)


make_ounul()

