"""Парсинг чарта (топ-100 песен) Яндекс-Музыка"""

import requests

headers = {
    'Accept': 'application/json, text/javascript, */*; q=0.01',
    'Accept-Language': 'ru-RU,ru;q=0.9',
    'Connection': 'keep-alive',
    'Referer': 'https://music.yandex.by/chart',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-origin',
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/'
                  '108.0.0.0 Safari/537.36',
    'X-Requested-With': 'XMLHttpRequest',
    'X-Retpath-Y': 'https://music.yandex.by/chart',
    'sec-ch-ua': '"Not?A_Brand";v="8", "Chromium";v="108", "Google Chrome";v="108"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Linux"',
}

params = {
    'what': 'chart',
    'lang': 'ru',
    'external-domain': 'music.yandex.by',
    'overembed': 'false',
    'ncrnd': '0.9667599766179826',
}

response = requests.get('https://music.yandex.by/handlers/main.jsx', params=params, headers=headers)

for track in response.json()['chartPositions']:
    position = track['chartPosition']['position']
    title = track['track']['title']
    author = track['track']['artists'][0]['name']
    artist = [artist['name'] for artist in track['track']['artists']]
    authors = ', '.join(artist)

    """Вывод результата"""
    print(f"N-{position} - {title} - {authors}")
