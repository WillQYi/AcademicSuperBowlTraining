import pygame
import Elements

#Draws text on a given screen
#Used for miscellaneous text
class TextDrawer:

    def __init__(self, screen):
        self.screen = screen
        self.Texts = []

    def add(self, string, X, Y, size, color):
        self.Texts.append((string, X, Y, size, color))

    def draw(self, string, X, Y, size, color):
        font = pygame.font.Font('freesansbold.ttf', size)
        text = font.render(string, True, color)
        textRect = text.get_rect()
        textRect.center = (X,Y)
        self.screen.blit(text, textRect)

    def drawAll(self):
        for i in range(len(self.Texts)):
            self.draw(self.Texts[i][0],self.Texts[i][1],self.Texts[i][2],self.Texts[i][3],self.Texts[i][4])

    def getTexts(self):
        for textTuple in Texts:



# Creates a Button object which returns a event when pressed
# Note the drawing of the button is centerbased    
class Button:

    def __init__(self, screen, X, Y, sizeX, sizeY, color, thickness, curveRadius, labelType, string, labelSize):

        #Initial Variables
        self.runTick = 0

        # Inputed variables stored in the object
        self.screen = screen
        self.color = color
        self.curveRadius = curveRadius
        self.thickness = thickness
        self.X = X
        self.Y = Y
        self.sizeX = sizeX
        self.sizeY = sizeY
        self.string = string
        self.labelSize = labelSize
        self.labelType = labelType

        #Button Creation
        self.ButtonRect = pygame.Rect(X-sizeX/2, Y-sizeY/2, sizeX, sizeY)
        self.label = Elements.Label(screen, labelSize, labelType, X, Y, string, color)

    #Draws everything
    def draw(self):
        pygame.draw.rect(self.screen, self.color, self.ButtonRect, self.thickness, self.curveRadius)
        self.label.draw()
        if (self.runTick > 0):
            self.runTick += 1
            if (self.runTick == 60):
                self.ButtonRect = self.ButtonRect.scale_by(10/9)
                self.label.changeSize(int(self.labelSize * 10/9))
                self.runTick = 0

    #Runs/check if clicked
    def clicked(self, mousePos):
        if (self.ButtonRect.collidepoint(mousePos) and self.runTick == 0):
            self.runTick += 1
            self.ButtonRect = self.ButtonRect.scale_by(0.9)
            self.label.changeSize(int(self.labelSize * 9/10))
            return True
        else:
            return False
        
    def getPosition(self):
        return self.X, self.Y

    def getSize(self):
        return self.sizeX, self.sizeY



#Creates a label object which can be stuck on things like buttons
class Label:

    def __init__(self, screen, initSize, type, X, Y, string, color):
        if (type == "text"):

            #Initial Variables
            self.type = "text"

            # Inputed variables stored in the object
            self.screen = screen
            self.string = string
            self.font = pygame.font.Font('freesansbold.ttf', initSize)
            self.color = color
            self.X = X
            self.Y = Y
            self.text = self.font.render(string, True, color)
            self.textRect = self.text.get_rect()
            self.textRect.center = (X, Y)
    
    def draw(self):
        if (self.type == "text"):
            self.screen.blit(self.text, self.textRect)

    #Just changes the size, so the shrinking button animation works
    def changeSize(self, size):
        self.font = pygame.font.Font('freesansbold.ttf', size)
        self.text = self.font.render(self.string, True, self.color)
        self.textRect = self.text.get_rect()
        self.textRect.center = (self.X, self.Y)
