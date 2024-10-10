# blinck project

## MPEblink 오픈소스와 fastapi를 통해 webcam으로 실시간 눈깜빡임을 감지하는 프로젝트를 만들었습니다.

## 준비
nstblink_r50.pth파일을 ```Shellpretrained_models/```안에 넣어주세요

```Shell
git clone https://github.com/wenzhengzeng/MPEblink
cp -r configs, demo_video, pretrained_models ./tools/code_for_demo
cd tools/code_for_demo
제가 올린 py파일들을 동일한 경로에 복사하세요

```

## 눈깜빡임을 감지하는 서버 모델실행
```Shell
(test할때, 눈감지 잘하는지 확인할때) python gogogo.py --download
(실제 구동할때) python gogogo.py
```
## local에서 webcam정보를 서버로 전송하는 코드 실행
```Shell
server_togo.ipynb
```

## 주의사항!
서버컴퓨터랑 로컬컴퓨터 포트번호 똑같이 맞춰주기!

## 예시
데모영상을 참고해주세요
```Shell
https://github.com/wenzhengzeng/MPEblink/blob/main/pictures/demo1.gif
```

### 실제로 테스트 했을때!
```Shell
웹캠 1초 영상찍었을때 결과를 내기까지 1.5초정도 걸렸고 정면과 측면에서 결과가 잘 나왔고 얼굴에 아래에서 위로찍을때, 위에서 아래로 찍을때는 결과가 좋지 않았습니다.
```
