import pygame
import Elements

eventDict = {4200: "home", 4201: "pracSelect", 4202: "alegbra", 4203: "geometry", 4204: "statistics", 4205: "logarithms", 4206: "calculus", 4207: "mod", 4208: "dooms"}

class homescreen:

    def __init__(self, screen, center_X, center_Y):

        self.Interactive = []

        self.center_X = center_X
        self.center_Y = center_Y

        self.colors = {"darkBlue":(53, 63, 112)}

        self.textDrawer = Elements.TextDrawer(screen, center_X, center_Y)

        titleTextSize = 50
        self.textDrawer.add("2023-2024 BHSS Academic Super Bowl", 0, -260, titleTextSize, self.colors["darkBlue"])
        self.textDrawer.add("Math Training Tool", 0, -200, titleTextSize, self.colors["darkBlue"])

        ButtonTextSize = 40
        
        StartButton = Elements.Button(screen, 0, 50, 300, 150, self.colors["darkBlue"], 8, 10, "text", "Start", ButtonTextSize, center_X, center_Y, 4201)
        
        self.Interactive.append(StartButton)

        self.draw()

    def draw(self):
        self.textDrawer.drawAll()
        for Button in self.Interactive:
            Button.draw()

    def recenter(self, center_X, center_Y):
        self.textDrawer.recenter(center_X, center_Y)
        for Interactive in self.Interactive:
            Interactive.recenter(center_X, center_Y)

class practiceSelectScreen:

    def __init__(self, screen, center_X, center_Y):

        self.Interactive = []

        self.center_X = center_X
        self.center_Y = center_Y

        self.colors = {"darkBlue":(53, 63, 112)}

        self.textDrawer = Elements.TextDrawer(screen, center_X, center_Y)

        titleTextSize = 50
        self.textDrawer.add("Select Practice", 0, -260, titleTextSize, self.colors["darkBlue"])

        
        #Utility Button Sizes
        settingsButton = Elements.Button(screen, 500, -260, 100, 100, self.colors["darkBlue"], 8, 10, "image", "homeButton.png", 0.2, center_X, center_Y, 4200)

        #Practice Button Sizes
        practiceButtonTextSize = 30
        practiceButtonX = 350
        practiceButtonY = 100
        practiceSpreadY = 150
        practiceSpreadX = 400
        
        #Creating Practice Buttons
        AlegbraButton = Elements.Button(screen, 0-practiceSpreadX, 50-practiceSpreadY, practiceButtonX, practiceButtonY, self.colors["darkBlue"], 8, 10, "text", "Algebra", practiceButtonTextSize, center_X, center_Y, 4202)
        GeometryButton = Elements.Button(screen, 0, 50-practiceSpreadY, practiceButtonX, practiceButtonY, self.colors["darkBlue"], 8, 10, "text", "Geometry", practiceButtonTextSize, center_X, center_Y, 4203)
        StatisticsButton = Elements.Button(screen, 0+practiceSpreadX, 50-practiceSpreadY, practiceButtonX, practiceButtonY, self.colors["darkBlue"], 8, 10, "text", "Statistics", practiceButtonTextSize, center_X, center_Y, 4204)
        LogarithmButton = Elements.Button(screen, 0-practiceSpreadX, 50, practiceButtonX, practiceButtonY, self.colors["darkBlue"], 8, 10, "text", "Logarithms", practiceButtonTextSize, center_X, center_Y, 4205)
        CalculusButton = Elements.Button(screen, 0, 50, practiceButtonX, practiceButtonY, self.colors["darkBlue"], 8, 10, "text", "Calculus", practiceButtonTextSize, center_X, center_Y, 4206)
        ModButton = Elements.Button(screen, 0+practiceSpreadX, 50, practiceButtonX, practiceButtonY, self.colors["darkBlue"], 8, 10, "text", "Modulo Arithemtic", practiceButtonTextSize, center_X, center_Y, 4207)
        DoomsButton = Elements.Button(screen, 0, 50+practiceSpreadY, practiceButtonX, practiceButtonY, self.colors["darkBlue"], 8, 10, "text", "Doomsday Rule", practiceButtonTextSize, center_X, center_Y, 4208)
        
        #Creating Utility Buttons

        #Adding to interactive
        self.Interactive.append(AlegbraButton)
        self.Interactive.append(GeometryButton)
        self.Interactive.append(StatisticsButton)
        self.Interactive.append(LogarithmButton)
        self.Interactive.append(CalculusButton)
        self.Interactive.append(ModButton)
        self.Interactive.append(DoomsButton)

        self.Interactive.append(settingsButton)

        self.draw()


    def draw(self):
        self.textDrawer.drawAll()
        for Button in self.Interactive:
            Button.draw()

    def recenter(self, center_X, center_Y):
        self.textDrawer.recenter(center_X, center_Y)
        for Interactive in self.Interactive:
            Interactive.recenter(center_X, center_Y)