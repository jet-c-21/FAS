# FAS - Face Analysis Applications

### A face analysis program built in Telegram-ChatBot that can predict one's BMI from one's face 

## How to launch the bot ?
1. open build-conda file and follow the instructions
2. open build-python file and follow the instructions
3. ```pip install -r -requirements.txt```
4. install the ngrok exe file for your OS
5. launch ngrok and choose a port for the websocket
6. type your telegram bot token in ```config.ini``` in ```bot_ult```
7. ```python FAS.py```

## Face Image Process Tool - glance
- Face Grid: the roi of the face in the image
- Face Feat: the visual 2d feature of human faces
- Face Scale: the scale to support for computing Face Feat
- Face YRP: base on the concept of Aircraft Principal Axes - calculate the Yaw, Roll, Pitch degree of the human faces in the image in real word
- jf_ult: my original image pipeline utilities

## How to use glance ?

```
from pprint import pprint as pp
from glance.face_analyst import FaceAnalyst

img_path = 'puff.jpg'

fa = FaceAnalyst(img_path, gen_ff_img=True)
fa.analyze()

if fa.result:
    pp(fa.data)
    print(fa.data.keys())
```