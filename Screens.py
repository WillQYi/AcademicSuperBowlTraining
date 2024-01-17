import pygame
import Elements

class homescreen:

    def __init__(self, screen, center_X, center_Y):

        self.Interactive = []

        self.colors = {"darkBlue":(53, 63, 112)}

        self.textDrawer = Elements.TextDrawer(screen, center_X, center_Y)

        titleTextSize = 50
        self.textDrawer.add("2023-2024 BHSS Academic Super Bowl", 0, -260, titleTextSize, self.colors["darkBlue"])
        self.textDrawer.add("Math Training Tool", 0, -200, titleTextSize, self.colors["darkBlue"])

        buttonTextSize = 40
        
        StartButton = Elements.Button(screen, 0, 50, 300, 150, self.colors["darkBlue"], 8, 10, "text", "Start", buttonTextSize, center_X, center_Y)
        
        self.Interactive.append(StartButton)

    def draw(self, center_X, center_Y):
        self.textDrawer.drawAll(center_X, center_Y)
        for Button in self.Interactive:
            Button.draw(center_X, center_Y)

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