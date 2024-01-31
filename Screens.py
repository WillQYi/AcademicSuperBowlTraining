import pygame
import Elements

eventDict = {4200: "home", 4201: "pracSelect", 4202: "algebra", 4203: "geometry", 4204: "statistics", 4205: "logarithms", 4206: "calculus", 4207: "mod", 4208: "dooms"}

class homescreen:

    def __init__(self, screen, center_X, center_Y):

        self.Elements = []
        self.Interactive = []

        self.center_X = center_X
        self.center_Y = center_Y

        self.colors = {"darkBlue":(53, 63, 112)}

        self.textDrawer = Elements.TextDrawer(screen, center_X, center_Y)

        titleTextSize = 50
        self.textDrawer.add("2023-2024 BHSS Academic Super Bowl", 0, -260, titleTextSize, self.colors["darkBlue"], "center","calibri")
        self.textDrawer.add("Math Training Tool", 0, -200, titleTextSize, self.colors["darkBlue"], "center","calibri")

        ButtonTextSize = 40
        
        StartButton = Elements.Button(screen, 0, 50, 300, 150, self.colors["darkBlue"], 8, 10, "text", "Start", ButtonTextSize, center_X, center_Y, 4201, True)
        
        self.Elements.append(self.textDrawer)
        self.Elements.append(StartButton)

        self.Interactive.append(StartButton)

        self.draw()

    def run(self):
        self.draw()

    def draw(self):
        for element in self.Elements:
            element.draw()

    def recenter(self, center_X, center_Y):
        self.center_X = center_X
        self.center_Y = center_Y
        self.textDrawer.recenter(center_X, center_Y)
        for Elements in self.Elements:
            Elements.recenter(center_X, center_Y)

