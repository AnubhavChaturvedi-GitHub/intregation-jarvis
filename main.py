import random
from Head.Ear import *
from Traning_Model.model import mind
from Function.wish import wish
from Function.welcome import welcome
from Data.dlg_data.dlg import *
from Head.Mouth import speak



def jarvis():
    wish()
    while True:
        text = listen().lower()
        if text in wake_key_word:
            welcome()
        elif text in bye_key_word:
            res_random = random.choice(res_bye)
            speak(res_random)
            break
        elif text.startswith(("jarvis","buddy","jar")):
            text = text.replace("jarvis","")
            text = text.replace("vis","")
            text = text.replace("buddy","")
            text = text.replace("jar","")
            text = text.strip()
            text = mind(text)
            speak(text)
        elif text.endswith(("jarvis","buddy","jar"," jarvis"," buddy"," jar")):
            text = text.replace("jarvis","")
            text = text.replace("vis","")
            text = text.replace("buddy","")
            text = text.replace("jar","")
            text = text.strip()
            text = mind(text)
            speak(text)
        else:
            pass







jarvis()