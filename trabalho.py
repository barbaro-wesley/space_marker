# Wesley Barbaro(1134832) Wendel Barbaro (1134430)
import pygame
import winsound
import os
import math 
from tkinter import simpledialog
def save_points(filename):
    with open(filename, 'w') as file:
        for pos, name in estrelas:
            file.write(f"{name} ({pos[0]}, {pos[1]})\n")

def resetar_marcações():
    global estrelas,circulos
    estrelas=[]
    circulos=[]
def carregar_pontos(filename):
    global estrelas, circulos
    estrelas = []
    circulos = []
    with open(filename, 'r') as file:
        for line in file:
            data = line.strip()
            name_start = data.index(' ') + 1
            name_end = data.index('(')
            name = data[name_start:name_end].strip()
            coords_start = data.index('(') + 1
            coords_end = data.index(')')
            coords = data[coords_start:coords_end].strip().split(',')
            pos = (int(coords[0]), int(coords[1]))
            estrelas.append((pos, name))
            circulos.append(pos)
def calculate_distance(p1, p2):
    return math.sqrt((p2[0] - p1[0]) ** 2 + (p2[1] - p1[1]) ** 2)
pygame.init()
tamanho = (800, 600)
tela = pygame.display.set_mode(tamanho)
pygame.display.set_caption("space marker")
icon=pygame.image.load("space_icone.jpg")
pygame.display.set_icon(icon)
clock = pygame.time.Clock()
fundo = pygame.image.load("bg.jpg")
pygame.mixer.music.load("novatrilha.mp3")
pygame.mixer.music.play(0,0,5)
branco=(255,255,255)
circulos=[]
estrelas = []

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            save_points("points.txt") 
            pygame.quit()    
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_F10:
                save_points("points.txt") 
            elif event.key == pygame.K_ESCAPE:
                save_points("points.txt")
                pygame.quit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            pos = pygame.mouse.get_pos()
            if pos[0] < tamanho[0] and pos[1] < tamanho[1]:
                
                circulos.append(pos)
                
            item=simpledialog.askstring("Space ", "Nome da Estrela")
            print (item)
            if item == None:
                item = "desconhecido "+str(pos)
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
            p1 = circulos[i - 1]
            p2 = circulos[i]
            pygame.draw.line(tela, branco, p1, p2, 3)
            distance = calculate_distance(p1, p2)
            fonte_distancia = pygame.font.Font(None, 18)
            texto_distancia = fonte_distancia.render(f"Distância: {distance:.2f}", True, branco)
            pos_distancia = ((p1[0] + p2[0]) // 2, (p1[1] + p2[1]) // 2)
            tela.blit(texto_distancia, pos_distancia)
    fonte=pygame.font.Font(None,18)
    texto = fonte.render(f"estrelas encontradas: {len(estrelas)}", True, (branco))
    tela.blit(texto, (10, 10))
    opções =["Pressione F10 para salvar os dados;",
               "Pressione F11 para carregar os dados;",
               "Pressione F12 para excluir os dados; "
    ]
    fonte_da_opção=pygame.font.Font(None,16)
    for r, opções in enumerate (opções):
        texto_mensagem = fonte_da_opção.render(opções, True, branco)
        pos_mensagem = (10, 30 + r * 20)
        tela.blit(texto_mensagem, pos_mensagem)
    
    pygame.display.flip()
    clock.tick(60)
    keys=pygame.key.get_pressed()
    if keys[pygame.K_F10]:
        save_points("points.txt")
    elif keys[pygame.K_F12]:
        resetar_marcações()
    elif keys[pygame.K_F11]:
        carregar_pontos("points.txt")
