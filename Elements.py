import pygame
import Elements

#
# The following classes are used to draw/create specifics things to display or for users to interact with
#

#Draws text on a given screen
#Used for miscellaneous text
#X and Y are operations relative to the center

#Element template 
'''
class Element:

    def __init__(self, screen, X, Y):
        
        self.screen = screen

        self.center_X = X
        self.center_Y = Y

    def draw(self):
        pass

    def recenter(self, X, Y):
        self.center_X = X
        self.center_Y = Y
'''

class TextDrawer:

    def __init__(self, screen, center_X, center_Y):
        self.screen = screen
        self.Texts = []
        self.center_X = center_X
        self.center_Y = center_Y
    
    #Creates a tuple that holds information about individual texts to draw
    def add(self, string, X, Y, size, color, type):
        self.Texts.append((string, X, Y, size, color, type))

    def drawOne(self, string, X, Y, size, color, type):
        font = pygame.font.Font('freesansbold.ttf', size)
        text = font.render(string, True, color)
        textRect = text.get_rect()
        if (type == "center"):
            textRect.center = (self.center_X+X,self.center_Y+Y)
        elif (type == "origin"):
            textRect.center = (X,Y)
        self.screen.blit(text, textRect)

    def drawAll(self):
        for i in range(len(self.Texts)):
            self.drawOne(self.Texts[i][0],self.Texts[i][1],self.Texts[i][2],self.Texts[i][3],self.Texts[i][4],self.Texts[i][5])

    def getTexts(self):
        for textTuple in self.Texts:
            print(textTuple)
        return self.Texts
    
    def recenter(self, center_X, center_Y):
        self.center_X = center_X
        self.center_Y = center_Y
    
    def clear(self):
        self.Texts = []

# Creates a Button object which returns a event when pressed
# Note the drawing of the button is center based    
class Button:

    #Fix: Streamline inputs for button function
    def __init__(self, screen, X, Y, sizeX, sizeY, color, thickness, curveRadius, labelType, string, labelSize, center_X, center_Y, event, isWorking):

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
        self.isWorking = isWorking

        #Location variables
        self.X = X
        self.Y = Y
        self.center_X = center_X
        self.center_Y = center_Y
        self.sizeX = sizeX

        #Button Creation
        self.ButtonRect = pygame.Rect(center_X+X-sizeX/2, center_Y+Y-sizeY/2, sizeX, sizeY)

        self.labels = []
        self.label = Elements.Label(screen, labelSize, labelType, center_X+X, center_Y+Y, string, color)
        self.labels.append(self.label)
        if (not isWorking):
            self.crossLine = Elements.Label(screen, thickness, "line", center_X+X, center_Y+Y, (sizeX, sizeY), color)
            self.labels.append(self.crossLine)

    #Draws everything
    def draw(self):
        pygame.draw.rect(self.screen, self.color, self.ButtonRect, self.thickness, self.curveRadius)
        for label in self.labels:
            label.draw()

        #Button waiting after pressed and growing again
        if (self.runTick > 0):
            self.runTick += 1
            if (self.runTick == 10):
                #Makes button large again
                self.ButtonRect = self.ButtonRect.scale_by(10/9)
                self.label.changeSize(10/9)

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
            if (self.isWorking):
                self.runTick += 1
                self.changeSize(9/10)
            return True
        else:
            return False

    #Changes size of button
    def changeSize(self, scale):
        self.ButtonRect = self.ButtonRect.scale_by(scale)
        self.label.changeSize(scale)

    def recenter(self, center_X, center_Y):
        self.center_X = center_X
        self.center_Y = center_Y
        for label in self.labels:
            label.recenter(center_X+self.X, center_Y+self.Y)
     
    def getPosition(self):
        return self.X, self.Y

    def getSize(self):
        return self.sizeX, self.sizeY

