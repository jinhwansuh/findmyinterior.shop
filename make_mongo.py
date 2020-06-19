import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

options = webdriver.ChromeOptions()
options.add_argument('headless')
options.add_argument("--disable-gpu")
options.add_argument("lang=ko_KR")
driver = webdriver.Chrome('home\\ubuntu\\class\\chromedriver', chrome_options= options)
import time             
import random


from pymongo import MongoClient           # pymongo를 임포트 하기(패키지 인스톨 먼저 해야겠죠?)
client = MongoClient('mongodb://test123:test123@54.180.94.114', 27017)  # mongoDB는 27017 포트로 돌아갑니다.
db = client.dbikea


# 이케아 만들기


ikea_sofa = {
    'grey': 'https://www.ikea.com/kr/ko/cat/all-sofas-39130/?filters=color%3A%EA%B7%B8%EB%A0%88%EC%9D%B4%2410028',
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
                    'homepage': '이케아(Ikea)',
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
                    'homepage': '이케아(Ikea)',
                    'brand': name1,
                    'color': color,
                    'name': name,
                    'price': price,
                    'url': href,
                    'img': img_url,
                    'like': 0
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
                    'homepage': '이케아(Ikea)',
                    'brand': name1,
                    'color': color,
                    'name': name,
                    'price': price,
                    'url': href,
                    'img': img_url,
                    'like': 0
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

# 동서가구 만들기
dongsuh_sofa = {
    '4인': 'http://www.dongsuhfurniture.co.kr/goods/goods_list.php?cateCd=001002',
    '2,3인': 'http://www.dongsuhfurniture.co.kr/goods/goods_list.php?cateCd=001003',
    '1인': 'http://www.dongsuhfurniture.co.kr/goods/goods_list.php?cateCd=001004',
    '소파베드': 'http://www.dongsuhfurniture.co.kr/goods/goods_list.php?cateCd=001006'
}
dongsuh_chair = {
    '중역용의자': 'http://www.dongsuhfurniture.co.kr/goods/goods_list.php?page=1&cateCd=022003001',
    '사무용의자': 'http://www.dongsuhfurniture.co.kr/goods/goods_list.php?page=2&cateCd=022003002',
    '회의용의자': 'http://www.dongsuhfurniture.co.kr/goods/goods_list.php?cateCd=022003003',
    '학생용의자': 'http://www.dongsuhfurniture.co.kr/goods/goods_list.php?cateCd=022003004',
    '스툴형의자': 'http://www.dongsuhfurniture.co.kr/goods/goods_list.php?cateCd=022003005',
    '오피스의자': 'http://www.dongsuhfurniture.co.kr/goods/goods_list.php?cateCd=022003006',
}

dongsuh_desk = {
    '소파테이블': 'http://www.dongsuhfurniture.co.kr/goods/goods_list.php?cateCd=001007',
    '1인책상': 'http://www.dongsuhfurniture.co.kr/goods/goods_list.php?cateCd=022001001',
    '2인책상': 'http://www.dongsuhfurniture.co.kr/goods/goods_list.php?cateCd=022001002',
    'H형책상': 'http://www.dongsuhfurniture.co.kr/goods/goods_list.php?cateCd=022001003',
    '오피스책상': 'http://www.dongsuhfurniture.co.kr/goods/goods_list.php?cateCd=022001009',
    '철제책상': 'http://www.dongsuhfurniture.co.kr/goods/goods_list.php?cateCd=022001008'
}

dong_suh_img = 'http://www.dongsuhfurniture.co.kr'


def make_dongsuh_sofa():
    for i, j in dongsuh_sofa.items():

        # URL을 읽어서 HTML를 받아오고,
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
        data = requests.get(j, headers=headers)

        # HTML을 BeautifulSoup이라는 라이브러리를 활용해 검색하기 용이한 상태로 만듦
        soup = BeautifulSoup(data.text, 'html.parser')

        # select를 이용해서, tr들을 불러오기
        sofas = soup.select(
            'div.content > div.goods_list_item > div.goods_list > div.goods_list_cont > div.item_gallery_type > ul > li')

        for sofa in sofas:
            type_ = i
            a_href = sofa.select_one('div.item_cont')
            if a_href is not None:
                href = a_href.select_one('div.item_photo_box > a')['href']
                # print(href)
                # print(sofa)
                real_href = dong_suh_img + href
                name1 = a_href.select_one('div.item_photo_box > a > img')['title']

                img_url = a_href.select_one('div.item_photo_box')['data-image-magnify']
                real_img_url = dong_suh_img + img_url

                price = a_href.select_one(
                    'div.item_info_cont > div.item_money_box > strong.item_price > span').text.strip()

                print(name1)
                print(price)
                print(real_href)
                print(real_img_url)

                doc = {
                    'brand': '동서가구',
                    'type': type_,
                    'name': name1,
                    'price': price,
                    'url': real_href,
                    'img': real_img_url,
                    'like': 0
                }

                db.sofas.insert_one(doc)


def make_dongsuh_chair():
    for i, j in dongsuh_chair.items():

        # URL을 읽어서 HTML를 받아오고,
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
        data = requests.get(j, headers=headers)

        # HTML을 BeautifulSoup이라는 라이브러리를 활용해 검색하기 용이한 상태로 만듦
        soup = BeautifulSoup(data.text, 'html.parser')

        # select를 이용해서, tr들을 불러오기
        sofas = soup.select(
            'div.content > div.goods_list_item > div.goods_list > div.goods_list_cont > div.item_gallery_type > ul > li')

        type_ = i
        for sofa in sofas:

            a_href = sofa.select_one('div.item_cont')
            if a_href is not None:
                href = a_href.select_one('div.item_photo_box > a')['href']
                # print(href)
                # print(sofa)

                real_href = dong_suh_img + href
                name1 = a_href.select_one('div.item_photo_box > a > img')['title']

                img_url = a_href.select_one('div.item_photo_box')['data-image-magnify']
                real_img_url = dong_suh_img + img_url

                price = a_href.select_one(
                    'div.item_info_cont > div.item_money_box > strong.item_price > span').text.strip()

                print(name1)
                print(price)
                print(real_href)
                print(real_img_url)

                doc = {
                    'brand': '동서가구',
                    'type': type_,
                    'name': name1,
                    'price': price,
                    'url': real_href,
                    'img': real_img_url,
                    'like': 0
                }

                db.chairs.insert_one(doc)


def make_dongsuh_desk():
    for i, j in dongsuh_desk.items():

        # URL을 읽어서 HTML를 받아오고,
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
        data = requests.get(j, headers=headers)

        # HTML을 BeautifulSoup이라는 라이브러리를 활용해 검색하기 용이한 상태로 만듦
        soup = BeautifulSoup(data.text, 'html.parser')

        # select를 이용해서, tr들을 불러오기
        sofas = soup.select(
            'div.content > div.goods_list_item > div.goods_list > div.goods_list_cont > div.item_gallery_type > ul > li')

        type_ = i
        for sofa in sofas:

            a_href = sofa.select_one('div.item_cont')
            if a_href is not None:
                href = a_href.select_one('div.item_photo_box > a')['href']
                # print(href)
                # print(sofa)
                real_href = dong_suh_img + href
                name1 = a_href.select_one('div.item_photo_box > a > img')['title']

                img_url = a_href.select_one('div.item_photo_box')['data-image-magnify']
                real_img_url = dong_suh_img + img_url

                price = a_href.select_one(
                    'div.item_info_cont > div.item_money_box > strong.item_price > span').text.strip()

                print(name1)
                print(price)
                print(real_href)
                print(real_img_url)

                doc = {
                    'brand': '동서가구',
                    'type': type_,
                    'name': name1,
                    'price': price,
                    'url': real_href,
                    'img': real_img_url,
                    'like': 0
                }

                db.desks.insert_one(doc)


def make_dongsuh():
    make_dongsuh_sofa()
    print('*' * 70)
    make_dongsuh_chair()
    print('*' * 70)
    make_dongsuh_desk()

# 오늘의집 만들기


ounul_sofa = {
    '일반소파': 'https://ohou.se/store/category?category=0_1_0_3',
    '빈백소파': 'https://ohou.se/store/category?category=0_1_0_4',
    '좌식소파': 'https://ohou.se/store/category?category=0_1_0_5',
    '소파베드': 'https://ohou.se/store/category?category=0_1_0_6',
    '소파스툴': 'https://ohou.se/store/category?category=0_1_0_7'

}
ounul_chair = {
    '일반의자': 'https://ohou.se/store/category?category=0_1_11_0',
    '좌식의자': 'https://ohou.se/store/category?category=0_1_11_1',
    '안락의자': 'https://ohou.se/store/category?category=0_1_11_2'
}
ounul_desk = {
    '일반형책상(일자형)': 'https://ohou.se/store/category?category=0_5_1_4',
    '코너형책상(L자형)': 'https://ohou.se/store/category?category=0_5_1_0',
    '컴퓨터형책상(H형)': 'https://ohou.se/store/category?category=0_5_1_1',
    '좌식책상': 'https://ohou.se/store/category?category=0_5_1_2',
    '스탠딩책상': 'https://ohou.se/store/category?category=0_5_1_3'
}
ounul_img = 'https://ohou.se'


def make_ounul_sofa():
    for i, j in ounul_sofa.items():
        type_ = i
        driver.get(j)
        time.sleep(1)
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
                price = a_href.select_one(
                    'div.production-item__content > span.production-item-price > span.production-item-price__price').text.strip()
                print(brand)
                print(name)
                print(price)
                print(href)
                print(img_url)

                # ##### DB에 추가하기,
                doc = {
                    'homepage': '오늘의집',
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
    for i, j in ounul_chair.items():
        type_ = i
        driver.get(j)
        time.sleep(1)
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
                price = a_href.select_one(
                    'div.production-item__content > span.production-item-price > span.production-item-price__price').text.strip()
                print(brand)
                print(name)
                print(price)
                print(href)
                print(img_url)

                # ##### DB에 추가하기,
                doc = {
                    'homepage': '오늘의집',
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
    for i, j in ounul_desk.items():
        type_ = i
        driver.get(j)
        time.sleep(1)
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
                price = a_href.select_one(
                    'div.production-item__content > span.production-item-price > span.production-item-price__price').text.strip()
                print(brand)
                print(name)
                print(price)
                print(href)
                print(img_url)

                # ##### DB에 추가하기,
                doc = {
                    'homepage': '오늘의집',
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



def make_ounul():
    make_ounul_sofa()
    print('*' * 80)
    make_ounul_chair()
    print('*' * 80)
    make_ounul_desk()
    print('*' * 80)

def drop_all():
    db.sofas.drop()
    db.chairs.drop()
    db.desks.drop()

def make_all():

    make_ikea()
    # make_dongsuh()
    make_ounul()

drop_all()
make_all()
