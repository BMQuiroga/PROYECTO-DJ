from email.mime import image
from logging import exception
from pickletools import TAKEN_FROM_ARGUMENT1

import speech_recognition as sr
import os
import difflib as dl
import webbrowser

import pygame

pygame.init()

screen = pygame.display.set_mode((1024,696))


class boton():
    def __init__(self,x,y,img,size):
        
        self.x = x
        self.y = y
        self.width = img.get_width()
        self.height = img.get_height()
        self.img = pygame.transform.scale(img,(int(self.width * size),int(self.height * size)))
        self.rect = self.img.get_rect()
        self.rect.topleft = (x,y)
        self.click = False

    def draw(self):
        action = False
        screen.blit(self.img,[self.x,self.y])
        if self.rect.collidepoint(pygame.mouse.get_pos()):
            if pygame.mouse.get_pressed()[0] and not self.click:
                self.click = True
                action = True
        if not pygame.mouse.get_pressed()[0]:
            self.click = False
            action = False
        return action


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
    
    
    #print(audio)
    lista = os.listdir('D:\\Descargas\\backup\\Internet Explorer')
    
    tema = dl.get_close_matches(audio,lista,8,0.1)
    tema2 = []
    for elemento in tema:
        if elemento.find('.mp3') != -1:
            tema2.append(elemento)
    

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
    botones = []
    textos = []
    tamaño = len(temas)
    
    
    for i in range(tamaño):
        botones.append(boton(50,50+(i*70),button,0.2))
        textos.append(arial.render(temas[i].split('.mp3')[0],False,(128,0,128)))

    #print(temas)#tienen el .mp3 como deberian

    

    while 1:
        screen.blit(background,[0,0])

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()
        
        for j in range(tamaño):
            if botones[j].draw():
                end(temas[j])
            screen.blit(textos[j],[130,40+(j*70)])
                
            
        pygame.display.flip()



def mainmenu():
    

    arial = pygame.font.SysFont('Arial', 100)
    texto_si = arial.render('Si',False,(0,0,0))
    texto_no = arial.render('No',False,(0,0,0))
    #rojo = (255,0,0)
    background = pygame.image.load("D:\Documentos\git\PROYECT\PROYECTO-DJ\dj.jpg").convert()
    button = pygame.image.load("D:\Documentos\git\PROYECT\PROYECTO-DJ\\button_re.png").convert()

    boton_si = boton(300,440,button,1)
    boton_no = boton(1024-300-158,440,button,1)

    while 1:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()
            

        screen.blit(background,[0,0])


        if boton_no.draw():
            exit()
        if boton_si.draw():
            print('si')
            return

        screen.blit(texto_si,[300,400])
        screen.blit(texto_no,[1024-300-158,400])



        pygame.display.flip()

def main():
    mainmenu()

    menu_dj()







if __name__ == '__main__':
    main()


