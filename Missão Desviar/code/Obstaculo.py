import pygame
import random

class Obstaculo:

    def __init__(self, largura_tela, altura_tela, tamanho):
        # Guarda informações da tela para controlar limites
        self.largura_tela = largura_tela
        self.altura_tela = altura_tela
        self.tamanho = tamanho

        # Carrega a imagem do obstáculo (pedra)
        self.imagem = pygame.image.load("asset/pedra.png").convert_alpha()
        # Redimensiona a imagem para o tamanho definido
        self.imagem = pygame.transform.scale(self.imagem, (tamanho, tamanho))
        # Define posição inicial do obstáculo
        self.resetar()

    def resetar(self):
        self.y = -self.tamanho # Coloca o obstáculo acima da tela

        # Define posição horizontal aleatória
        self.x = random.randint(0, self.largura_tela - self.tamanho)

    def atualizar(self, dt, pontos):
        # Move o obstáculo para baixo
        # A velocidade aumenta conforme a pontuação
        self.y += (200 + pontos * 2) * dt

        # Se sair da tela, reaparece no topo
        if self.y > self.altura_tela:
            self.resetar()
            return True # indica que passou pela tela (serve para somar ponto)
        return False

    def desenhar(self, tela):
        # Desenha o obstáculo na tela
        tela.blit(self.imagem, (self.x, self.y))

    def get_rect(self):
        # Retorna o retângulo usado para detectar colisão com o jogador
        return self.imagem.get_rect(topleft=(self.x, self.y))