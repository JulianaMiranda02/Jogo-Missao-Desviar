import pygame
from code.const import BRANCO, AMARELO


class Menu:

    def __init__(self, largura, altura):

        self.largura = largura
        self.altura = altura

        self.fonte_titulo = pygame.font.SysFont(None, 90)
        self.fonte_texto = pygame.font.SysFont(None, 30)

    def desenhar(self, tela, fundo):

        tela.blit(fundo, (0, 0))

        titulo = self.fonte_titulo.render("MISSÃO DESVIAR", True, AMARELO)
        instrucoes = self.fonte_texto.render("Seu objetivo é desviar das pedras", True, AMARELO)

        controle1 = self.fonte_texto.render(
            "<-  Tecla direcional Esquerda: Mover para esquerda", True, BRANCO
        )

        controle2 = self.fonte_texto.render(
            "->  Tecla direcional Direita: Mover para direita", True, BRANCO
        )

        controle3 = self.fonte_texto.render(
            "ENTER  Iniciar jogo", True, BRANCO
        )

        controle4 = self.fonte_texto.render(
            "ESC  Sair do jogo", True, BRANCO
        )

        tela.blit(
            titulo,
            (self.largura // 2 - titulo.get_width() // 2, 150)
        )

        tela.blit(
            instrucoes,
            (self.largura // 2 - instrucoes.get_width() // 2, 250)
        )

        tela.blit(
            controle1,
            (self.largura // 2 - controle1.get_width() // 2, 300)
        )

        tela.blit(
            controle2,
            (self.largura // 2 - controle2.get_width() // 2, 340)
        )

        tela.blit(
            controle3,
            (self.largura // 2 - controle3.get_width() // 2, 420)
        )

        tela.blit(
            controle4,
            (self.largura // 2 - controle4.get_width() // 2, 460)
        )