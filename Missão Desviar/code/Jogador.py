import pygame


class Jogador:

    def __init__(self, largura_tela):
        # Guarda a largura da tela para limitar o movimento do jogador
        self.largura_tela = largura_tela

        # Carrega a imagem do personagem vivo
        self.imagem_vivo = pygame.image.load("asset/personagem.png").convert_alpha()
        # Redimensiona a imagem para 80x80 pixels
        self.imagem_vivo = pygame.transform.scale(self.imagem_vivo, (80, 80))

        # Carrega a imagem do personagem morto
        self.imagem_morto = pygame.image.load("asset/personagem_morto.png").convert_alpha()
        self.imagem_morto = pygame.transform.scale(self.imagem_morto, (80, 80))

        # Define a imagem inicial como personagem vivo
        self.imagem = self.imagem_vivo

        # Cria o retângulo de colisão baseado no tamanho da imagem
        self.rect = self.imagem.get_rect()
        self.rect.centerx = largura_tela // 2 # Posiciona o jogador no centro horizontal da tela
        self.rect.bottom = 530 # Define posição vertical do jogador (parte inferior da tela)
        # Velocidade de movimento do jogador
        self.velocidade = 400
        # Flag para controlar estado
        self.morto = False # Flag para controlar se o jogador morreu

    def morrer(self):
        # Troca a imagem para personagem morto
        self.imagem = self.imagem_morto
        self.morto = True

    def mover(self, teclas, dt):
        # Movimento para esquerda
        if teclas[pygame.K_LEFT]:
            self.rect.x -= self.velocidade * dt
        # Movimento para direita
        if teclas[pygame.K_RIGHT]:
            self.rect.x += self.velocidade * dt

        # Impede o jogador de sair da tela
        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.right > self.largura_tela:
            self.rect.right = self.largura_tela


    def desenhar(self, tela):
        # Desenha o jogador na tela
        tela.blit(self.imagem, self.rect)

    def get_rect(self):
        # Retorna o retângulo para detecção de colisão
        return self.rect
