from operator import inv
import speech_recognition as sr
import os 
import difflib as dl

def main():
    audio = speech_recognition()
    path = 'D:\Descargas\backup\Internet Explorer'
    lista= os.listdir(path)
    tema = dl.get_close_matches(audio,lista)
    invertedslash = '\ '
    invertedslash = invertedslash - ' '
    path2 = path + invertedslash + tema
    print(invertedslash)
    print(tema)
    print(path2)
    os.open(path2)


main()

def speech_recognition():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Say something!")
        audio = r.listen(source)
    return audio