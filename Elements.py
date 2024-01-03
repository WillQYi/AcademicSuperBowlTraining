import pygame

#Draws text on a given screen
class TextDrawer:

    def __init__(self, screen):
        self.screen = screen
        self.drawTexts = []
        pass

    def add(self, string, X, Y, size, color):
        self.drawTexts.append((string, X, Y, size, color))

    def drawOne(self, string, X, Y, size, color):
        font = pygame.font.Font('freesansbold.ttf', size)
        text = font.render(string, True, color)
        textRect = text.get_rect()
        textRect.center = (X,Y)
        self.screen.blit(text, textRect)

    def drawAll(self):
        for i in range(len(self.drawTexts)):
            self.drawOne(self.drawTexts[i][0],self.drawTexts[i][1],self.drawTexts[i][2],self.drawTexts[i][3],self.drawTexts[i][4])
    
        

    