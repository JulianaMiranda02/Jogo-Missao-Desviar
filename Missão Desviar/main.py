import pygame
import sys
# Importa as classes do jogo
from code.Jogador import Jogador
from code.Menu import Menu
from code.Obstaculo import Obstaculo

# Importa constantes definidas no arquivo const.py
from code.const import (
    LARGURA, ALTURA, FPS, TAMANHO_OBSTACULO,
    BRANCO, AMARELO, CIANO, VERMELHO
)
# Pré-configuração do sistema de áudio do pygame
pygame.mixer.pre_init(44100, -16, 2, 512)

# Inicializa todos os módulos do pygame
pygame.init()
pygame.mixer.init()
print("Mixer inicializado:", pygame.mixer.get_init())

# Cria a janela do jogo com largura e altura definidas
tela = pygame.display.set_mode((LARGURA, ALTURA))

# Controla o FPS do jogo
clock = pygame.time.Clock()

# Cria o menu principal
menu = Menu(LARGURA, ALTURA)
estado = "menu"  # estados: menu, jogando, game_over
# Carrega a imagem de fundo do jogo
fundo = pygame.image.load("asset/forest_bridge.png")
# Ajusta a imagem para o tamanho da tela
fundo = pygame.transform.scale(fundo, (LARGURA, ALTURA))

# Carrega a música de fundo
pygame.mixer.music.load("asset/somdojogo.wav")
# Define o volume da música
pygame.mixer.music.set_volume(0.5)
# Reproduz a música em loop infinito
pygame.mixer.music.play(-1)

# Carrega o som de colisão (game over)
som_colisao = pygame.mixer.Sound("asset/gameover.wav")

# Inicializa o jogador
jogador = Jogador(LARGURA)

# Cria a lista de obstáculos (começa com 1)
obstaculos = [Obstaculo(LARGURA, ALTURA, TAMANHO_OBSTACULO)]

# Variáveis do jogo
pontos = 0
recorde = 0
tempo = 0
tempo_spawn = 0 # tempo para gerar novo obstáculo
frequencia_spawn = 20 # frequência de spawn dos obstáculos

# Fontes para os textos do jogo
fonte_grande = pygame.font.SysFont(None, 80)
fonte_pequena = pygame.font.SysFont(None, 40)

# Variável principal do loop do jogo
rodando = True
# LOOP PRINCIPAL DO JOGO
while rodando:
    # Controla a velocidade do jogo usando FPS
    dt = clock.tick(FPS) / 1000

    # Processa eventos (teclado, fechar janela, etc)
    for evento in pygame.event.get():
        # Se fechar a janela
        if evento.type == pygame.QUIT:
            rodando = False

        # EVENTOS DO MENU
        if estado == "menu" and evento.type == pygame.KEYDOWN:
            # ENTER inicia o jogo
            if evento.key == pygame.K_RETURN:
                estado = "jogando"
                # ESC fecha o jogo
            if evento.key == pygame.K_ESCAPE:
                rodando = False

        # EVENTOS DO GAME OVER
        if estado == "game_over" and evento.type == pygame.KEYDOWN:
            # Pressionar R reinicia o jogo
            if evento.key == pygame.K_r:
                pontos = 0
                tempo = 0
                # recria jogador
                jogador = Jogador(LARGURA)
                # recria obstáculos
                obstaculos = [Obstaculo(LARGURA, ALTURA, TAMANHO_OBSTACULO)]
                tempo_spawn = 0
                # toca música novamente
                pygame.mixer.music.play(-1)
                estado = "jogando"

     # MENU
    if estado == "menu":
        menu.desenhar(tela, fundo) # desenha o menu na tela
        pygame.display.update()
        continue  # impede o jogo de rodar enquanto estiver no menu

    # 🔹 LÓGICA DO JOGO
    if estado == "jogando":
        # atualiza o tempo de jogo
        tempo += dt
        tempo_spawn += dt

        # cria novos obstáculos com base no tempo
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

        # captura teclas pressionadas
        teclas = pygame.key.get_pressed()
        jogador.mover(teclas, dt)  # move o jogador

        # atualizar obstáculos
        for obstaculo in obstaculos:
            # move obstáculo
            saiu = obstaculo.atualizar(dt, pontos)
            # se saiu da tela aumenta pontuação
            if saiu:
                pontos += 1

            # verifica colisão entre jogador e obstáculo
            if jogador.get_rect().colliderect(obstaculo.get_rect()):
                # atualiza recorde
                if pontos > recorde:
                    recorde = pontos

                pygame.mixer.music.stop() # para música
                som_colisao.play() # toca som de colisão
                jogador.morrer()  # executa animação de morte
                estado = "game_over" # muda estado para game over

    # 🔹 DESENHO NA TELA
    tela.blit(fundo, (0, 0))  # desenha fundo
    # desenha obstáculos
    for obstaculo in obstaculos:
        obstaculo.desenhar(tela)
    jogador.desenhar(tela)  # desenha jogador

    # mostra pontuação, recorde e tempo de jogo
    tela.blit(fonte_pequena.render(f"Pontos: {pontos}", True, BRANCO), (10, 10))
    tela.blit(fonte_pequena.render(f"Recorde: {recorde}", True, AMARELO), (10, 50))
    tela.blit(fonte_pequena.render(f"Tempo: {int(tempo)}s", True, CIANO), (10, 90))

    # TELA DE GAME OVER
    if estado == "game_over":
        texto = fonte_grande.render("GAME OVER", True, VERMELHO)
        instrucoes = fonte_pequena.render("Pressione R para reiniciar", True, BRANCO)
        tela.blit(texto, (LARGURA // 2 - texto.get_width() // 2, ALTURA // 2 - 60))
        tela.blit(instrucoes, (LARGURA // 2 - instrucoes.get_width() // 2, ALTURA // 2 + 10))

    pygame.display.update() # atualiza tela

pygame.quit() # finaliza pygame
sys.exit() # encerra programa