import pygame
import sys
from code.Jogador import Jogador
from code.Obstaculo import Obstaculo
from code.const import *

pygame.mixer.pre_init(44100, -16, 2, 512)
pygame.init()
pygame.mixer.init()
print("Mixer inicializado:", pygame.mixer.get_init())


tela = pygame.display.set_mode((LARGURA, ALTURA))
clock = pygame.time.Clock()

fundo = pygame.image.load("asset/forest_bridge.png")
fundo = pygame.transform.scale(fundo, (LARGURA, ALTURA))

musica_fundo = "asset/somdojogo.wav"
pygame.mixer.music.load(musica_fundo)
pygame.mixer.music.set_volume(0.5)  # volume de 0.0 a 1.0
pygame.mixer.music.play(-1)  # -1 = loop infinito

som_colisao = pygame.mixer.Sound("asset/gameover.wav")



jogador = Jogador(LARGURA)
obstaculos = [Obstaculo(LARGURA, ALTURA, TAMANHO_OBSTACULO)]

rodando = True
game_over = False
pontos = 0
recorde = 0
tempo = 0
tempo_spawn = 0
frequencia_spawn = 2

fonte_grande = pygame.font.SysFont(None, 80)
fonte_pequena = pygame.font.SysFont(None, 40)

while rodando:

    dt = clock.tick(FPS) / 1000

    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            rodando = False

        if game_over and evento.type == pygame.KEYDOWN:
            if evento.key == pygame.K_r:
                pontos = 0
                tempo = 0
                game_over = False
                jogador = Jogador(LARGURA)
                obstaculos = [Obstaculo(LARGURA, ALTURA, TAMANHO_OBSTACULO)]
                tempo_spawn = 0
                pygame.mixer.music.play(-1)  # reinicia música

    if not game_over:
        tempo += dt

        tempo_spawn += dt
        if tempo_spawn >= frequencia_spawn:
            obstaculos.append(
                Obstaculo(LARGURA, ALTURA, TAMANHO_OBSTACULO))
            tempo_spawn = 0

        teclas = pygame.key.get_pressed()
        jogador.mover(teclas, dt)

        for obstaculo in obstaculos:
            saiu = obstaculo.atualizar(dt, pontos)

            if saiu:
                pontos += 1

            if jogador.get_rect().colliderect(obstaculo.get_rect()):
                if pontos > recorde:
                    recorde = pontos

                pygame.mixer.music.stop()  # para música de fundo
                som_colisao.play()  # toca som de game over

                game_over = True

    tela.blit(fundo, (0, 0))


    for obstaculo in obstaculos:
        obstaculo.desenhar(tela)

    jogador.desenhar(tela)

    # 🔹 PONTOS
    texto_pontos = fonte_pequena.render(
        f"Pontos: {pontos}", True, BRANCO)
    tela.blit(texto_pontos, (10, 10))

    # 🔹 RECORDE
    texto_recorde = fonte_pequena.render(
        f"Recorde: {recorde}", True, AMARELO)
    tela.blit(texto_recorde, (10, 50))

    # 🔹 TEMPO
    texto_tempo = fonte_pequena.render(
        f"Tempo: {int(tempo)}s", True, CIANO)
    tela.blit(texto_tempo, (10, 90))

    if game_over:
        texto = fonte_grande.render("GAME OVER", True, VERMELHO)
        instrucoes = fonte_pequena.render(
            "Pressione R para reiniciar", True, BRANCO)

        tela.blit(texto, (LARGURA // 2 - texto.get_width() // 2, ALTURA // 2 - 60))
        tela.blit(instrucoes,
                  (LARGURA // 2 - instrucoes.get_width() // 2, ALTURA // 2 + 10))

    pygame.display.update()

pygame.quit()
sys.exit()