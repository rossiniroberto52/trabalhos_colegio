import pygame
import os
import sys
import math
from time import sleep

PRETO = (0, 0, 0)
BRANCO = (255, 255, 255)
VERMELHO = (255, 0, 0)
VERDE = (0, 255, 0)
AZUL = (0, 0, 255)


PI = 3.1416

pygame.init()

janela = pygame.display.set_mode((800, 600))
pygame.display.set_caption('figuguras e txt')

janela2 = pygame.display.set_mode((800, 600))
pygame.display.set_caption('!')

janela.fill(PRETO)

fonte = pygame.font.Font(None, 48)
texto = fonte.render('hacking ...', True, VERDE)
janela.blit(texto, (100, 100))

pygame.display.update()


arquivo = open("contatos.txt", "a")
arquivo.write("user: PFAdmin135RT senha: PFAdminRT")
pygame.display.update(sleep(5))


deve_continual = True

while deve_continual:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            deve_continual = False

pygame.quit()