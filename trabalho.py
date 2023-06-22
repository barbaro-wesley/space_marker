import pygame
import random
import winsound

pygame.init()

tamanho = (800, 600)
tela = pygame.display.set_mode(tamanho)
pygame.display.set_caption("space marker")
icone=pygame.image.load("space_icone.jpg")
pygame.display.set_icon(icone)
clock = pygame.time.Clock()
fundo = pygame.image.load("bg.jpg")
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
           

    tela.blit(fundo, (0, 0))
    pygame.display.flip()
    clock.tick(60)

