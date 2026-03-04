import pygame
import random
from code.const import VERMELHO

class Obstaculo:
    def __init__(self, largura_tela, altura_tela, tamanho):
        self.largura_tela = largura_tela
        self.altura_tela = altura_tela
        self.tamanho = tamanho

        #  carregar imagem da pedra
        self.imagem = pygame.image.load("asset/pedra.png").convert_alpha()
        self.imagem = pygame.transform.scale(self.imagem, (tamanho, tamanho))

        self.resetar()

    def resetar(self):
        self.y = -self.tamanho
        self.x = random.randint(0, self.largura_tela - self.tamanho)

    def atualizar(self, dt, pontos):
        self.y += (200 + pontos * 2) * dt

        if self.y > self.altura_tela:
            self.resetar()
            return True
        return False

    def desenhar(self, tela):
        # pygame.draw.rect(tela, VERMELHO,
        #                  (self.x, self.y, self.tamanho, self.tamanho))
        tela.blit(self.imagem, (self.x, self.y))

    def get_rect(self):
        return self.imagem.get_rect(topleft=(self.x, self.y))