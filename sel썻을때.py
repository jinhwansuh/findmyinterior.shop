import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
driver = webdriver.Chrome('C:\\Users\\nick0\\Desktop\\chromedriver')
import time



ikea_url = 'https://www.ikea.com/kr/ko/'
# chair_url = 'https://www.ikea.com/kr/ko/cat/chairs-fu002/' # 의자를 선택하면 뒤에 cat/chairs-fu002/
# sofa_url = 'https://www.ikea.com/kr/ko/cat/all-sofas-39130/' #sofa를 선택하면 cat/all-sofas-39130/

''''' 소파를 선택하면 아래 저장된 sofa_url_dict 에 있는 링크들이 실행이 되게 할수 있게.
        의자를 선택하면 역시 chair_url_dict가 실행되게.
    or 색상이라는 링크를 들어가서 자동으로 크롤링 하기.'''

color_dict = {'예시 링크 화이트' : 'https://www.ikea.com/kr/ko/cat/chairs-fu002/?filters=color%3A%ED%99%94%EC%9D%B4%ED%8A%B8%2410156',
    'gray': '%2410028',
    'beige': '%2410003',
    'black': '%2410139',
    'brown': '%2410019',
    'white': '%2410156',
    'Green': '%2410033',
    'Blue': '%2410007',
    'Red': '%2410124',
    'Multi-color': '%2410583',
    'Pink': '%2410119',
    'Emerald': '%2410152'
}


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
# 페이지 추가하기기  https://www.ikea.com/kr/ko/cat/all-sofas-39130/?filters=color%3A%EA%B7%B8%EB%A0%88%EC%9D%B4%2410028&page=1                     &page=1 &page=1 &page=1 &page=1

   # URL을 읽어서 HTML를 받아오고,
for i,j in sofa_url_dict.items():
    driver.get(j)
    driver.implicitly_wait(1)
    time.sleep(3)
    req = driver.page_source

    # headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
    # data = requests.get( j  ,headers=headers)


    color = i
    # HTML을 BeautifulSoup이라는 라이브러리를 활용해 검색하기 용이한 상태로 만듦
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
            print(name)
            print(price)
            print(href)
            print(img_url)
    print('*'*80)
