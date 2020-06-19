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

ikea_url = 'https://www.ikea.com/kr/ko/'



#동서가구
dongsuh_sofa = {
    '4인' : 'http://www.dongsuhfurniture.co.kr/goods/goods_list.php?cateCd=001002',
    '2,3인': 'http://www.dongsuhfurniture.co.kr/goods/goods_list.php?cateCd=001003',
    '1인': 'http://www.dongsuhfurniture.co.kr/goods/goods_list.php?cateCd=001004',
    '소파베드': 'http://www.dongsuhfurniture.co.kr/goods/goods_list.php?cateCd=001006'
}
dong_suh_img = 'http://www.dongsuhfurniture.co.kr'

#이케아
sofa_url_dict = {
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
chair_url_dict = {
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
desk_url_dict = {
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

#오늘의 집
ounul_sofa = 'https://ohou.se/store/category?category=0_1_0_3'
ounul_img = 'https://ohou.se'

def make_ikea_sofa():
    # URL을 읽어서 HTML를 받아오고, 데이터 가져오기 까지
    for i,j in sofa_url_dict.items():

        driver.get(j)



        time.sleep(15)

        color = i
        # HTML을 BeautifulSoup이라는 라이브러리를 활용해 검색하기 용이한 상태로 만듦
        req = driver.page_source
        soup = BeautifulSoup(req, 'html.parser')

        # select를 이용해서, tr들을 불러오기
        sofas = soup.select('div.range-product-list__products > div ')

        for sofa in sofas:
            a_href = sofa.select_one('div.product-compact > div > a')
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
                    'img': img_url,
                    'like': 0
                }

                db.sofas.insert_one(doc)
                # 만약 중복된것이 있으면 삭제하기 기능,
                # img 사진이 중복된것이 있다면 삭제하기

        print('*'*80)
def make_dongsuh_sofa():
    for i,j in dongsuh_sofa.items():

        # URL을 읽어서 HTML를 받아오고,
        headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
        data = requests.get(j ,headers=headers)

        # HTML을 BeautifulSoup이라는 라이브러리를 활용해 검색하기 용이한 상태로 만듦
        soup = BeautifulSoup(data.text, 'html.parser')

        # select를 이용해서, tr들을 불러오기
        sofas = soup.select('div.content > div.goods_list_item > div.goods_list > div.goods_list_cont > div.item_gallery_type > ul > li')


        for sofa in sofas:
            a_href = sofa.select_one('div.item_cont')
            if a_href is not None:
                href = a_href.select_one('div.item_photo_box > a')['href']
                # print(href)
                # print(sofa)
                real_href = dong_suh_img + href.lstrip('.')
                name1 = a_href.select_one('div.item_photo_box > a > img')['title']

                img_url = a_href.select_one('div.item_photo_box')['data-image-magnify']
                real_img_url = dong_suh_img + img_url

                price = a_href.select_one('div.item_info_cont > div.item_money_box > strong.item_price > span').text.strip()

                print(name1)
                print(price)
                print(real_href)
                print(real_img_url)

                doc = {
                    'brand': 'Dong-suh',
                    'name': name1,
                    'price': price,
                    'url': real_href,
                    'img': real_img_url,
                    'like': 0
                }

                db.sofas.insert_one(doc)
def make_ounul_sofa():
    # URL을 읽어서 HTML를 받아오고, 데이터 가져오기 까지


    driver.get(ounul_sofa)

    # HTML을 BeautifulSoup이라는 라이브러리를 활용해 검색하기 용이한 상태로 만듦


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
                'name': name,
                'price': price,
                'url': href,
                'img': img_url,
                'like': 0
            }

            db.sofas.insert_one(doc)
            # # 만약 중복된것이 있으면 삭제하기 기능,
            # # img 사진이 중복된것이 있다면 삭제하기

    print('*' * 80)






# 기존 sofas 콜렉션을 삭제하고, 출처 url들을 가져온 후, 크롤링하여 DB에 저장합니다.
def insert_all():
      # sofas 콜렉션을 모두 지워줍니다.
    db.sofas.drop()
    make_ikea_sofa()
    make_dongsuh_sofa()
    make_ounul_sofa()


insert_all()




