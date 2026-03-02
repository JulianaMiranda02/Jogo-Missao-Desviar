
import pygame

from code.Menu import Menu


class Jogo:
    def __init__(self):
        pygame.init()
        # janela
        self.janela = pygame.display.set_mode(size=(640, 480))

    def executar(self):

        #loop de repetição
        while True:
            menu = Menu(self.janela)
            menu.executar()
            pass

            # for event  in pygame.event.get():
            #     if event.type == pygame.QUIT:
            #         pygame.quit() # fechar a janela
            #         quit()