import speech_recognition as speak
from gtts import gTTS as shon
import time
import os


myText="Hello, I am Shihab Kamel.I am a student of Computer science and engineering.This is my digital cv.Ask me about my any information."
language='en-in'
print(myText)
output=shon(text=myText,lang=language)
output.save("Introdution.mp3")
os.system("start Introdution.mp3")
time.sleep(15)
  
def educational_status():
    info_edu="School: Satkhira Govt. High School. PASSED with 5.00 GPA.College: Satkhira Govt. College. PASSED With 3.84 GPA.University: Bangladesh Army University of Science & Technology.Which is running."
    output_edu=shon(text=info_edu,lang=language)
    output_edu.save("info_edu.mp3")
    os.system("start info_edu.mp3")
    time.sleep(20)
def experience():
    info_exp="কোনো এক্সপিরিএন্স নাই"
    output_exp=shon(text=info_exp,lang='bn')
    output_exp.save("info_exp.mp3")
    os.system("start info_exp.mp3")
    time.sleep(20)
def projects():
    pass
def skills():
    pass
def certification():
    pass
def achievement():
    pass


def hear():
    print("1.Educational status.")
    print("2.Experience")
    print("3.Additional projects")
    print("4.Skills")
    print("5.Licenses & certifications")
    print("6.Other acheivements")

    sr=speak.Recognizer()
    print("I am litsening.........")
    with speak.Microphone() as m:
        audio=sr.listen(m)
        query= sr.recognize_google(audio,language='eng-in')
        print(query)  
    if(query=="educational status"):
        educational_status()
        hear() 
    elif(query=="experience"):
        experience()
        hear()
    elif(query=="additional projects"):
        projects()
        hear()
    elif(query=="skill"):
        skills()
        hear()
    elif(query=="licenses and certification"):
        certification()
        hear()                       
    elif(query=="other achievement"):
        achievement()
        hear()
    else:
        print("Command error")
        hear()    
hear()     




