# blinck project

## MPEblink 오픈소스와 fastapi를 통해 webcam으로 실시간 눈깜빡임을 감지하는 프로젝트를 만들었습니다.

## 준비
nstblink_r50.pth파일을 ```Shellpretrained_models/```안에 넣어주세요

```Shell
git clone https://github.com/wenzhengzeng/MPEblink
cp -r configs, demo_video, pretrained_models ./tools/code_for_demo
cd tools/code_for_demo
```

## 눈깜빡임을 감지하는 서버 모델실행
```Shell
python gogogo.py --download True
```
## local에서 webcam정보를 서버로 전송하는 코드 실행
```Shell
server_togo.ipynb
```

## 주의사항!
서버컴퓨터랑 로컬컴퓨터 포트번호 똑같이 맞춰주기!
