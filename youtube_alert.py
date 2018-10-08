from bs4 import BeautifulSoup

from settings import WEBHOOK_URL

import requests
import time
import sys

temp_subscriber = 0


def get_subscriber(url):
    targetUrl = url
    html = requests.get(targetUrl).text
    soupData = BeautifulSoup(html, 'html.parser')
    data = soupData.find('span', attrs={'class': 'yt-subscription-button-subscriber-count-branded-horizontal subscribed yt-uix-tooltip'})

    subscriber = str(data)[str(data).find('">') + 2: str(data).find('</s')]

    return int(subscriber)


def check_subscriber(now_subscriber):
    global temp_subscriber

    if temp_subscriber > now_subscriber:
        temp_subscriber = now_subscriber
        requests.post(WEBHOOK_URL, data={'content': '누군가 구독버튼을 두번 누른거같군..'})
        requests.post(WEBHOOK_URL, data={'content': '현재 구독자수 {}명'.format(temp_subscriber)})

    elif temp_subscriber < now_subscriber:
        temp_subscriber = now_subscriber
        requests.post(WEBHOOK_URL, data={'content': '구독자가 한명늘었네! 오케이 사딸라!'})
        requests.post(WEBHOOK_URL, data={'content': '현재 구독자수 {}명'.format(temp_subscriber)})


def main():
    print('Started bot...')

    global temp_subscriber

    url = sys.argv[1]
    subscriber = get_subscriber(url)
    temp_subscriber = subscriber
    requests.post(WEBHOOK_URL, data={'content': '현재 구독자수 {}명'.format(subscriber)})

    while True:
        check_subscriber(get_subscriber(url))
        time.sleep(10)


if __name__ == "__main__":
    main()
