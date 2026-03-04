import pygame


class Jogador:

    def __init__(self, largura_tela):

        self.largura_tela = largura_tela

        #  Carrega a imagem
        self.imagem_vivo = pygame.image.load("asset/personagem.png").convert_alpha()
        self.imagem_vivo = pygame.transform.scale(self.imagem_vivo, (80, 80))

        # Imagem morto
        self.imagem_morto = pygame.image.load("asset/personagem_morto.png").convert_alpha()
        self.imagem_morto = pygame.transform.scale(self.imagem_morto, (80, 80))

        # Começa vivo
        self.imagem = self.imagem_vivo

        # Cria rect baseado na imagem
        self.rect = self.imagem.get_rect()
        self.rect.centerx = largura_tela // 2
        self.rect.bottom = 530

        self.velocidade = 400
        # Flag para controlar estado
        self.morto = False

    def morrer(self):
        self.imagem = self.imagem_morto
        self.morto = True

    def mover(self, teclas, dt):

        if teclas[pygame.K_LEFT]:
            self.rect.x -= self.velocidade * dt

        if teclas[pygame.K_RIGHT]:
            self.rect.x += self.velocidade * dt

        #  Limite da tela
        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.right > self.largura_tela:
            self.rect.right = self.largura_tela


    def desenhar(self, tela):
        tela.blit(self.imagem, self.rect)

    def get_rect(self):
        return self.rect
