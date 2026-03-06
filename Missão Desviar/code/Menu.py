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

        tela.blit(
            credito1,
            (self.largura // 2 - credito1.get_width() // 2, 40)
        )

        tela.blit(
            credito2,
            (self.largura // 2 - credito2.get_width() // 2, 70)
        )

        tela.blit(
            credito3,
            (self.largura // 2 - credito3.get_width() // 2, 100)
        )

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


