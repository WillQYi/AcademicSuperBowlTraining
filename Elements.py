import pygame

#Draws text on a given screen
class TextDrawer:

    def __init__(self, screen):
        self.screen = screen
        self.drawTexts = []

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

# Creates a buttonObject which returns a event 
# Note the drawing of the button is centerbased    
class Button:

    def __init__(self, screen, X, Y, sizeX, sizeY, color, thickness, curveRadius):
        self.screen = screen
        self.running = False
        self.color = color
        self.curveRadius = curveRadius
        self.thickness = thickness
        self.ButtonRect = pygame.Rect(X-sizeX/2, Y-sizeY/2, sizeX, sizeY)

    def draw(self):
        pygame.draw.rect(self.screen, self.color, self.ButtonRect, self.thickness, self.curveRadius) 

    def clicked(self, mousePos):
        if (self.ButtonRect.collidepoint(mousePos) and not self.running):
            self.running = True
            self.PressedAnimation()
            return True
        else:
            return False
        
    def PressedAnimation(self):
        print("Running...")
        self.ButtonRect.scale_by(0.8)
        self.draw()
        '''
        pygame.display.update()
        pygame.time.wait(300)
        self.ButtonRect.scale_by(1.25)
        self.draw()
        pygame.display.update()
        '''
        self.running = False
        return
        
