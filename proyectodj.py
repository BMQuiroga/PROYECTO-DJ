import pywhatkit
import speech_recognition as sr
import os
import difflib as dl
import webbrowser
import button_class

import pygame

pygame.init()

screen = pygame.display.set_mode((1024,696))

def menu_whatsapp():
    pass









def speech_recorder(code):

    arial = pygame.font.SysFont('Arial', 150)
    texto_saysomething = arial.render('SAY SOMETHING',False,(128,0,128))
    background = pygame.image.load("D:\Documentos\git\PROYECT\PROYECTO-DJ\dj.jpg").convert()

    r = sr.Recognizer()
    speech = 'hola'
    with sr.Microphone() as source:
        print("Say something!")
        pygame.display.flip()
        screen.blit(background,[0,0])
        screen.blit(texto_saysomething,[0,400])
        pygame.display.flip()


        audio = r.listen(source)
        

        try:
            if code == 0:
                speech = r.recognize_google(audio,None,language='es-AR')
            if code == 1:
                speech = r.recognize_google(audio)
            
            
            #print('Google: ' + speech)
            
            
            #print('Bing: ' + r.recognize_bing(audio,))REQUIERE KEY
            #print('Houndify: ' + r.recognize_houndify(audio))REQUIERE ID Y KEY
            #print('IBM: ' + r.recognize_ibm(audio)) REQUIERE USERNAME Y PASSWORD
            #print('Sphinx: ' + r.recognize_sphinx(audio)) MISSING POCKETSPINX MODULE
            #print('Wit: ' + r.recognize_wit(audio)) REQUIERE KEY
        except Exception as e:
            print('Error' + str(e))
    
    pygame.display.flip()

    return speech

def menu_yt(audio):
    pywhatkit.playonyt(audio)


def main_audio(code):



    audio = speech_recorder(code)
   
    
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
    tema = dl.get_close_matches(audio,lista,7,cutoff)
    for elemento in tema:
        if elemento.find('.mp3') != -1:
            tema2.append(elemento.upper())
        #elementos = len(tema2)
        #cutoff = cutoff + 0.01
    
    while len(tema2) > 8:
        tema2.pop
    
    #for elemento in tema2:


    return (tema2, audio)

def path_creator(tema):
    
    invertedslash = '\\'

    #print(invertedslash)
    path = 'D:\\Descargas\\backup\\Internet Explorer' + invertedslash + tema
    return path

def end(tema):
    webbrowser.open(path_creator(tema))
    exit()

def menu_dj(code):
    background = pygame.image.load("D:\Documentos\git\PROYECT\PROYECTO-DJ\dj.jpg").convert()
    
    arial = pygame.font.SysFont('Arial', 60)
    temas = main_audio(code)
    audio = temas[1]
    temas = temas[0]
    #temas = ['TEMA1GENERICO.mp3','TEMA2GENERICO.mp3','TEMA3GENERICO.mp3','TEMA4GENERICO.mp3']
    
    button = pygame.image.load("D:\Documentos\git\PROYECT\PROYECTO-DJ\\button2.png").convert()
    returnbutton = pygame.image.load("D:\Documentos\git\PROYECT\PROYECTO-DJ\\return.png").convert()
    button_re = pygame.image.load("D:\Documentos\git\PROYECT\PROYECTO-DJ\\button_re.png").convert()
    botones = []
    textos = []
    tamaño = len(temas)
    boton_return = button_class.boton(960,0,returnbutton,0.1)
    boton_no = button_class.boton(960,40,button_re,0.3)
    boton_yt = button_class.boton(1024-128,696-128,pygame.image.load("D:\Documentos\git\PROYECT\PROYECTO-DJ\\yt_button.png").convert_alpha(),0.0625*2)
    boton_btb = button_class.boton(960,80,pygame.image.load("D:\Documentos\git\PROYECT\PROYECTO-DJ\\btb_1.png").convert_alpha(),0.1)
    
    for i in range(tamaño):
        botones.append(button_class.boton(50,120+(i*70),button,0.2))
        textos.append(arial.render(temas[i].split('.MP3')[0],False,(128,0,128)))

    #print(temas)#tienen el .mp3 como deberian

    str_audio = 'Busqueda: ' + audio
    texto_audio = arial.render(str_audio,False,(255,0,0))

    

    while 1:
        screen.blit(background,[0,0])
        screen.blit(texto_audio,[50,50])


        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()
        
        for j in range(tamaño):
            if botones[j].draw(screen):
                end(temas[j])
            screen.blit(textos[j],[130,110+(j*70)])
                
        if boton_return.draw(screen):
            return False    
        if boton_no.draw(screen):
            exit()
        if boton_yt.draw(screen):
            menu_yt(audio)
        if boton_btb.draw(screen):
            return True


        pygame.display.flip()



def mainmenu():
    

    arial = pygame.font.SysFont('Arial', 100)
    texto_yes = arial.render('Yes',False,(0,0,0))
    texto_si = arial.render('Si',False,(0,0,0))
    texto_no = arial.render('No',False,(0,0,0))
    #rojo = (255,0,0)
    background = pygame.image.load("D:\Documentos\git\PROYECT\PROYECTO-DJ\dj.jpg").convert()
    button = pygame.image.load("D:\Documentos\git\PROYECT\PROYECTO-DJ\\button_re.png").convert()

    boton_yes = button_class.boton(1024/2-158/2-250,440,button,1)
    boton_si = button_class.boton(1024/2-158/2,440,button,1)
    boton_no = button_class.boton(1024/2-158/2+250,440,button,1)
    boton_wsp = button_class.boton(0,0,pygame.image.load("D:\Documentos\git\PROYECT\PROYECTO-DJ\Wsp.png").convert_alpha(),0.3)

    while 1:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()
            

        screen.blit(background,[0,0])


        if boton_no.draw(screen):
            exit()
        if boton_si.draw(screen):
            print('si')
            return 0
        if boton_yes.draw(screen):
            print('yes')
            return 1
        if boton_wsp.draw(screen):
            print('warap')
            return 2
        screen.blit(texto_si,[1024/2-158/2,400])
        screen.blit(texto_no,[1024/2-158/2+250,400])
        screen.blit(texto_yes,[1024/2-158/2-250,400])

        pygame.display.flip()



def main():

    while 1:
        code = mainmenu()

        while 1:
            if code == 2:
                menu_whatsapp()
            else:
                if menu_dj(code):
                    break







if __name__ == '__main__':
    main()


