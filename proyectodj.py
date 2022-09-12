import speech_recognition as sr
import os
import difflib as dl
import webbrowser
import button_class

import pygame

pygame.init()

screen = pygame.display.set_mode((1024,696))


def speech_recorder():
    r = sr.Recognizer()
    speech = 'hola'
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


def main_audio():



    audio = speech_recorder()
   
    
    print(audio)

    
    lista = os.listdir('D:\\Descargas\\backup\\Internet Explorer')
    lista2 = []
    for i in range(len(lista)):
        aux = lista.pop()
        lista.insert(0,aux.lower())

    #print(lista)


    #elementos = 0
    cutoff = 0.1
    tema2 = []

    #while elementos < 8:
    tema = dl.get_close_matches(audio,lista,8,cutoff)
    for elemento in tema:
        if elemento.find('.mp3') != -1:
            tema2.append(elemento.upper())
        #elementos = len(tema2)
        #cutoff = cutoff + 0.01
    
    while len(tema2) > 8:
        tema2.pop
    
    #for elemento in tema2:


    return tema2

def path_creator(tema):
    
    invertedslash = '\\'

    #print(invertedslash)
    path = 'D:\\Descargas\\backup\\Internet Explorer' + invertedslash + tema
    return path

def end(tema):
    webbrowser.open(path_creator(tema))
    exit()

def menu_dj():
    background = pygame.image.load("D:\Documentos\git\PROYECT\PROYECTO-DJ\dj.jpg").convert()
    
    arial = pygame.font.SysFont('Arial', 60)
    temas = main_audio()
    #temas = ['TEMA1GENERICO.mp3','TEMA2GENERICO.mp3','TEMA3GENERICO.mp3','TEMA4GENERICO.mp3']
    button = pygame.image.load("D:\Documentos\git\PROYECT\PROYECTO-DJ\\button2.png").convert()
    returnbutton = pygame.image.load("D:\Documentos\git\PROYECT\PROYECTO-DJ\\return.png").convert()
    button_re = pygame.image.load("D:\Documentos\git\PROYECT\PROYECTO-DJ\\button_re.png").convert()
    botones = []
    textos = []
    tamaño = len(temas)
    boton_return = button_class.boton(960,0,returnbutton,0.1)
    boton_no = button_class.boton(960,40,button_re,0.3)
    
    for i in range(tamaño):
        botones.append(button_class.boton(50,50+(i*70),button,0.2))
        textos.append(arial.render(temas[i].split('.MP3')[0],False,(128,0,128)))

    #print(temas)#tienen el .mp3 como deberian

    

    while 1:
        screen.blit(background,[0,0])



        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()
        
        for j in range(tamaño):
            if botones[j].draw(screen):
                end(temas[j])
            screen.blit(textos[j],[130,40+(j*70)])
                
        if boton_return.draw(screen):
            return    
        if boton_no.draw(screen):
            exit()
        
        pygame.display.flip()



def mainmenu():
    

    arial = pygame.font.SysFont('Arial', 100)
    texto_si = arial.render('Si',False,(0,0,0))
    texto_no = arial.render('No',False,(0,0,0))
    #rojo = (255,0,0)
    background = pygame.image.load("D:\Documentos\git\PROYECT\PROYECTO-DJ\dj.jpg").convert()
    button = pygame.image.load("D:\Documentos\git\PROYECT\PROYECTO-DJ\\button_re.png").convert()

    boton_si = button_class.boton(300,440,button,1)
    boton_no = button_class.boton(1024-300-158,440,button,1)

    while 1:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()
            

        screen.blit(background,[0,0])


        if boton_no.draw(screen):
            exit()
        if boton_si.draw(screen):
            print('si')
            return

        screen.blit(texto_si,[300,400])
        screen.blit(texto_no,[1024-300-158,400])



        pygame.display.flip()

def main():
    mainmenu()
    while 1:
        menu_dj()







if __name__ == '__main__':
    main()


