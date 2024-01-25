import pygame
import Elements

#
# The following classes are used to draw/create specifics things to display or for users to interact with
#

#Draws text on a given screen
#Used for miscellaneous text
#X and Y are operations relative to the center
class TextDrawer:

    def __init__(self, screen, center_X, center_Y):
        self.screen = screen
        self.Texts = []
        self.center_X = center_X
        self.center_Y = center_Y
    
    #Creates a tuple that holds information about individual texts to draw
    def add(self, string, X, Y, size, color):
        self.Texts.append((string, X, Y, size, color))

    def draw(self, string, X, Y, size, color):
        font = pygame.font.Font('freesansbold.ttf', size)
        text = font.render(string, True, color)
        textRect = text.get_rect()
        textRect.center = (self.center_X+X,self.center_Y+Y)
        self.screen.blit(text, textRect)

    def drawAll(self):
        for i in range(len(self.Texts)):
            self.draw(self.Texts[i][0],self.Texts[i][1],self.Texts[i][2],self.Texts[i][3],self.Texts[i][4])

    def getTexts(self):
        for textTuple in self.Texts:
            print(textTuple)
        return self.Texts
    
    def recenter(self, center_X, center_Y):
        self.center_X = center_X
        self.center_Y = center_Y

# Creates a Button object which returns a event when pressed
# Note the drawing of the button is centerbased    
class Button:

    #Fix: Streamline inputs for button function
    def __init__(self, screen, X, Y, sizeX, sizeY, color, thickness, curveRadius, labelType, string, labelSize, center_X, center_Y, event):

        #Initial Variables
        self.runTick = 0

        # Inputed variables stored in the object
        self.screen = screen
        self.color = color
        self.curveRadius = curveRadius
        self.thickness = thickness
        self.sizeY = sizeY
        self.string = string
        self.labelSize = labelSize
        self.labelType = labelType
        self.event = event

        #Location variables
        self.X = X
        self.Y = Y
        self.center_X = center_X
        self.center_Y = center_Y
        self.sizeX = sizeX

        #Button Creation
        self.ButtonRect = pygame.Rect(center_X+X-sizeX/2, center_Y+Y-sizeY/2, sizeX, sizeY)
        self.label = Elements.Label(screen, labelSize, labelType, center_X+X, center_Y+Y, string, color)

    #Draws everything
    def draw(self):
        pygame.draw.rect(self.screen, self.color, self.ButtonRect, self.thickness, self.curveRadius)
        self.label.draw(self.center_X+self.X, self.center_Y+self.Y)

        #Button waiting after pressed and growing again
        if (self.runTick > 0):
            self.runTick += 1
            if (self.runTick == 10):
                #Makes button large again
                self.ButtonRect = self.ButtonRect.scale_by(10/9)
                self.label.changeSizeText(int(self.labelSize * 10/9))

                #Creates event to change screen
                #Fix: event creater/processing, don't know how to carry information with events, only can change the event type
                CUSTOMEVENT = pygame.event.Event(self.event)
                pygame.event.post(CUSTOMEVENT)
                self.runTick = 0
        else: 
            self.ButtonRect = pygame.Rect(self.center_X+self.X-self.sizeX/2, self.center_Y+self.Y-self.sizeY/2, self.sizeX, self.sizeY)

    #Runs/check if clicked
    def clicked(self, mousePos):
        if (self.ButtonRect.collidepoint(mousePos) and self.runTick == 0):
            self.runTick += 1
            self.ButtonRect = self.ButtonRect.scale_by(0.9)
            self.label.changeSizeText(int(self.labelSize * 9/10))
            return True
        else:
            return False

    def recenter(self, center_X, center_Y):
        self.center_X = center_X
        self.center_Y = center_Y
     
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
    
    def draw(self, X, Y):
        if (self.type == "text"):
            self.textRect.center = (X, Y)
            self.screen.blit(self.text, self.textRect)

    #Just changes the size for Text, so the shrinking button animation works
    def changeSizeText(self, size):
        self.font = pygame.font.Font('freesansbold.ttf', size)
        self.text = self.font.render(self.string, True, self.color)
        self.textRect = self.text.get_rect()
        self.textRect.center = (self.X, self.Y)