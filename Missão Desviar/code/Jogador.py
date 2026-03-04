import pygame
from code.const import BRANCO

class Jogador:
    def __init__(self, largura_tela):
        self.largura_tela = largura_tela

        #  Carrega a imagem
        self.imagem = pygame.image.load("asset/personagem.png").convert_alpha()
        self.imagem = pygame.transform.scale(self.imagem, (130, 130))

        # Cria rect baseado na imagem
        self.rect = self.imagem.get_rect()
        self.rect.centerx = largura_tela // 2
        self.rect.bottom = 580

        self.velocidade = 400

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
        # pygame.draw.rect(tela, BRANCO,
        #                  (self.x, self.y, self.largura, self.altura))
        tela.blit(self.imagem, self.rect)

    def get_rect(self):
        # return pygame.Rect(self.x, self.y, self.largura, self.altura)
        return self.rect
