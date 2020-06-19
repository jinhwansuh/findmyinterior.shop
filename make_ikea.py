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

ikea_sofa = {
    'gray': 'https://www.ikea.com/kr/ko/cat/all-sofas-39130/?filters=color%3A%EA%B7%B8%EB%A0%88%EC%9D%B4%2410028',
    'beige': 'https://www.ikea.com/kr/ko/cat/all-sofas-39130/?filters=color%3A%EB%B2%A0%EC%9D%B4%EC%A7%80%2410003',
    'black': 'https://www.ikea.com/kr/ko/cat/all-sofas-39130/?filters=color%3A%EB%B8%94%EB%9E%99%2410139',
    'brown': 'https://www.ikea.com/kr/ko/cat/all-sofas-39130/?filters=color%3A%EB%B8%8C%EB%9D%BC%EC%9A%B4%2410019',
    'white': 'https://www.ikea.com/kr/ko/cat/all-sofas-39130/?filters=color%3A%ED%99%94%EC%9D%B4%ED%8A%B8%2410156',
    'Green': 'https://www.ikea.com/kr/ko/cat/all-sofas-39130/?filters=color%3A%EA%B7%B8%EB%A6%B0%2410033',
    'Blue': 'https://www.ikea.com/kr/ko/cat/all-sofas-39130/?filters=color%3A%EB%B8%94%EB%A3%A8%2410007',
    'Red': 'https://www.ikea.com/kr/ko/cat/all-sofas-39130/?filters=color%3A%EB%A0%88%EB%93%9C%2410124',
    'Multi-color': 'https://www.ikea.com/kr/ko/cat/all-sofas-39130/?filters=color%3A%EB%A9%80%ED%8B%B0%EC%BB%AC%EB%9F%AC%2410583',
    'Pink': 'https://www.ikea.com/kr/ko/cat/all-sofas-39130/?filters=color%3A%ED%95%91%ED%81%AC%2410119',
    'Emerald': 'https://www.ikea.com/kr/ko/cat/all-sofas-39130/?filters=color%3A%ED%84%B0%EC%BF%BC%EC%9D%B4%EC%A6%88%2410152'
}
ikea_chair = {
    'white': 'https://www.ikea.com/kr/ko/cat/chairs-fu002/?filters=color%3A%ED%99%94%EC%9D%B4%ED%8A%B8%2410156',
    'black': 'https://www.ikea.com/kr/ko/cat/chairs-fu002/?filters=color%3A%EB%B8%94%EB%9E%99%2410139',
    'grey': 'https://www.ikea.com/kr/ko/cat/chairs-fu002/?filters=color%3A%EA%B7%B8%EB%A0%88%EC%9D%B4%2410028',
    'beige': 'https://www.ikea.com/kr/ko/cat/chairs-fu002/?filters=color%3A%EB%B2%A0%EC%9D%B4%EC%A7%80%2410003',
    'brown': 'https://www.ikea.com/kr/ko/cat/chairs-fu002/?filters=color%3A%EB%B8%8C%EB%9D%BC%EC%9A%B4%2410019',
    'blue': 'https://www.ikea.com/kr/ko/cat/chairs-fu002/?filters=color%3A%EB%B8%94%EB%A3%A8%2410007',
    'green': 'https://www.ikea.com/kr/ko/cat/chairs-fu002/?filters=color%3A%EA%B7%B8%EB%A6%B0%2410033',
    'pink': 'https://www.ikea.com/kr/ko/cat/chairs-fu002/?filters=color%3A%ED%95%91%ED%81%AC%2410119',
    'red': 'https://www.ikea.com/kr/ko/cat/chairs-fu002/?filters=color%3A%EB%A0%88%EB%93%9C%2410124',
    'yellow': 'https://www.ikea.com/kr/ko/cat/chairs-fu002/?filters=color%3A%EC%98%90%EB%A1%9C%2410042',
    'orange': 'https://www.ikea.com/kr/ko/cat/chairs-fu002/?filters=color%3A%EC%98%A4%EB%A0%8C%EC%A7%80%2410112',
    'turquoise': 'https://www.ikea.com/kr/ko/cat/chairs-fu002/?filters=color%3A%ED%84%B0%EC%BF%BC%EC%9D%B4%EC%A6%88%2410152'
}
ikea_desk = {
    'white': 'https://www.ikea.com/kr/ko/cat/tables-desks-fu004/?filters=color%3A%ED%99%94%EC%9D%B4%ED%8A%B8%2410156',
    'black': 'https://www.ikea.com/kr/ko/cat/tables-desks-fu004/?filters=color%3A%EB%B8%94%EB%9E%99%2410139',
    'beige': 'https://www.ikea.com/kr/ko/cat/tables-desks-fu004/?filters=color%3A%EB%B2%A0%EC%9D%B4%EC%A7%80%2410003',
    'brown': 'https://www.ikea.com/kr/ko/cat/tables-desks-fu004/?filters=color%3A%EB%B8%8C%EB%9D%BC%EC%9A%B4%2410019',
    'grey': 'https://www.ikea.com/kr/ko/cat/tables-desks-fu004/?filters=color%3A%EA%B7%B8%EB%A0%88%EC%9D%B4%2410028',
    'blue': 'https://www.ikea.com/kr/ko/cat/tables-desks-fu004/?filters=color%3A%EB%B8%94%EB%A3%A8%2410007',
    'green': 'https://www.ikea.com/kr/ko/cat/tables-desks-fu004/?filters=color%3A%EA%B7%B8%EB%A6%B0%2410033',
    'red': 'https://www.ikea.com/kr/ko/cat/tables-desks-fu004/?filters=color%3A%EB%A0%88%EB%93%9C%2410124',
    'pink': 'https://www.ikea.com/kr/ko/cat/tables-desks-fu004/?filters=color%3A%ED%95%91%ED%81%AC%2410119',
}

