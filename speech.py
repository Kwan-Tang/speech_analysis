import speech_recognition as sr
import os
from gtts import gTTS
from bs4 import BeautifulSoup
import requests
from random import choice
# r = sr.Recognizer()
#
# mic = sr.Microphone()
#
# with mic as source:
#     audio = r.listen(source)
#     with open('transcript.wav','wb') as f:
#         f.write(audio.get_wav_data())
#
# command = r.recognize_google(audio)
# def word_count(s):
#     counts = dict()
#     for word in s.split():
#         if word in counts:
#             counts[word] +=1
#         else:
#             counts[word] = 1
#     return counts
#
# print(word_count(command))

def start_interview():
    req = requests.get("https://www.glassdoor.com/blog/common-interview-questions/")
    soup = BeautifulSoup(req.content,'html.parser')
    items = soup.find("ol").findAll('li')
    questions = []
    for item in items[1:]:
        if item.text != "":
            questions.append(item.text)
    text = choice(questions)
    lang = "en"
    gtts_obj = gTTS(text,lang)
    gtts_obj.save("question.mp3")
    os.startfile("question.mp3")

if __name__ == "__main__":
    start_interview()
