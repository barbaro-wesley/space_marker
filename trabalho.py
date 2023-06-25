# Wesley Barbaro(1134832) Wendel Barbaro (1134430)
import pygame
import winsound
from tkinter import simpledialog
def save_points(filename):
    with open(filename, 'w') as file:
        for pos, name in estrelas:
            file.write(f"{name} ({pos[0]}, {pos[1]})\n")

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
                pygame.draw.line(tela, branco, circulos[i - 1], circulos[i], 3)
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

