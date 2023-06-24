# Wesley Barbaro(1134832) Wendel Barbaro (1134430)
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
pygame.mixer.music.play(0,1)
branco=(255,255,255)
circulos=[]
estrelas = []

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            

        if event.type == pygame.MOUSEBUTTONDOWN:
            pos = pygame.mouse.get_pos()
            if pos[0] < tamanho[0] and pos[1] < tamanho[1]:
                
                circulos.append(pos)
                
            item=simpledialog.askstring("Space ", "Nome da Estrela")
            print (item)
            if item == None:
                item == "desconhecido "+str(pos)
            estrelas.append((pos, item))


    tela.blit(fundo, (0, 0))

    
    for pos,nome  in estrelas:
        pygame.draw.circle(tela, (branco), pos, 3)
        fonte = pygame.font.Font(None, 18)
        texto = fonte.render(f"{nome} ({pos[0]}, {pos[1]})", True, branco)
        pos_texto=(pos[0]+10,pos[1]-10)
        tela.blit(texto,pos_texto)
    if len(circulos)>1:
        for i in range (1, len(circulos)):
                pygame.draw.line(tela, branco, circulos[i - 1], circulos[i], 1)
    fonte=pygame.font.Font(None,18)
    texto = fonte.render(f"estrelas encontradas: {len(estrelas)}", True, (branco))
   
    tela.blit(texto, (10, 10))

    pygame.display.flip()
    clock.tick(60)
    


