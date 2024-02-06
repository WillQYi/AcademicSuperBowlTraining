import pygame
import Elements
import Expressions

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
    def add(self, string, X, Y, size, color, font):
        self.Texts.append((string, X, Y, size, color, font))

    def drawOne(self, string, X, Y, size, color, font):

        if (font.endswith("ttf")):
            self.font = pygame.font.Font(font, size)
        else:
            self.font = pygame.font.SysFont(font, size)
        text = self.font.render(string, True, color)
        textRect = text.get_rect()
    
        xOp = Expressions.locationOperationValue(X, self.center_X, self.center_Y)
        yOp = Expressions.locationOperationValue(Y, self.center_X, self.center_Y)

        textRect.center = (xOp,yOp)
        self.screen.blit(text, textRect)

    def draw(self):
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

        xOp = Expressions.locationOperationValue(X, self.center_X, self.center_Y)
        yOp = Expressions.locationOperationValue(Y, self.center_X, self.center_Y)
        self.sizeX = sizeX

        #Button Creation
        self.hasThickness = False
        if (thickness > 0):
            self.ButtonRectOutside = pygame.Rect(center_X+xOp-sizeX/2, center_Y+yOp-sizeY/2, sizeX, sizeY)
            self.hasThickness = True
        self.ButtonRectInside = pygame.Rect(center_X+xOp-sizeX/2, center_Y+yOp-sizeY/2, sizeX, sizeY)

        self.labels = []
        self.label = Elements.Label(screen, labelSize, labelType, center_X+xOp, center_Y+yOp, string, color[2], 'ariel')
        self.labels.append(self.label)
        if (not isWorking):
            self.crossLine = Elements.Label(screen, thickness, "line", center_X+xOp, center_Y+yOp, (sizeX, sizeY), color[0], 'ariel')
            self.labels.append(self.crossLine)

    #Draws everything
    def draw(self):
        pygame.draw.rect(self.screen, self.color[1], self.ButtonRectInside, 0, self.curveRadius)
        if (self.hasThickness):
            pygame.draw.rect(self.screen, self.color[0], self.ButtonRectOutside, self.thickness, self.curveRadius)
        for label in self.labels:
            label.draw()

        #Button waiting after pressed and growing again
        if (self.runTick > 0):
            self.runTick += 1
            if (self.runTick == 10):
                #Makes button large again
                if (self.hasThickness):
                    self.ButtonRectOutside = self.ButtonRectOutside.scale_by(10/9)
                self.ButtonRectInside = self.ButtonRectInside.scale_by(10/9)
                self.label.changeSize(10/9)

                #Creates event to change screen
                #Fix: event creater/processing, don't know how to carry information with events, only can change the event type
                CUSTOMEVENT = pygame.event.Event(self.event)
                pygame.event.post(CUSTOMEVENT)
                self.runTick = 0
        else: 
            xOp = Expressions.locationOperationValue(self.X, self.center_X, self.center_Y)
            yOp = Expressions.locationOperationValue(self.Y, self.center_X, self.center_Y)
            self.ButtonRectOutside = pygame.Rect(self.center_X+xOp-self.sizeX/2, self.center_Y+yOp-self.sizeY/2, self.sizeX, self.sizeY)
            self.ButtonRectInside= pygame.Rect(self.center_X+xOp-self.sizeX/2, self.center_Y+yOp-self.sizeY/2, self.sizeX, self.sizeY)

    #Runs/check if clicked
    def clicked(self, mousePos):
        if (self.ButtonRectOutside.collidepoint(mousePos) and self.runTick == 0):
            if (self.isWorking):
                self.runTick += 1
                self.changeSize(9/10)
            return True
        else:
            return False

    #Changes size of button
    def changeSize(self, scale):
        self.ButtonRectOutside = self.ButtonRectOutside.scale_by(scale)
        self.ButtonRectInside = self.ButtonRectInside.scale_by(scale)
        self.label.changeSize(scale)

    def recenter(self, center_X, center_Y):
        self.center_X = center_X
        self.center_Y = center_Y
        xOp = Expressions.locationOperationValue(self.X, self.center_X, self.center_Y)
        yOp = Expressions.locationOperationValue(self.Y, self.center_X, self.center_Y)
        for label in self.labels:
            label.recenter(center_X+xOp, center_Y+yOp)
     
    def getPosition(self):
        return self.X, self.Y

    def getSize(self):
        return self.sizeX, self.sizeY
    
    def changeColor(self, color):
        self.color = color


