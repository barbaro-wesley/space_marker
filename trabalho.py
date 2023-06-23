import pygame
import random
import winsound
from tkinter import simpledialog
pygame.init()

tamanho = (800, 600)
tela = pygame.display.set_mode(tamanho)
pygame.display.set_caption("space marker")
icone=pygame.image.load("space_icone.jpg")
pygame.display.set_icon(icone)
clock = pygame.time.Clock()
fundo = pygame.image.load("bg.jpg")
pygame.mixer.music.load("Space_Machine_Power.mp3")
pygame.mixer.music.play(0,5)
branco=(255,255,255)
circulos=[]
estrelas = 0

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            

        if event.type == pygame.MOUSEBUTTONDOWN:
            pos = pygame.mouse.get_pos()
            if pos[0] < tamanho[0] and pos[1] < tamanho[1]:
                
                circulos.append(pos)
                estrelas += 1
            item=simpledialog.askstring("Space ", "Nome da Estrela")
            print (item)
            if item == None:
                item = "desconhecido "+str(pos)
            

    tela.blit(fundo, (0, 0))

    
    for pos in circulos:
        pygame.draw.circle(tela, (255, 255, 255), pos, 3)
    fonte = pygame.font.Font(None, 36)
    texto = fonte.render(f"estrelas encontradas: {estrelas}", True, (255, 255, 255))
    tela.blit(texto, (10, 10))
    pygame.display.flip()
    clock.tick(60)
    