def make_ikea_sofa():
    # URL을 읽어서 HTML를 받아오고, 데이터 가져오기 까지
    for i,j in ikea_sofa.items():

        driver.get(j)
        time.sleep(10)

        color = i
        # HTML을 BeautifulSoup이라는 라이브러리를 활용해 검색하기 용이한 상태로 만듦
        req = driver.page_source
        soup = BeautifulSoup(req, 'html.parser')

        # select를 이용해서, tr들을 불러오기
        chairs = soup.select('div.range-product-list__products > div ')

        for chair in chairs:
            a_href = chair.select_one('div.product-compact > div > a')
            if a_href is not None:
                href = a_href['href']
                # print(href)
                # print(sofa)

                name1 = a_href.select_one('span.product-compact__name').text
                name2 = a_href.select_one('span.product-compact__type').text

                name = name1 + ' ' + name2.strip()
                price = a_href.select_one('span.product-compact__price').text.strip()
                img_url = a_href.select_one('div.product-compact__image-container > div > div > img')['src']
                print(color)
                print(name1)
                print(name)
                print(price)
                print(href)
                print(img_url)

                ##### DB에 추가하기,
                doc = {
                    'brand': name1,
                    'color': color,
                    'name': name,
                    'price': price,
                    'url': href,
                    'img': img_url
                }

                db.sofas.insert_one(doc)
                # 만약 중복된것이 있으면 삭제하기 기능,
                # img 사진이 중복된것이 있다면 삭제하기

        print('*'*80)

def make_ikea_chair():
    # URL을 읽어서 HTML를 받아오고, 데이터 가져오기 까지
    for i,j in ikea_chair.items():

        driver.get(j)
        time.sleep(10)

        color = i
        # HTML을 BeautifulSoup이라는 라이브러리를 활용해 검색하기 용이한 상태로 만듦
        req = driver.page_source
        soup = BeautifulSoup(req, 'html.parser')

        # select를 이용해서, tr들을 불러오기
        chairs = soup.select('div.range-product-list__products > div ')

        for chair in chairs:
            a_href = chair.select_one('div.product-compact > div > a')
            if a_href is not None:
                href = a_href['href']
                # print(href)
                # print(sofa)

                name1 = a_href.select_one('span.product-compact__name').text
                name2 = a_href.select_one('span.product-compact__type').text

                name = name1 + ' ' + name2.strip()
                price = a_href.select_one('span.product-compact__price').text.strip()
                img_url = a_href.select_one('div.product-compact__image-container > div > div > img')['src']
                print(color)
                print(name1)
                print(name)
                print(price)
                print(href)
                print(img_url)

                ##### DB에 추가하기,
                doc = {
                    'brand': name1,
                    'color': color,
                    'name': name,
                    'price': price,
                    'url': href,
                    'img': img_url
                }

                db.chairs.insert_one(doc)
                # 만약 중복된것이 있으면 삭제하기 기능,
                # img 사진이 중복된것이 있다면 삭제하기

        print('*'*80)

def make_ikea_desk():
    # URL을 읽어서 HTML를 받아오고, 데이터 가져오기 까지
    for i,j in ikea_desk.items():

        driver.get(j)
        time.sleep(10)

        color = i
        # HTML을 BeautifulSoup이라는 라이브러리를 활용해 검색하기 용이한 상태로 만듦
        req = driver.page_source
        soup = BeautifulSoup(req, 'html.parser')

        # select를 이용해서, tr들을 불러오기
        chairs = soup.select('div.range-product-list__products > div ')

        for chair in chairs:
            a_href = chair.select_one('div.product-compact > div > a')
            if a_href is not None:
                href = a_href['href']
                # print(href)
                # print(sofa)

                name1 = a_href.select_one('span.product-compact__name').text
                name2 = a_href.select_one('span.product-compact__type').text

                name = name1 + ' ' + name2.strip()
                price = a_href.select_one('span.product-compact__price').text.strip()
                img_url = a_href.select_one('div.product-compact__image-container > div > div > img')['src']
                print(color)
                print(name1)
                print(name)
                print(price)
                print(href)
                print(img_url)

                ##### DB에 추가하기,
                doc = {
                    'brand': name1,
                    'color': color,
                    'name': name,
                    'price': price,
                    'url': href,
                    'img': img_url
                }

                db.desks.insert_one(doc)
                # 만약 중복된것이 있으면 삭제하기 기능,
                # img 사진이 중복된것이 있다면 삭제하기

        print('*'*80)

def make_ikea():
    make_ikea_sofa()
    print('*'*70)
    make_ikea_desk()
    print('*'*70)
    make_ikea_chair()

make_ikea()