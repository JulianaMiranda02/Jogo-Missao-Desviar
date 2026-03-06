import pygame
from code.Const import BRANCO, AMARELO


class Menu:

    def __init__(self, largura, altura):
        # Guarda o tamanho da tela para centralizar os textos
        self.largura = largura
        self.altura = altura
        # Fonte do título principal do menu
        self.fonte_titulo = pygame.font.SysFont(None, 90)
        self.fonte_texto = pygame.font.SysFont(None, 30)
        self.fonte_credito = pygame.font.SysFont("verdana", 18, bold=True)

    def desenhar(self, tela, fundo):
        # Desenha o fundo do jogo na tela
        tela.blit(fundo, (0, 0))

        credito1 = self.fonte_credito.render("Desenvolvido por", True, BRANCO)
        credito2 = self.fonte_credito.render("Juliana Miranda de Almeida Abreu", True, BRANCO)
        credito3 = self.fonte_credito.render("RU: 4913555", True, BRANCO)

        # sombras
        credito1_sombra = self.fonte_credito.render("Desenvolvido por", True, (0, 0, 0))
        credito2_sombra = self.fonte_credito.render("Juliana Miranda de Almeida Abreu", True, (0, 0, 0))
        credito3_sombra = self.fonte_credito.render("RU: 4913555", True, (0, 0, 0))

        # Cria os textos do menu
        titulo = self.fonte_titulo.render("MISSÃO DESVIAR", True, AMARELO)
        instrucoes = self.fonte_texto.render("Seu objetivo é desviar das pedras", True, AMARELO)

        # Controles do jogo
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

        x1 = self.largura // 2 - credito1.get_width() // 2
        x2 = self.largura // 2 - credito2.get_width() // 2
        x3 = self.largura // 2 - credito3.get_width() // 2

        y1 = 40
        y2 = 70
        y3 = 100

        # sombra
        tela.blit(credito1_sombra, (x1 + 2, y1 + 2))
        tela.blit(credito2_sombra, (x2 + 2, y2 + 2))
        tela.blit(credito3_sombra, (x3 + 2, y3 + 2))

        # texto principal
        tela.blit(credito1, (x1, y1))
        tela.blit(credito2, (x2, y2))
        tela.blit(credito3, (x3, y3))

        # Desenha o título centralizado na tela
        tela.blit(
            titulo,
            (self.largura // 2 - titulo.get_width() // 2, 170)
        )
        # Desenha instruções do jogo
        tela.blit(
            instrucoes,
            (self.largura // 2 - instrucoes.get_width() // 2, 260)
        )
        # Desenha os controles do jogador
        tela.blit(
            controle1,
            (self.largura // 2 - controle1.get_width() // 2, 310)
        )

        tela.blit(
            controle2,
            (self.largura // 2 - controle2.get_width() // 2, 350)
        )
        # Opções do menu (iniciar ou sair)
        tela.blit(
            controle3,
            (self.largura // 2 - controle3.get_width() // 2, 430)
        )

        tela.blit(
            controle4,
            (self.largura // 2 - controle4.get_width() // 2, 470)
        )


