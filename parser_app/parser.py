import requests
from bs4 import BeautifulSoup
from django.views.decorators.csrf import csrf_exempt

HOST = "https://jut.su/"
URL = "https://jut.su/anime/2022/"

HEADERS = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.102 Safari/537.36',
}


@csrf_exempt
def get_html(url, params=''):
    req = requests.get(url,headers=HEADERS, params=params)
    return req

@csrf_exempt
def get_data(html):
    soup = BeautifulSoup(html, 'html.parser')
    items = soup.find_all('div', class_="all_anime")
    anime = []

    for item in items:
        anime.append(
            {
                'title': item.find('div', class_='aaname').get_text(),
                'image': HOST + item.find('div',class_='all_anime_image').find('img').get('src')

            }
        )
    return anime

@csrf_exempt
def parser_func():
    html = get_html(URL)
    if html.status_code == 200:
        anime = []
        for page in range(0, 1):
            html = get_html(URL, params={'page': page})
            anime.extend(get_data(html.text))
            return anime
    else:
        raise ValueError("Error maybe permission denies")
