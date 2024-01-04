import pygame
import Elements

class homescreen:

    def __init__(self, screen, center_X, center_Y):

        self.Interactive = []

        self.colors = {"darkBlue":(53, 63, 112)}

        self.textDrawer = Elements.TextDrawer(screen)

        titleTextSize = 50
        self.textDrawer.add("2023-2024 BHSS Academic Super Bowl", center_X, center_Y-260, titleTextSize, self.colors["darkBlue"])
        self.textDrawer.add("Math Training Tool", center_X, center_Y-200, titleTextSize, self.colors["darkBlue"])

        buttonTextSize = 30
        
        StartButton = Elements.Button(screen, center_X, center_Y-10, 240, 100, self.colors["darkBlue"], 7, 10, "text", "Button 1", 30)
        OtherButton = Elements.Button(screen, center_X, center_Y+120, 240, 100, self.colors["darkBlue"], 7, 10, "text", "Button 2", 30)

        self.Interactive.append(StartButton)
        self.Interactive.append(OtherButton)

    def draw(self):
        self.textDrawer.drawAll()
        for Button in self.Interactive:
            Button.draw()

class resourcesScreen:

    def __init__(self):
        pass

    def draw():
        pass

class practiceScreen:

    def __init__(self):
        pass

    def draw():
        pass