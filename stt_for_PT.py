import speech_recognition as sr

import requests
from playsound import playsound
import time
import random


introduction_list = ['안녕', '하루야 안녕', '하루애 안녕', '하루에 안녕']
write_list = ['일기쓸래', '일기 쓰기', '일기 쓸래', '하루야 일기 쓸래']
weather_list = ['맑음', '맑았다', '말 같다', '맑았어','화창했어', '말 갔어', '잘 갔어']
emotion_list = ['기쁨','기뻤다', '즐거웠다', '재밌었다', '즐거웠어','기뻤어', '즐거웠어']
drawing_list = ['유화', '유하']

def get_data():
    r = sr.Recognizer()

    with sr.Microphone() as source: 
        # playsound('first.mp3')
        print("말씀해주세요. ")
        audio = r.listen(source)
        audio_data = r.recognize_google(audio, language='ko')
        print('대답 : ', audio_data)
    return audio_data    


while True:
    
    weather = ''
    drawing = ''
    emotion = ''
    content = ''

    audio_data = get_data()
    # print(audio_data)
    done = False

    #인사말
    if audio_data in introduction_list:
        hello_list=['audio_tts/hello1.mp3', 'audio_tts/hello2.mp3']
        randomhello = random.choice(hello_list)
        print(randomhello)
        playsound(randomhello)
        print()

    #일기쓰기 시작
    elif audio_data in write_list:
        print(audio_data)
        print()       
        playsound('audio_tts/weather1.mp3')
        print('오늘은 날씨는 어떠셨습니까?')
        for i in range(10):
            audio_data = get_data()

            if audio_data in weather_list:
                weather = '맑음'
                print()
                playsound('audio_tts/emotion1.mp3')
                print('오늘 기분은 어땠나요')
                for i in range(10):
                    audio_data = get_data()
                    if audio_data in emotion_list:
                        emotion = '기쁨'
                        print()
                        playsound('audio_tts/drawing1.mp3')
                        print('화풍을 선택해주세요')
                        for i in range(10):
                            audio_data = get_data()
                            if audio_data in drawing_list:
                                drawing = '유화'
                                print()
                                playsound('audio_tts/content.mp3')
                                print('오늘 기록에 남기고 싶은 걸 말씀해주세요')
                                audio_data = get_data()
                                content = audio_data
                                test_url = "http://192.168.43.223:8000/diary/test/"
                                test_formdata = {'content_short': (None, content),
                                            'Weather':(None, weather),
                                            'Drawing':(None, drawing),
                                            'Emotion':(None, emotion),
                                                }
                                test_formresponse = requests.post(test_url, files=test_formdata)
                                print('===========TEST',test_formresponse)

                            else:
                                print()
                                playsound('audio_tts/dontknow.mp3')
                                print('화풍을 다시 말씀해주세요')
                               
                    else:
                        playsound('audio_tts/dontknow.mp3')
                        print('기분을 다시 말씀해주세요')
                        print()    

                done = True
                break
            else:
                playsound('audio_tts/dontknow.mp3')
                print('날씨를 모르겠어요')
                print()
                #do nothing

    else:
        print(audio_data)
        playsound('audio_tts/dontknow.mp3')
        print('i dont understand please say again')
        print()

    if done==True:
        break