#Creates a label object which can be stuck on things like buttons
# not center or origin based, you put in the cords of the center of where you want to put the label
class Label:

    #Initializing function for labels of text and images 
    def __init__(self, screen, initSize, type, X, Y, otherInformation, color):
        if (type == "text"):

            #Initial Variables
            self.type = "text"

            # Inputed variables stored in the object
            self.screen = screen
            self.string = otherInformation
            self.labelSize = initSize
            self.font = pygame.font.Font('freesansbold.ttf', initSize)
            self.color = color
            self.X = X
            self.Y = Y
            self.text = self.font.render(otherInformation, True, color)
            self.textRect = self.text.get_rect()
            self.textRect.center = (X, Y)

        elif (type == "image"):

            #Initial Variables
            self.type = "image"

            # Inputed variables stored in the object
            self.screen = screen
            self.string = otherInformation
            self.X = X
            self.Y = Y
            self.size = initSize
            self.image = pygame.image.load(otherInformation)
            self.image = pygame.transform.scale_by(self.image, initSize)
            self.imageRect = self.image.get_rect()
            self.imageRect.center = (X, Y)

        #I really only used this label to cross out buttons that don't work
        #The other information in this case is the size of button
        elif (type == "line"):

            self.screen = screen
            self.thickness = initSize
            self.type = "line"
            self.color = color

            self.X = X
            self.Y = Y
            self.horiDis = int(otherInformation[0]/2)
            self.vertDis = int(otherInformation[1]/2)
    
    def draw(self):
        if (self.type == "text"):
            self.textRect.center = (self.X, self.Y)
            self.screen.blit(self.text, self.textRect)
        elif (self.type == "image"):
            self.imageRect.center = (self.X, self.Y)
            self.screen.blit(self.image, self.imageRect)
        if (self.type == "line"):
            pygame.draw.line(self.screen, self.color, (self.X - self.horiDis +  6, self.Y - self.vertDis + 6), (self.X + self.horiDis -  6, self.Y + self.vertDis - 6), self.thickness)

    #Just changes the size for label, so the shrinking button animation works
    def changeSize(self, scale):
        if (self.type == "text"):
            self.font = pygame.font.Font('freesansbold.ttf', int(self.labelSize * scale))
            self.text = self.font.render(self.string, True, self.color)
            self.textRect = self.text.get_rect()
            self.textRect.center = (self.X, self.Y)
        elif (self.type == "image"):
            self.image = pygame.image.load(self.string)
            self.image = pygame.transform.scale_by(self.image, self.size*scale)
            self.imageRect = self.image.get_rect()
            self.imageRect.center = (self.X, self.Y)
    
    def recenter(self, X, Y):
        if (self.type == "text"):
            self.X = X
            self.Y = Y
        elif (self.type == "image"):
            self.X = X
            self.Y = Y
        if (self.type == "line"):
            self.X = X
            self.Y = Y

class inputTextBox:

    def __init__(self, screen, X, Y, sizeX, sizeY):
        pass

    def draw(self):
        pass

    def recenter(self):
        pass

class divider:

    def __init__(self, screen, type, center_X, center_Y, cord, thickness, color):

        self.screen = screen
        
        self.type = type

        self.center_X= center_X
        self.center_Y = center_Y

        self.cord = cord

        self.color = color

        self.thickness = thickness

    def draw(self):
        if (self.type == "horizontal"):
            pygame.draw.line(self.screen, self.color, (0,self.cord), (2*self.center_X,self.cord), self.thickness)
        elif (self.type == "vertical"):
            pygame.draw.line(self.screen, self.color, (self.cord,0), (self.cord,2*self.center_Y), self.thickness)

    def recenter(self, X, Y):
        self.center_X = X
        self.center_Y = Y

#origin based
class problemNumberBox:

    def __init__(self, screen, X, Y, sizeX, sizeY, problemNumber, color):
        
        self.screen = screen

        self.X = X
        self.Y = Y

        self.sizeX = sizeX
        self.sizeY = sizeY

        self.color = color

        self.boxOutlineRect = pygame.Rect(X, Y, sizeX, sizeY)
        self.boxFillRect = pygame.Rect(X, Y, sizeX, sizeY)

        self.label = Elements.Label(screen, 30, "text", X+sizeX/2, Y+sizeY/2, problemNumber, color)

    def draw(self):
        pygame.draw.rect(self.screen, (255,255,255), self.boxOutlineRect, 0, 0)
        pygame.draw.rect(self.screen, self.color, self.boxOutlineRect, 7, 0)
        self.label.draw()

    def recenter(self, X, Y):
        self.X = X
        self.Y = Y