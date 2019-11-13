import speech_recognition as sr
import os
from gtts import gTTS
from bs4 import BeautifulSoup
import requests
from random import choice
import myspsolution as mysp

r = sr.Recognizer()
mic = sr.Microphone()

def file_string(filename):
    return os.path.join(os.getcwd()+f"\Sound files\{filename}.mp3")

def listen():
    with mic as source:
        audio = r.listen(source)
        with open('transcript.wav','wb') as f:
            f.write(audio.get_wav_data())
    command = r.recognize_google(audio)
    return command

def word_count(s):
    counts = dict()
    for word in s.split():
        if word in counts:
            counts[word] +=1
        else:
            counts[word] = 1
    return counts

def start_interview():
    req = requests.get("https://www.glassdoor.com/blog/common-interview-questions/")
    soup = BeautifulSoup(req.content,'html.parser')
    items = soup.find("ol").findAll('li')
    questions = []
    for item in items[1:]:
        if item.text != "":
            questions.append(item.text)
    question = choice(questions)
    record(question,title="question")
    os.startfile(file_string("question"))

def record(text,title):
    gtts_obs=gTTS(text=text,lang="en")
    gtts_obs.save(f"Sound files/{title}.mp3")

def analysis(p):
    print(mysp.mysptotal(p,os.getcwd()))
    print(mysp.myspgend(p,os.getcwd()))
    print(mysp.mysppron(p,os.getcwd()))



if __name__ == "__main__":
    os.startfile(file_string("start"))
    response = listen()
    if response == "yes":
        os.startfile(file_string("ready"))
        start_interview()
    else:
        os.startfile(file_string("bye"))
    listen()
    analysis('transcript')
