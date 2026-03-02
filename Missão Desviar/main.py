import pygame

pygame.init()
# janela
window = pygame.display.set_mode(size=(640, 480))

#loop de repetição
while True:
    for event  in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit() # fechar a janela
            quit()
