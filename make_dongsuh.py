import requests
from bs4 import BeautifulSoup
from pymongo import MongoClient           # pymongo를 임포트 하기(패키지 인스톨 먼저 해야겠죠?)
client = MongoClient('localhost', 27017)  # mongoDB는 27017 포트로 돌아갑니다.
db = client.dbikea


dongsuh_sofa = {
    '4인' : 'http://www.dongsuhfurniture.co.kr/goods/goods_list.php?cateCd=001002',
    '2,3인': 'http://www.dongsuhfurniture.co.kr/goods/goods_list.php?cateCd=001003',
    '1인': 'http://www.dongsuhfurniture.co.kr/goods/goods_list.php?cateCd=001004',
    '소파베드': 'http://www.dongsuhfurniture.co.kr/goods/goods_list.php?cateCd=001006'
}
dongsuh_chair = {
    '중역용의자' : 'http://www.dongsuhfurniture.co.kr/goods/goods_list.php?page=1&cateCd=022003001',
    '사무용의자' : 'http://www.dongsuhfurniture.co.kr/goods/goods_list.php?page=2&cateCd=022003002',
    '회의용의자' :'http://www.dongsuhfurniture.co.kr/goods/goods_list.php?cateCd=022003003',
    '학생용의자' :'http://www.dongsuhfurniture.co.kr/goods/goods_list.php?cateCd=022003004',
    '스툴형의자' :'http://www.dongsuhfurniture.co.kr/goods/goods_list.php?cateCd=022003005',
    '오피스의자' : 'http://www.dongsuhfurniture.co.kr/goods/goods_list.php?cateCd=022003006',
}

dongsuh_desk = {
    '소파테이블' : 'http://www.dongsuhfurniture.co.kr/goods/goods_list.php?cateCd=001007',
    '1인책상' :'http://www.dongsuhfurniture.co.kr/goods/goods_list.php?cateCd=022001001',
    '2인책상' : 'http://www.dongsuhfurniture.co.kr/goods/goods_list.php?cateCd=022001002',
    'H형책상' : 'http://www.dongsuhfurniture.co.kr/goods/goods_list.php?cateCd=022001003',
    '오피스책상': 'http://www.dongsuhfurniture.co.kr/goods/goods_list.php?cateCd=022001009',
    '철제책상' : 'http://www.dongsuhfurniture.co.kr/goods/goods_list.php?cateCd=022001008'
}


dong_suh_img = 'http://www.dongsuhfurniture.co.kr'
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
            type_ = i
            a_href = sofa.select_one('div.item_cont')
            if a_href is not None:
                href = a_href.select_one('div.item_photo_box > a')['href']
                # print(href)
                # print(sofa)
                href.lstrip('.')
                real_href = dong_suh_img + href
                name1 = a_href.select_one('div.item_photo_box > a > img')['title']

                img_url = a_href.select_one('div.item_photo_box')['data-image-magnify']
                real_img_url = dong_suh_img + img_url

                price = a_href.select_one('div.item_info_cont > div.item_money_box > strong.item_price > span').text.strip()

                print(name1)
                print(price)
                print(real_href)
                print(real_img_url)

                doc = {
                    'brand': '동서가구',
                    'type': type_,
                    'name': name1,
                    'price': price,
                    'url': href,
                    'img': img_url
                }

                db.sofas.insert_one(doc)

def make_dongsuh_chair():
    for i,j in dongsuh_chair.items():

        # URL을 읽어서 HTML를 받아오고,
        headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
        data = requests.get(j ,headers=headers)

        # HTML을 BeautifulSoup이라는 라이브러리를 활용해 검색하기 용이한 상태로 만듦
        soup = BeautifulSoup(data.text, 'html.parser')

        # select를 이용해서, tr들을 불러오기
        sofas = soup.select('div.content > div.goods_list_item > div.goods_list > div.goods_list_cont > div.item_gallery_type > ul > li')

        type_ = i
        for sofa in sofas:
            
            a_href = sofa.select_one('div.item_cont')
            if a_href is not None:
                href = a_href.select_one('div.item_photo_box > a')['href']
                # print(href)
                # print(sofa)
                href.replace(".","",2)
                real_href = dong_suh_img + href
                name1 = a_href.select_one('div.item_photo_box > a > img')['title']

                img_url = a_href.select_one('div.item_photo_box')['data-image-magnify']
                real_img_url = dong_suh_img + img_url

                price = a_href.select_one('div.item_info_cont > div.item_money_box > strong.item_price > span').text.strip()

                print(name1)
                print(price)
                print(real_href)
                print(real_img_url)

                doc = {
                    'brand': '동서가구',
                    'type': type_,
                    'name': name1,
                    'price': price,
                    'url': href,
                    'img': img_url
                }


                db.chairs.insert_one(doc)

def make_dongsuh_desk():
    for i,j in dongsuh_desk.items():

        # URL을 읽어서 HTML를 받아오고,
        headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
        data = requests.get(j ,headers=headers)

        # HTML을 BeautifulSoup이라는 라이브러리를 활용해 검색하기 용이한 상태로 만듦
        soup = BeautifulSoup(data.text, 'html.parser')

        # select를 이용해서, tr들을 불러오기
        sofas = soup.select('div.content > div.goods_list_item > div.goods_list > div.goods_list_cont > div.item_gallery_type > ul > li')

        type_ = i
        for sofa in sofas:
            
            a_href = sofa.select_one('div.item_cont')
            if a_href is not None:
                href = a_href.select_one('div.item_photo_box > a')['href']
                # print(href)
                # print(sofa)
                href.lstrip('.')
                real_href = dong_suh_img + href
                name1 = a_href.select_one('div.item_photo_box > a > img')['title']

                img_url = a_href.select_one('div.item_photo_box')['data-image-magnify']
                real_img_url = dong_suh_img + img_url

                price = a_href.select_one('div.item_info_cont > div.item_money_box > strong.item_price > span').text.strip()

                print(name1)
                print(price)
                print(real_href)
                print(real_img_url)

                doc = {
                    'brand': '동서가구',
                    'type': type_,
                    'name': name1,
                    'price': price,
                    'url': href,
                    'img': img_url
                }

                db.desks.insert_one(doc)


# def make_dongsuh():
#     make_dongsuh_sofa()
#     print('*'*70)
#     make_dongsuh_chair()
#     print('*'*70)
#     make_dongsuh_desk()



db.sofas.drop()
make_dongsuh_chair()