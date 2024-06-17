# 문제 상황 😪

> 좁고 좁은 저 문으로 들어가는 길은
>
> ...
>
> 익숙해가는 거친 잠자리도
>
> 또 다른 안식을 빚어
>
> 그마저 두려울 뿐인데
>
> ...



그래 나는 익숙해졌다! 그리고 게을러졌다. 무기력하다. 약을 먹어도 어쩔 수 없다.

아침 일찍 일어나는 것... 어떻게 하는 거였지?



그리고... 나 요즘 그저 그런대로 살고 있는 것 같다.

그래서 꺼져가는 불꽃에 휴지 조각 올려놓듯 조심스럽게 아주 작은 프로젝트를 시작해본다. 이 블로그의 첫 프로젝트가 될...



 'Alram for Powerful Morning'이다.



# 해결 절차 ✍

1. 일어나고자 하는 시간(7:00!)에 컴퓨터가 켜진다.
2. 파이썬 프로그램을 자동 실행한다.
3. 미리 확보해둔 음악들 중 하나를 재생한다. (유튜브 링크, 크롬)
4. (추가 기능) 20분 뒤에 자동으로 시스템을 종료한다. (집 비웠을 때 켜질까봐)



# 해결 과정

## 1. 컴퓨터 자동 실행

https://brunch.co.kr/@openmobile/127

위 블로그를 참고했다.

요약하자면 음.... 그냥 바이오스에서 설정하면 되는군...

약간 김새지만 세팅을 해준다.

<img src="C:\Users\kor\AppData\Roaming\Typora\typora-user-images\image-20240612003158592.png" alt="image-20240612003158592" style="zoom:50%;" />

easy peasy!



## 2. 파이썬 시작 프로그램 등록

![image-20240612003554769](C:\Users\kor\AppData\Roaming\Typora\typora-user-images\image-20240612003554769.png)

ㅇㅋ

![image-20240612003654682](C:\Users\kor\AppData\Roaming\Typora\typora-user-images\image-20240612003654682.png)



## 3. AlramforPowerfulMorning.py 작성

![image-20240612004124900](C:\Users\kor\AppData\Roaming\Typora\typora-user-images\image-20240612004124900.png)

먼저 메모장을 준비하고 그 안에 유튜브 음악 경로를 넣어둔다. 이러고 리스트에서 불러오면 되지.



```python
import os
import time
import random
import webbrowser

start = time.time()

f = open("C:/Users/kor/Documents/PowerfulMusicList.txt", 'r')
PowerfulMusics = f.read().split("\n")
TodaysMusic = random.choice(PowerfulMusics)
webbrowser.open_new(TodaysMusic)

while True:
    if time.time() - start > 60*20:
        break

os.system("shutdown -s -t 1")
```



20분 안에 일어나서 while 문을 종료시키지 않으면 컴퓨터는 알아서 종료된다.

이걸로 아침에 집에 없을 때 알아서 꺼지도록 만들었다.



내일 아침에 후기 간다!!



# 후기 1: 실행하랬더니...

라고 하기 전에 컴퓨터를 재부팅했더니 파이썬 파일이 실행 되긴 했다. 되긴 했는데....



![image-20240612010657997](C:\Users\kor\AppData\Roaming\Typora\typora-user-images\image-20240612010657997.png)



VS code 당신이 뜨면 안되는거잖아요



아무튼 아놔 어이 없네.

\__name__을 써야하나 싶다가.. 코드 실행 자체가 안 된 거니까 그것도 의미 없고... exe파일로 바꿔줘야겠다..



아무튼 진짜 잔다 내일 후기 고



# 후기2: 바이오스 설정 끝까지

https://www.asus.com/kr/support/faq/1043640/

아침 7시가 되어도 안 켜지길래 또 한숨 나오려다가 위 사이트를 참고해서 해결했다.

바이오스에서만 세팅할 게 아니라 윈도우 설정에서도 조작해줘야했다.

위 사이트가 내 바이오스랑 완전 같아서 (ASUS) 편하게 보면서 해결했다.





---

그리고 지금 github.io 블로그가 안 되어서 해결 중에 있다. 이 포스팅이 올라간다면 해결된 것.

첫 포스팅은 ruby 설치 없이 올라갔는데 결국 설치하게 되었다.
