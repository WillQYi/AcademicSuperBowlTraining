import pygame
import Elements

eventDict = {4199: "home", 4200: "pracScreen", 4201: "alegbra", 4202: "geometry", 4203: "statistics", 4204: "logarithms", 4205: "calculus", 4206: "mod", 4207: "dooms"}

class homescreen:

    def __init__(self, screen, center_X, center_Y):

        self.Interactive = []

        self.colors = {"darkBlue":(53, 63, 112)}

        self.textDrawer = Elements.TextDrawer(screen, center_X, center_Y)

        titleTextSize = 50
        self.textDrawer.add("2023-2024 BHSS Academic Super Bowl", 0, -260, titleTextSize, self.colors["darkBlue"])
        self.textDrawer.add("Math Training Tool", 0, -200, titleTextSize, self.colors["darkBlue"])

        buttonTextSize = 40
        
        StartButton = Elements.Button(screen, 0, 50, 300, 150, self.colors["darkBlue"], 8, 10, "text", "Start", buttonTextSize, center_X, center_Y, "PRACTICESELECT")
        
        self.Interactive.append(StartButton)

        self.draw(center_X, center_Y)

    def draw(self, center_X, center_Y):
        self.textDrawer.drawAll(center_X, center_Y)
        for Button in self.Interactive:
            Button.draw(center_X, center_Y)

class resourcesScreen:

    def __init__(self):
        pass

    def draw():
        pass

class practiceSelectScreen:

    def __init__(self, screen, center_X, center_Y):

        self.Interactive = []

        self.colors = {"darkBlue":(53, 63, 112)}

        self.textDrawer = Elements.TextDrawer(screen, center_X, center_Y)

        titleTextSize = 50
        self.textDrawer.add("Select Practice", 0, -260, titleTextSize, self.colors["darkBlue"])

        buttonTextSize = 30
        buttonX = 350
        buttonY = 100
        spreadY = 150
        spreadX = 400
        
        AlegbraButton = Elements.Button(screen, 0-spreadX, 50-spreadY, buttonX, buttonY, self.colors["darkBlue"], 8, 10, "text", "Algebra", buttonTextSize, center_X, center_Y, 4201)
        GeometryButton = Elements.Button(screen, 0, 50-spreadY, buttonX, buttonY, self.colors["darkBlue"], 8, 10, "text", "Geometry", buttonTextSize, center_X, center_Y, 4202)
        StatisticsButton = Elements.Button(screen, 0+spreadX, 50-spreadY, buttonX, buttonY, self.colors["darkBlue"], 8, 10, "text", "Statistics", buttonTextSize, center_X, center_Y, 4203)
        LogarithmButton = Elements.Button(screen, 0-spreadX, 50, buttonX, buttonY, self.colors["darkBlue"], 8, 10, "text", "Logarithms", buttonTextSize, center_X, center_Y, 4204)
        CalculusButton = Elements.Button(screen, 0, 50, buttonX, buttonY, self.colors["darkBlue"], 8, 10, "text", "Calculus", buttonTextSize, center_X, center_Y, 4205)
        ModButton = Elements.Button(screen, 0+spreadX, 50, buttonX, buttonY, self.colors["darkBlue"], 8, 10, "text", "Modulo Arithemtic", buttonTextSize, center_X, center_Y, 4206)
        DoomsButton = Elements.Button(screen, 0, 50+spreadY, buttonX, buttonY, self.colors["darkBlue"], 8, 10, "text", "Doomsday Rule", buttonTextSize, center_X, center_Y, 4207)

        self.Interactive.append(AlegbraButton)
        self.Interactive.append(GeometryButton)
        self.Interactive.append(StatisticsButton)
        self.Interactive.append(LogarithmButton)
        self.Interactive.append(CalculusButton)
        self.Interactive.append(ModButton)
        self.Interactive.append(DoomsButton)

        self.draw(center_X, center_Y)


    def draw(self, center_X, center_Y):
        self.textDrawer.drawAll(center_X, center_Y)
        for Button in self.Interactive:
            Button.draw(center_X, center_Y)