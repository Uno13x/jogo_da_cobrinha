import pygame
import random

pygame.init()
pygame.display.set_caption("JOGO DA COBRINHA")
largura, altura = 900, 700
tela = pygame.display.set_mode((largura, altura))
relogio = pygame.time.Clock()

def gerar_comida():
    comida_x = round(random.randrange(0, largura - quadrado) / quadrado) * quadrado
    comida_y = round(random.randrange(0, altura - quadrado) / quadrado) * quadrado
    return comida_x, comida_y

def desenhar_comida(tamanho, comida_x, comida_y):
    pygame.draw.rect(tela, vermelha, [comida_x, comida_y, tamanho, tamanho])

def desenhar_cobra(tamanho, pixels):
    for pixel in pixels:
        pygame.draw.rect(tela, verde, [pixel[0], pixel[1], tamanho, tamanho])

def desenhar_pontuação(pontuacao):
    fonte = pygame.font.SysFont("Helvetica", 25)
    texto = fonte.render(f"Pontuação: {pontuacao}", False, branca)
    tela.blit(texto, [1, 1])

def selecionar_velocidade(tecla):
    if tecla == pygame.K_DOWN:
        velocidade_x = 0
        velocidade_y = quadrado
    elif tecla == pygame.K_UP:
        velocidade_x = 0
        velocidade_y = -quadrado
    elif tecla == pygame.K_RIGHT:
        velocidade_x = quadrado
        velocidade_y = 0
    elif tecla == pygame.K_LEFT:
        velocidade_x = -quadrado
        velocidade_y = 0
    return velocidade_x, velocidade_y

preta = (0, 0, 0)
branca = (255, 255, 255)
vermelha = (255, 0, 0)
verde = (0, 255, 0)

quadrado = 20
velocidade_do_jogo = 15

def rodar():
    fim = False
 
    x = largura / 2
    y = altura / 2

    velocidade_x = 0
    velocidade_y = 0

    tamanho_cobra = 1
    pixels = []

    comida_x, comida_y = gerar_comida()

    while not fim:
        tela.fill(preta)  

        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                fim = True
            elif evento.type == pygame.KEYDOWN:
                velocidade_x, velocidade_y = selecionar_velocidade(evento.key)

        comidas = [comida_x, comida_y]
        desenhar_comida(quadrado, comida_x, comida_y)
        
        x += velocidade_x
        y += velocidade_y

        pixels.append([x, y])
        if len(pixels) > tamanho_cobra:
            del pixels[0]

        for pixel in pixels[:-1]:
            if pixel == [x, y]:
                fim = True

        if x >= largura or x < 0 or y >= altura or y < 0:
            fim = True

        desenhar_cobra(quadrado, pixels)

        desenhar_pontuação(tamanho_cobra - 1)

        pygame.display.update()

        if comida_x - quadrado <= x <= comida_x + quadrado and comida_y - quadrado <= y <= comida_y + quadrado:
            tamanho_cobra += 1
            comida_x, comida_y = gerar_comida()

        relogio.tick(velocidade_do_jogo)

rodar()
