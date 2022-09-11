from operator import inv
import speech_recognition as sr
import os
import difflib as dl
import playsound

def speech_recorder():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Say something!")
        audio = r.listen(source)
    return audio

def speech_recognize(audio):
    return 'Camellia'

def main():
    #audio = speech_recorder()
    audio = speech_recognize('audio')
    print(audio)
    lista= os.listdir('D:\\Descargas\\backup\\Internet Explorer')
    #print(lista)
    tema = dl.get_close_matches(audio,lista,1,0.1)
    print(tema)
    
    invertedslash = '\\'

    print(invertedslash)
    path2 = 'D:\\Descargas\\backup\\Internet Explorer' + invertedslash + tema[0]
    
    print(path2)
    playsound.playsound(os.path.relpath(path2))

main()

#TODOLIST
#1 - RECONOCIMIENTO DE AUDIO
#2 - PATH RELATIVO
#3 - EL GET CLOSE MATCHES HACE CUALQUIER COSA