#Creates a label object which can be stuck on things like buttons
# not center or origin based, you put in the cords of the center of where you want to put the label
class Label:

    #Initializing function for labels of text and images 
    def __init__(self, screen, initSize, type, X, Y, otherInformation, color, font):
        if (type == "text"):

            #Initial Variables
            self.type = "text"

            # Inputed variables stored in the object
            self.screen = screen
            self.string = otherInformation
            self.labelSize = initSize
            self.X = X
            self.Y = Y

            if (font.endswith("ttf")):
                self.font = pygame.font.Font(font, initSize)
            else:
                self.font = pygame.font.SysFont(font, initSize)

            self.color = color
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
            self.font = pygame.font.SysFont('ariel', int(self.labelSize * scale))
            self.text = self.font.render(self.string, True, self.color)
            self.textRect = self.text.get_rect()
            self.textRect.center = (self.X, self.Y)
        elif (self.type == "image"):
            self.image = pygame.image.load(self.string)
            self.image = pygame.transform.scale_by(self.image, self.size*scale)
            self.imageRect = self.image.get_rect()
            self.imageRect.center = (self.X, self.Y)
    
    def changeText(self, text):
        self.text = self.font.render(text, True, self.color)
    
    def changeColor(self, color):
        self.color = color

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

#Note that this is center-based 
class inputTextBox:

    def __init__(self, screen, center_X, center_Y, X, Y, sizeX, sizeY, textInside):

        self.screen = screen
        self.isActive = False
        self.submitted = False
        self.isCorrect = False

        self.X = X
        self.Y = Y
        self.center_X = center_X
        self.center_Y = center_Y
        self.sizeX = sizeX
        self.sizeY = sizeY

        self.textInside = textInside

        self.inputtedText = ""

        xOp = Expressions.locationOperationValue(self.X, center_X, center_Y)
        yOp = Expressions.locationOperationValue(self.Y, center_X, center_Y)
        self.insideRect = pygame.Rect(center_X+xOp-self.sizeX/2, center_Y+yOp-self.sizeY/2, self.sizeX, self.sizeY)
        self.outsideRect = pygame.Rect(center_X+xOp-self.sizeX/2, center_Y+yOp-self.sizeY/2, self.sizeX, self.sizeY)
        self.activeRect = pygame.Rect(center_X+xOp-self.sizeX/2, center_Y+yOp-self.sizeY/2, self.sizeX, self.sizeY)
        self.correctRect = pygame.Rect(center_X+xOp-self.sizeX/2, center_Y+yOp-self.sizeY/2, self.sizeX, self.sizeY)

        self.label = Elements.Label(screen, 20,"text",center_X+xOp, center_Y+yOp, self.textInside, (200,200,200), 'calibri')
        self.label.recenter(center_X+xOp-(self.sizeX/2-10-self.label.textRect.width/2), center_Y+yOp)

        pass

    def draw(self):
        pygame.draw.rect(self.screen, (255,255,255), self.insideRect, 0, 3)

        if (self.submitted):
            if (self.isCorrect):
                pygame.draw.rect(self.screen, (140,250,150), self.correctRect, 0, 3)
                self.label.changeColor((50, 150, 60))
            else:
                pygame.draw.rect(self.screen, (250,145,145), self.correctRect, 0, 3)
                self.label.changeColor((170, 20, 20))

        pygame.draw.rect(self.screen, (100,100,100), self.outsideRect, 3, 3)

        if (self.isActive):
            pygame.draw.rect(self.screen, (55, 190, 245), self.activeRect, 3, 3)
        self.label.draw()

        if (len(self.inputtedText) > 0):
            self.label.changeText(self.inputtedText)
            self.label.changeColor((0,0,0))
        else:
            if (len(self.inputtedText) == 0):
                self.label.changeText(self.textInside)
                self.label.changeColor((200,200,200))
            else: 
                self.label.changeText("")
        pass

    def clicked(self, mousePos):
        if (self.activeRect.collidepoint(mousePos)):
            self.isActive = True
            return True
        else:
            self.isActive = False
            return False
        
    def inputText(self, event):
        if event.key == pygame.K_RETURN:
            self.isActive = False
            pass
        elif event.key == pygame.K_BACKSPACE:
            if (len(self.inputtedText) == 1):
                self.inputtedText = ""
            else:
                self.inputtedText = self.inputtedText[:-1]
        else:
            self.inputtedText += event.unicode  

    def recenter(self, center_X, center_Y):
        self.center_X = center_X
        self.center_Y = center_Y
        xOp = Expressions.locationOperationValue(self.X, center_X, center_Y)
        yOp = Expressions.locationOperationValue(self.Y, center_X, center_Y)
        self.insideRect = pygame.Rect(center_X+xOp-self.sizeX/2, center_Y+yOp-self.sizeY/2, self.sizeX, self.sizeY)
        self.outsideRect = pygame.Rect(center_X+xOp-self.sizeX/2, center_Y+yOp-self.sizeY/2, self.sizeX, self.sizeY)
        self.activeRect = pygame.Rect(center_X+xOp-self.sizeX/2, center_Y+yOp-self.sizeY/2, self.sizeX, self.sizeY)
        self.correctRect = pygame.Rect(center_X+xOp-self.sizeX/2, center_Y+yOp-self.sizeY/2, self.sizeX, self.sizeY)
        self.label.recenter(center_X+xOp-(self.sizeX/2-10-self.label.textRect.width/2), center_Y+yOp)
        pass 

    def submit(self, isCorrect):
        self.submitted = True
        self.isCorrect = isCorrect
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
        cord = Expressions.locationOperationValue(self.cord, self.center_X, self.center_Y)
        if (self.type == "horizontal"):
            pygame.draw.line(self.screen, self.color, (0,cord), (2*self.center_X,cord), self.thickness)
        elif (self.type == "vertical"):
            pygame.draw.line(self.screen, self.color, (cord,0), (cord,2*self.center_Y), self.thickness)

    def recenter(self, X, Y):
        self.center_X = X
        self.center_Y = Y

