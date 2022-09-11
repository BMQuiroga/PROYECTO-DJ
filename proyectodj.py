from logging import exception
import speech_recognition as sr
import os
import difflib as dl
import webbrowser


def speech_recorder():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Say something!")
        audio = r.listen(source)
        try:
            speech = r.recognize_google(audio)
            
            
            #print('Google: ' + speech)
            
            
            #print('Bing: ' + r.recognize_bing(audio,))REQUIERE KEY
            #print('Houndify: ' + r.recognize_houndify(audio))REQUIERE ID Y KEY
            #print('IBM: ' + r.recognize_ibm(audio)) REQUIERE USERNAME Y PASSWORD
            #print('Sphinx: ' + r.recognize_sphinx(audio)) MISSING POCKETSPINX MODULE
            #print('Wit: ' + r.recognize_wit(audio)) REQUIERE KEY
        except Exception as e:
            print('Error' + str(e))
    
    return speech


def main():
    audio = speech_recorder()
    
    #print(audio)
    lista = os.listdir('D:\\Descargas\\backup\\Internet Explorer')
    #print(lista)
    tema = dl.get_close_matches(audio,lista,1,0.1)
    #print(tema)
    
    invertedslash = '\\'

    #print(invertedslash)
    path2 = 'D:\\Descargas\\backup\\Internet Explorer' + invertedslash + tema[0]
    
    #print(path2)
    
    webbrowser.open(path2)

if __name__ == '__main__':
    main()

#TODOLIST
#1 - RECONOCIMIENTO DE AUDIO
#3 - EL GET CLOSE MATCHES HACE CUALQUIER COSA
