# 구독자 알림 봇 ( Subscribers Alert Bot ) by discord

### requirements

- use python 3.5

- bs4
- requests



### development

#### 1.YouTube subscribers notification bot

> ##### Started...
>- git clone https://github.com/sprumin/SubscriberAlert.git
>- cd SubscriberAlert
>- echo WEBHOOK_URL="yourdiscordwebhookurl" >> settings.py
>  > 디스코드 채널 접속 -> 서버설정 -> 웹훅 생성 -> url 복사 후 위 양식에 맞게 붙여넣기
>- python youtube_alert.py "YoutubeLink"
>  > ex) python youtube_alert.py https://www.youtube.com/channel/UCwqRPb8q7M6c1YHuBNDkR0w
>- check your discord channel

> ##### Info...
>- python 으로 크롤링 공부를 하던 도중 게임 영상으로 유튜브를 하는 친구의 구독자수를 실시간으로 확인할 수 있는 방법이 뭐가 있을까 해서 만들게된 프로그램
>- 그렇다 저 위에 예제 url은 "그 친구"의 유튜브 주소다. ( 좋아요 구독하기 눌러주세요 핳 )
>- 사실 카톡으로 하면 어떨까 했지만 discord 지박령들이라 discord가 차라리 낫다고 판단함
>- youtube api(있는지 확인 안해봄)를 사용하지않았다. 크롤링 공부하는김에 만든 거다보니..
>- 방법은 단순하다 url을 입력하면 파싱한 데이터값을 10초마다 비교해서 값을 리턴한다
>- 참고로 저 봇 프로필사진이 "김두X" 님이다
>- 프로그램을 실행할때를 포함 구독자가 늘어나거나 줄어들면 아래와 같은 모습을 볼 수 있다.
>![png](https://user-images.githubusercontent.com/23535108/46600319-c2aa4500-cb24-11e8-8e6d-19eb027a43f9.PNG)


developer sprumin / " sprumin@gmail.com "




