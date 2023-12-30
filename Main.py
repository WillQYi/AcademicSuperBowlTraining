import pygame

pygame.init()
screen = pygame.display.set_mode((1280,720),pygame.RESIZABLE)
clock = pygame.time.Clock()
running = True

def text(string, X, Y, size, color):
    font = pygame.font.Font('freesansbold.ttf', size)
    text = font.render(string, True, color)
    textRect = text.get_rect()
    textRect.center = (X,Y)
    screen.blit(text, textRect)

#Creates the homescreen
def homescreen():

    darkBlue = (53, 63, 112)

    titleTextSize = 50
    text("2023-2024 BHSS Academic Super Bowl", 640, 100, titleTextSize, darkBlue)
    text("Math Training Tool", 640, 160, titleTextSize, darkBlue)

    buttonTextSize = 30
    text("Training", 640, 350, buttonTextSize, darkBlue)
    text("Resources", 640, 480, buttonTextSize, darkBlue)

    pygame.draw.rect(screen, darkBlue, pygame.Rect(520, 300, 240, 100), 7, 10)
    pygame.draw.rect(screen, darkBlue, pygame.Rect(520, 430, 240, 100), 7, 10)
    #pygame.draw.rect(screen, buttonColor, pygame.Rect(640, 90, 90, 120))

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    screen.fill((230,230,230))

    homescreen()
    
    pygame.display.flip()

    clock.tick(60)

pygame.quit()
            