class practiceSelectScreen:

    def __init__(self, screen, center_X, center_Y):

        self.Elements = []
        self.Interactive = []

        self.center_X = center_X
        self.center_Y = center_Y

        self.colors = {"darkBlue":(53, 63, 112)}

        self.textDrawer = Elements.TextDrawer(screen, center_X, center_Y)

        titleTextSize = 50
        self.textDrawer.add("Select Practice", 0, -260, titleTextSize, self.colors["darkBlue"], "center","calibri")
        
        #Utility Button Sizes
        homeButton = Elements.Button(screen, 500, -260, 100, 100, self.colors["darkBlue"], 8, 10, "image", "homeButton.png", 0.23, center_X, center_Y, 4200, True)
        settingsButton = Elements.Button(screen, 500, 260, 100, 100, self.colors["darkBlue"], 8, 10, "image", "settingsButton.png", 0.9, center_X, center_Y, 4200, False)
        statsButton = Elements.Button(screen, -500, 260, 100, 100, self.colors["darkBlue"], 8, 10, "image", "statsButton.png", 0.9, center_X, center_Y, 4200, False)

        #Practice Button Sizes
        practiceButtonTextSize = 30
        practiceButtonX = 350
        practiceButtonY = 100
        practiceSpreadY = 150
        practiceSpreadX = 400
        
        #Creating Practice Buttons
        AlegbraButton = Elements.Button(screen, 0-practiceSpreadX, 50-practiceSpreadY, practiceButtonX, practiceButtonY, self.colors["darkBlue"], 8, 10, "text", "Algebra", practiceButtonTextSize, center_X, center_Y, 4202, True)
        GeometryButton = Elements.Button(screen, 0, 50-practiceSpreadY, practiceButtonX, practiceButtonY, self.colors["darkBlue"], 8, 10, "text", "Geometry", practiceButtonTextSize, center_X, center_Y, 4203, False)
        StatisticsButton = Elements.Button(screen, 0+practiceSpreadX, 50-practiceSpreadY, practiceButtonX, practiceButtonY, self.colors["darkBlue"], 8, 10, "text", "Statistics", practiceButtonTextSize, center_X, center_Y, 4204, False)
        LogarithmButton = Elements.Button(screen, 0-practiceSpreadX, 50, practiceButtonX, practiceButtonY, self.colors["darkBlue"], 8, 10, "text", "Logarithms", practiceButtonTextSize, center_X, center_Y, 4205, False)
        CalculusButton = Elements.Button(screen, 0, 50, practiceButtonX, practiceButtonY, self.colors["darkBlue"], 8, 10, "text", "Calculus", practiceButtonTextSize, center_X, center_Y, 4206, False)
        ModButton = Elements.Button(screen, 0+practiceSpreadX, 50, practiceButtonX, practiceButtonY, self.colors["darkBlue"], 8, 10, "text", "Modulo Arithemtic", practiceButtonTextSize, center_X, center_Y, 4207, False)
        DoomsButton = Elements.Button(screen, 0, 50+practiceSpreadY, practiceButtonX, practiceButtonY, self.colors["darkBlue"], 8, 10, "text", "Doomsday Rule", practiceButtonTextSize, center_X, center_Y, 4208, False)
        
        #Creating Utility Buttons

        #Adding to Elements
        self.Elements.append(AlegbraButton)
        self.Elements.append(GeometryButton)
        self.Elements.append(StatisticsButton)
        self.Elements.append(LogarithmButton)
        self.Elements.append(CalculusButton)
        self.Elements.append(ModButton)
        self.Elements.append(DoomsButton)

        self.Elements.append(homeButton)
        self.Elements.append(settingsButton)
        self.Elements.append(statsButton)

        self.Elements.append(self.textDrawer)

        #Adding to interactive
        self.Interactive.append(AlegbraButton)
        self.Interactive.append(GeometryButton)
        self.Interactive.append(StatisticsButton)
        self.Interactive.append(LogarithmButton)
        self.Interactive.append(CalculusButton)
        self.Interactive.append(ModButton)
        self.Interactive.append(DoomsButton)

        self.Interactive.append(homeButton)
        self.Interactive.append(settingsButton)
        self.Interactive.append(statsButton)

        self.draw()

    def run(self):
        self.draw()

    def draw(self):
        for element in self.Elements:
            element.draw()

    def recenter(self, center_X, center_Y):
        self.center_X = center_X
        self.center_Y = center_Y
        for Elements in self.Elements:
            Elements.recenter(center_X, center_Y)

class algebraScreen:

    def __init__(self, screen, center_X, center_Y):

        self.screen = screen

        self.Elements = []
        self.Interactive = []

        self.center_X = center_X
        self.center_Y = center_Y

        self.problemsDone = 0

        self.colors = {"darkBlue":(53, 63, 112)}

        self.titleTextSize = 40

        self.textDrawer = Elements.TextDrawer(screen, center_X, center_Y)
        self.textDrawer.add("Algebra Practice", 0, -1*(self.center_Y-40), self.titleTextSize, self.colors["darkBlue"], "center","calibri")

        self.topDivider = Elements.divider(screen, "horizontal", center_X, center_Y, 80, 7, self.colors["darkBlue"])
        self.bottomDivider = Elements.divider(screen, "horizontal", center_X, center_Y, 550, 7, self.colors["darkBlue"])
        self.problemNumberBox = Elements.problemNumberBox(screen, 25, 115, 60, 60, str(self.problemsDone+1), self.colors["darkBlue"])

        #Testing
        self.textBox = Elements.inputTextBox(screen, center_X, center_Y, 0, 275, 300, 50, "x", "Type Answer")

        self.Elements.append(self.textDrawer)
        self.Elements.append(self.topDivider)
        self.Elements.append(self.bottomDivider)
        self.Elements.append(self.textBox)
        self.Elements.append(self.problemNumberBox)

        self.Interactive.append(self.textBox)

        self.draw()

    def run(self):
        self.draw()

    def draw(self):
        for element in self.Elements:
            element.draw()

    def recenter(self, center_X, center_Y):
        self.center_X = center_X
        self.center_Y = center_Y
        for element in self.Elements:
            element.recenter(center_X, center_Y)
