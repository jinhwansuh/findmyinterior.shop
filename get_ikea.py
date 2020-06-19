import requests
from bs4 import BeautifulSoup

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


for l in range(1, 5):
    # URL을 읽어서 HTML를 받아오고,
    headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
    data = requests.get('https://www.ikea.com/kr/ko/cat/all-sofas-39130/?page={}'.format(l),headers=headers)

    # HTML을 BeautifulSoup이라는 라이브러리를 활용해 검색하기 용이한 상태로 만듦
    soup = BeautifulSoup(data.text, 'html.parser')

    # select를 이용해서, tr들을 불러오기
    sofas = soup.select('div.range-product-list__products > div')
    # print(sofas)
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
            print(name)
            print(price)
            print(href)
            print(img_url)
            print(l)
    print('*'*70)



    # # div.catalog-product-list__fragment > div.product-compact > div.product-compact__spacer >
    # name1 = sofas.select_one('span.product-compact__name').text
    # name2 = sofas.select_one('span.product-compact__type').text
    #
    # name = name1 + name2
    # img_url = sofas.select_one('div.product-compact__image-container > div.product-compact__image > div.range-image-claim-height > img')['src']
    # price = sofas.select_one('span.product-compact__price__value').text
    #
    #
    # # doc = {
    # #     'name': '엄청 편한 소파 ',
    # #     'price': 50000,
    # #     'color': 'black'
    # # }
    #
    #
    # print(name)
    # print(img_url)
    # print(price)