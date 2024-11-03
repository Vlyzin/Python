#Faça um arquivo que abra e reproduza um audio mp3
import pygame

pygame.mixer.init()

pygame.mixer.music.load(r'C:\Users\vinic\Documents\VsCode\Projeto 1\teste.mp3')
pygame.mixer.music.play()

while pygame.mixer.music.get_busy():
    pass
