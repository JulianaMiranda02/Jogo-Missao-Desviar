import pygame
import sys
from code.Jogador import Jogador
from code.Menu import Menu
from code.Obstaculo import Obstaculo
from code.const import (
    LARGURA, ALTURA, FPS, TAMANHO_OBSTACULO,
    BRANCO, AMARELO, CIANO, VERMELHO
)

pygame.mixer.pre_init(44100, -16, 2, 512)
pygame.init()
pygame.mixer.init()
print("Mixer inicializado:", pygame.mixer.get_init())

tela = pygame.display.set_mode((LARGURA, ALTURA))
clock = pygame.time.Clock()

menu = Menu(LARGURA, ALTURA)
estado = "menu"  # estados: menu, jogando, game_over

fundo = pygame.image.load("asset/forest_bridge.png")
fundo = pygame.transform.scale(fundo, (LARGURA, ALTURA))

pygame.mixer.music.load("asset/somdojogo.wav")
pygame.mixer.music.set_volume(0.5)
pygame.mixer.music.play(-1)

som_colisao = pygame.mixer.Sound("asset/gameover.wav")

# Inicializa jogador e obstáculos
jogador = Jogador(LARGURA)
obstaculos = [Obstaculo(LARGURA, ALTURA, TAMANHO_OBSTACULO)]

# Variáveis do jogo
pontos = 0
recorde = 0
tempo = 0
tempo_spawn = 0
frequencia_spawn = 20

fonte_grande = pygame.font.SysFont(None, 80)
fonte_pequena = pygame.font.SysFont(None, 40)

rodando = True

while rodando:

    dt = clock.tick(FPS) / 1000

    # Processa eventos
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            rodando = False

        # MENU
        if estado == "menu" and evento.type == pygame.KEYDOWN:
            if evento.key == pygame.K_RETURN:
                estado = "jogando"
            if evento.key == pygame.K_ESCAPE:
                rodando = False

        # GAME OVER
        if estado == "game_over" and evento.type == pygame.KEYDOWN:
            if evento.key == pygame.K_r:
                # reinicia jogo
                pontos = 0
                tempo = 0
                jogador = Jogador(LARGURA)
                obstaculos = [Obstaculo(LARGURA, ALTURA, TAMANHO_OBSTACULO)]
                tempo_spawn = 0
                pygame.mixer.music.play(-1)
                estado = "jogando"

    # 🔹 MENU (trava o loop aqui até o jogador apertar ENTER)
    if estado == "menu":
        menu.desenhar(tela, fundo)
        pygame.display.update()
        continue  # ESSENCIAL para não rodar código do jogo enquanto menu ativo

    # 🔹 LÓGICA DO JOGO
    if estado == "jogando":
        tempo += dt
        tempo_spawn += dt

        # spawn obstáculos
        if tempo_spawn >= frequencia_spawn:
            obstaculos.append(Obstaculo(LARGURA, ALTURA, TAMANHO_OBSTACULO))
            tempo_spawn = 0

        # aumenta dificuldade com o tempo
        if tempo_spawn > 60:
            frequencia_spawn = 15
        if tempo_spawn > 120:
            frequencia_spawn = 10
        if tempo_spawn > 180:
            frequencia_spawn = 5

        # mover jogador
        teclas = pygame.key.get_pressed()
        jogador.mover(teclas, dt)

        # atualizar obstáculos
        for obstaculo in obstaculos:
            saiu = obstaculo.atualizar(dt, pontos)
            if saiu:
                pontos += 1

            # colisão
            if jogador.get_rect().colliderect(obstaculo.get_rect()):
                if pontos > recorde:
                    recorde = pontos

                pygame.mixer.music.stop()
                som_colisao.play()
                jogador.morrer()
                estado = "game_over"

    # 🔹 DESENHO
    tela.blit(fundo, (0, 0))
    for obstaculo in obstaculos:
        obstaculo.desenhar(tela)
    jogador.desenhar(tela)

    # pontuação, recorde e tempo
    tela.blit(fonte_pequena.render(f"Pontos: {pontos}", True, BRANCO), (10, 10))
    tela.blit(fonte_pequena.render(f"Recorde: {recorde}", True, AMARELO), (10, 50))
    tela.blit(fonte_pequena.render(f"Tempo: {int(tempo)}s", True, CIANO), (10, 90))

    # game over
    if estado == "game_over":
        texto = fonte_grande.render("GAME OVER", True, VERMELHO)
        instrucoes = fonte_pequena.render("Pressione R para reiniciar", True, BRANCO)
        tela.blit(texto, (LARGURA // 2 - texto.get_width() // 2, ALTURA // 2 - 60))
        tela.blit(instrucoes, (LARGURA // 2 - instrucoes.get_width() // 2, ALTURA // 2 + 10))

    pygame.display.update()

pygame.quit()
sys.exit()