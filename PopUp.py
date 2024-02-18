import pygame
import Elements
import PopUp

class popUpRect:

    def __init__ (self, screen, center_X, center_Y, colors, sizeX, sizeY):

        self.screen = screen

        self.colors = colors

        self.center_X = center_X
        self.center_Y = center_Y

        self.sizeX = sizeX
        self.sizeY = sizeY

        self.rect = pygame.Rect(center_X-self.sizeX/2, center_Y-self.sizeY/2, self.sizeX, self.sizeY)
    
    def draw(self):
        pygame.draw.rect(self.screen, self.colors["screenGrey"], self.rect, 0, 10)
        pygame.draw.rect(self.screen, self.colors["darkBlue"], self.rect, 6, 10)

    def recenter(self, center_X, center_Y):
        self.center_X = center_X
        self.center_Y = center_Y
        self.rect = pygame.Rect(center_X-self.sizeX/2, center_Y-self.sizeY/2, self.sizeX, self.sizeY)

class popUpInPracticeMenu:

    def __init__(self, screen, center_X, center_Y):

        self.screen = screen

        self.colors = {"darkBlue":(53, 63, 112), "screenGrey": (230,230,230)}

        self.center_X = center_X
        self.center_Y = center_Y

        self.Elements = []

        self.screenShader = Elements.screenShader(screen, center_X, center_Y)
        self.Elements.append(self.screenShader)

        self.popUpRect = popUpRect(screen, center_X, center_Y, self.colors, 400, 400)
        self.Elements.append(self.popUpRect)

        self.textDrawer = Elements.TextDrawer(screen, center_X, center_Y)
        self.Elements.append(self.popUpRect)
        
        self.textDrawer.add("Menu", "cX", "cy-155", 50, self.colors["darkBlue"],"ariel")
        self.Elements.append(self.textDrawer)

        buttonColor = (self.colors["darkBlue"], self.colors["screenGrey"], self.colors["darkBlue"])

        self.exitButton = Elements.Button(screen, 75, 150, 100, 50, buttonColor, 6, 10, "text", "Exit", 30, center_X, center_Y, 4201, True)
        self.returnButton = Elements.Button(screen, -75, 150, 100, 50, buttonColor, 6, 10, "text", "Done", 30, center_X, center_Y, 3799, True)

        self.Elements.append(self.exitButton)
        self.Elements.append(self.returnButton)

        self.Interactive = []

        self.Interactive.append(self.exitButton)
        self.Interactive.append(self.returnButton)

    def draw(self):
        for element in self.Elements:
            element.draw()

    def recenter(self, center_X, center_Y):
        self.center_X = center_X
        self.center_Y = center_Y
        for element in self.Elements:
            element.recenter(center_X,center_Y)