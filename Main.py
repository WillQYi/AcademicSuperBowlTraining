import pygame
import Elements
import Screens

pygame.init()
screen = pygame.display.set_mode((1280,720),pygame.RESIZABLE)
clock = pygame.time.Clock()
running = True
Buttons = []

center_X = 640
center_Y = 360
#homescreen = Screens.homescreen(screen, center_X, center_Y)
practiceSelectScreen = Screens.practiceSelectScreen(screen, center_X, center_Y)

while running:
    for event in pygame.event.get():
        #print(event)
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.MOUSEBUTTONUP:
            mousePos = pygame.mouse.get_pos()
            for Button in practiceSelectScreen.Interactive:
                Button.clicked(mousePos)

    #print("-----------")   
    
    screen.fill((230,230,230))

    center_X = pygame.display.get_window_size()[0]/2
    center_Y = pygame.display.get_window_size()[1]/2
    
    practiceSelectScreen.draw(center_X, center_Y)

    pygame.display.flip()

    clock.tick(60)

pygame.quit()