#origin based
class problemNumberBox:

    def __init__(self, screen, X, Y, sizeX, sizeY, problemNumber, color):
        
        self.screen = screen
        self.submitted = False

        self.X = X
        self.Y = Y

        self.sizeX = sizeX
        self.sizeY = sizeY

        self.color = color

        self.boxOutlineRect = pygame.Rect(X, Y, sizeX, sizeY)
        self.boxFillRect = pygame.Rect(X, Y, sizeX, sizeY)

        self.label = Elements.Label(screen, 30, "text", X+sizeX/2, Y+sizeY/2, problemNumber, color, 'ariel')

    def draw(self):
        pygame.draw.rect(self.screen, (255,255,255), self.boxOutlineRect, 0, 0)
        pygame.draw.rect(self.screen, self.color, self.boxOutlineRect, 7, 0)
        self.label.draw()

    def recenter(self, X, Y):
        self.X = X
        self.Y = Y

class problemController():

    def __init__(self, screen, center_X, center_Y, color):

        self.screen = screen
        self.color = color
        self.submitted = False

        self.answer = []

        self.center_X = center_X
        self.center_Y = center_Y
        self.TextDrawer = TextDrawer(screen, center_X, center_Y)
        pass

    def loadProblemDisplay(self, problem):

        self.problem = problem

        question = problem.getQuestion()

        type = problem.problemDisplayType

        if (type == "equations"):
            
            self.questionDisplayType = type

            spacing = 100

            topHieght = -1*float((len(question)-2))/2 * spacing -25

            for i in range(len(question)-1):
                self.TextDrawer.add(question[i], "cX", "cY+" + str(topHieght+spacing*i), 60, self.color, "ariel")
            
            self.TextDrawer.add(question[len(question)-1], 120+(len(question[len(question)-1])/2)*20, 175, 60, self.color, "ariel")

    def loadProblemInput(self, type):
        
        self.inputType = type

        self.inputElements = []

        if (type[0] == "textBox"):
            if (type[1] == 1):
                self.textBox1 = Elements.inputTextBox(self.screen, self.center_X, self.center_Y, 0, "cY-88", 700, 50, "Type Answer")
                self.inputElements.append(self.textBox1)
            elif (type[1] == 2):
                self.textBox1 = Elements.inputTextBox(self.screen, self.center_X, self.center_Y, 250, "cY-88", 400, 50, "Type Answer")
                self.textBox2 = Elements.inputTextBox(self.screen, self.center_X, self.center_Y, -250, "cY-88", 400, 50, "Type Answer")
                self.inputElements.append(self.textBox1)
                self.inputElements.append(self.textBox2)
            elif (type[1] == 3):
                self.textBox1 = Elements.inputTextBox(self.screen, self.center_X, self.center_Y, 400, "cY-88", 300, 50, "Type Answer")
                self.textBox2 = Elements.inputTextBox(self.screen, self.center_X, self.center_Y, 0, "cY-88", 300, 50, "Type Answer")
                self.textBox3 = Elements.inputTextBox(self.screen, self.center_X, self.center_Y, -400, "cY-88", 300, 50, "Type Answer")

                self.inputElements.append(self.textBox1)
                self.inputElements.append(self.textBox2)
                self.inputElements.append(self.textBox3)

    def checkCorrect(self):

        #self.submitted = True
        self.answer = []
        for textbox in self.inputElements:
            self.answer.append(textbox.inputtedText)
        self.answer.reverse()
        self.correctList = self.problem.checkCorrect(self.answer)
        print(self.answer)
        for i in range(len(self.correctList)):
            print(self.correctList[i])
            (self.inputElements[i]).submit(self.correctList[i])
        pass
    
    def draw(self):
        if (self.questionDisplayType == "equations"):
            self.TextDrawer.draw()

        for element in self.inputElements:
            element.draw()
    
    def recenter(self, center_X, center_Y):
        self.center_X = center_X
        self.center_Y = center_Y
        self.TextDrawer.recenter(center_X, center_Y)

        for element in self.inputElements:
            element.recenter(center_X, center_Y)