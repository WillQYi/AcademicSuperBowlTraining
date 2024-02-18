import pygame
import Elements
import random
import AlgebraProblems
import ModProblems
import DoomProblems
import Expressions

eventDict = {3799: "popUpExit", 3800: "popUpInPractice", 3801: "checkExit", 3802: "popUpSettings", 4199: "credits", 4200: "home", 4201: "pracSelect", 4202: "algebra", 4203: "geometry", 4204: "statistics", 4205: "logarithms", 4206: "calculus", 4207: "mod", 4208: "dooms", 6900: "answerInputted", 6901: "newProblem"}

class testScreen:

    def __init__(self, screen, center_X, center_Y):

        self.screen = screen

        self.Elements = []
        self.Interactive = []
        self.InteractiveText = []

        self.center_X = center_X
        self.center_Y = center_Y

        self.rect = pygame.Rect(0,0,2*center_X,2*center_Y)

        self.surface = pygame.Surface((2*center_X,2*center_Y), pygame.SRCALPHA)

    def run(self):
        self.draw()

    def draw(self):
        self.screen.blit(self.surface, (0,0))
        pygame.draw.rect(self.surface, (0,0,0,50), self.rect, 0, 0)
        '''
        for element in self.Elements:
            element.draw()
        '''

    def recenter(self, center_X, center_Y):
        self.center_X = center_X
        self.center_Y = center_Y
        '''
        self.textDrawer.recenter(center_X, center_Y)
        for Elements in self.Elements:
            Elements.recenter(center_X, center_Y)
        '''

class homescreen:

    def __init__(self, screen, center_X, center_Y):

        self.Elements = []
        self.Interactive = []
        self.InteractiveText = []

        self.center_X = center_X
        self.center_Y = center_Y

        self.colors = {"darkBlue":(53, 63, 112), "screenGrey": (230,230,230)}

        self.textDrawer = Elements.TextDrawer(screen, center_X, center_Y)

        titleTextSize = 70
        self.textDrawer.add("2023-2024 BHSS Academic Super Bowl", "cX", "cY-260", titleTextSize, self.colors["darkBlue"],"ariel")
        self.textDrawer.add("Math Training Tool", "cX", "cY-200", titleTextSize, self.colors["darkBlue"],"ariel")

        ButtonTextSize = 50
        buttonColor = (self.colors["darkBlue"], self.colors["screenGrey"], self.colors["darkBlue"])

        StartButton = Elements.Button(screen, 0, 0, 300, 150, buttonColor, 8, 10, "text", "Start", ButtonTextSize, center_X, center_Y, 4201, True)
        creditsHelpButton = Elements.Button(screen, 0, 185, 300, 150, buttonColor, 8, 10, "text", "Credits/Help", ButtonTextSize, center_X, center_Y, 4199, True)

        self.Elements.append(self.textDrawer)
        self.Elements.append(StartButton)
        self.Elements.append(creditsHelpButton)

        self.Interactive.append(StartButton)
        self.Interactive.append(creditsHelpButton)

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

class creditsScreen:

    def __init__(self, screen, center_X, center_Y):

        self.Elements = []
        self.Interactive = []
        self.InteractiveText = []

        self.center_X = center_X
        self.center_Y = center_Y

        self.colors = {"darkBlue":(53, 63, 112), "screenGrey": (230,230,230)}

        self.textDrawer = Elements.TextDrawer(screen, center_X, center_Y)
        self.Elements.append(self.textDrawer)

        buttonColor = (self.colors["darkBlue"], self.colors["screenGrey"], self.colors["darkBlue"])

        homeButton = Elements.Button(screen, "cX-100", "100-cY", 100, 100, buttonColor, 8, 10, "image", "homeButton.png", 0.23, center_X, center_Y, 4200, True)

        self.Elements.append(homeButton)
        self.Interactive.append(homeButton)

        titleTextSize = 70
        self.textDrawer.add("Created by:", 175, 50, titleTextSize, self.colors["darkBlue"],"ariel")

        normalTextSize = 30
        self.textDrawer.add("- An Kieu", 95, 100, normalTextSize, self.colors["darkBlue"],"ariel")

        self.textDrawer.add("BHSS 2023-2024 Math Team: ", 390, 200, titleTextSize, self.colors["darkBlue"],"ariel")
        self.textDrawer.add("- An Kieu (Captian), Minh Huynh, Edward Choi, Jackson Fries, Jacob Hammond,", 440, 270, normalTextSize, self.colors["darkBlue"],"ariel")
        self.textDrawer.add("Will Yi, Dylan Stringer, Shayan Shamsipour, Yelena Zhou, Yucelin Zhou", 410, 320, normalTextSize, self.colors["darkBlue"],"ariel")

        self.textDrawer.add("Notes Link:", 165, 430, titleTextSize, self.colors["darkBlue"],"ariel")
        self.textDrawer.add("- https://docs.google.com/document/d/1ockbV0BvivHAAlEOwTlSEGRIsPMJ869TA_Aa0GmViF4/edit?usp=sharing", 590, 490, normalTextSize, self.colors["darkBlue"],"ariel")

        self.textDrawer.add("Assigned Subjects:", 260, 590, titleTextSize, self.colors["darkBlue"],"ariel")
        self.textDrawer.add("- https://docs.google.com/spreadsheets/d/18DLC50YC8_uU0_lGhbcC9ZMmexmqa_q2V47GzfwVNSE/edit#gid=0", 575, 650, normalTextSize, self.colors["darkBlue"],"ariel")


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

        self.InteractiveText = []

        self.center_X = center_X
        self.center_Y = center_Y

        self.colors = {"darkBlue":(53, 63, 112), "screenGrey": (230,230,230)}

        self.textDrawer = Elements.TextDrawer(screen, center_X, center_Y)

        titleTextSize = 70
        self.textDrawer.add("Select Practice", "cX", "cY-260", titleTextSize, self.colors["darkBlue"], "ariel")

        buttonColor = (self.colors["darkBlue"], self.colors["screenGrey"], self.colors["darkBlue"])
        
        #Utility Button Sizes
        homeButton = Elements.Button(screen, "cX-100", "100-cY", 100, 100, buttonColor, 8, 10, "image", "homeButton.png", 0.23, center_X, center_Y, 4200, True)
        settingsButton = Elements.Button(screen, "cX-100", "cY-100", 100, 100, buttonColor, 8, 10, "image", "settingsButton.png", 0.9, center_X, center_Y, 4200, False)
        statsButton = Elements.Button(screen, "100-cX", "cY-100", 100, 100, buttonColor, 8, 10, "image", "statsButton.png", 0.9, center_X, center_Y, 4200, False)

        #Practice Button Sizes
        practiceButtonTextSize = 40
        practiceButtonX = 350
        practiceButtonY = 100
        practiceSpreadY = 150
        practiceSpreadX = 400
        
        #Creating Practice Buttons
        AlegbraButton = Elements.Button(screen, 0-practiceSpreadX, 50-practiceSpreadY, practiceButtonX, practiceButtonY, buttonColor, 8, 10, "text", "Algebra", practiceButtonTextSize, center_X, center_Y, 4202, True)
        GeometryButton = Elements.Button(screen, 0, 50-practiceSpreadY, practiceButtonX, practiceButtonY, buttonColor, 8, 10, "text", "Geometry", practiceButtonTextSize, center_X, center_Y, 4203, False)
        StatisticsButton = Elements.Button(screen, 0+practiceSpreadX, 50-practiceSpreadY, practiceButtonX, practiceButtonY, buttonColor, 8, 10, "text", "Statistics", practiceButtonTextSize, center_X, center_Y, 4204, False)
        LogarithmButton = Elements.Button(screen, 0-practiceSpreadX, 50, practiceButtonX, practiceButtonY, buttonColor, 8, 10, "text", "Logarithms", practiceButtonTextSize, center_X, center_Y, 4205, False)
        CalculusButton = Elements.Button(screen, 0, 50, practiceButtonX, practiceButtonY, buttonColor, 8, 10, "text", "Calculus", practiceButtonTextSize, center_X, center_Y, 4206, False)
        ModButton = Elements.Button(screen, 0+practiceSpreadX, 50, practiceButtonX, practiceButtonY, buttonColor, 8, 10, "text", "Modulo Arithemtic", practiceButtonTextSize, center_X, center_Y, 4207, True)
        DoomsButton = Elements.Button(screen, 0, 50+practiceSpreadY, practiceButtonX, practiceButtonY, buttonColor, 8, 10, "text", "Doomsday Rule", practiceButtonTextSize, center_X, center_Y, 4208, True)
        
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

        self.InteractiveText = []

        self.center_X = center_X
        self.center_Y = center_Y

        self.problemsDone = 0

        self.colors = {"darkBlue": (53, 63, 112), "screenGrey": (230,230,230), "lightBlue":(38, 176, 237)}

        self.titleTextSize = 50

        self.textDrawer = Elements.TextDrawer(screen, center_X, center_Y)
        self.textDrawer.add("Algebra Practice", "cX", 95/2, self.titleTextSize, self.colors["darkBlue"], "ariel")

        self.topDivider = Elements.divider(screen, "horizontal", center_X, center_Y, 95, 7, self.colors["darkBlue"])
        self.bottomDivider = Elements.divider(screen, "horizontal", center_X, center_Y, "2*cY-175", 7, self.colors["darkBlue"])
        self.problemNumberBox = Elements.problemNumberBox(screen, 25, 140, 60, 60, str(self.problemsDone), self.colors["darkBlue"])

        self.problemController = Elements.problemController(screen, self.center_X, self.center_Y, self.colors["darkBlue"])
        self.loadProblem()
        self.Elements.append(self.problemController)

        buttonColor = (self.colors["darkBlue"], self.colors["screenGrey"], self.colors["darkBlue"])

        menuButton = Elements.Button(screen, "cX-50", "50-cY", 68, 68, buttonColor, 6, 10, "image", "menuButton.png", 0.6, center_X, center_Y, 3800, True)

        self.Elements.append(menuButton)
        self.Interactive.append(menuButton)

        self.checkButton = Elements.Button(screen, "cX-100", "cY-88", 100, 68, buttonColor, 6, 10, "text", "Submit", 30, center_X, center_Y, 6900, True)
        self.nextButton = Elements.Button(screen, "cX-100", "cY-88", 100, 68, buttonColor, 6, 10, "image", "arrowButton.png", 0.3, center_X, center_Y, 6901, True)

        self.Elements.append(self.checkButton)
        self.Interactive.append(self.checkButton)

        self.Elements.append(self.textDrawer)
        self.Elements.append(self.topDivider)
        self.Elements.append(self.bottomDivider)
        self.Elements.append(self.problemNumberBox)

        self.draw()

    def run(self):
        self.draw()

    def draw(self):
        for element in self.Elements:
            element.draw()

    def loadProblem(self):

        self.problemsDone += 1
        self.problemNumberBox.changeNumber(self.problemsDone)
        
        try:
            for textbox in self.problemController.inputElements:
                self.Interactive.append(textbox)
                self.InteractiveText.append(textbox)
        except:
            pass

        self.problemController.reset()

        self.problem = AlgebraProblems.problemList[random.randint(0,1)]
        self.problem.create()
        self.problemController.loadProblemDisplay(self.problem)
        self.problemController.loadProblemInput(self.problem.answerReceiver)

        for textbox in self.problemController.inputElements:
            self.Interactive.append(textbox)
            self.InteractiveText.append(textbox)

    def swapButton(self):
        if (self.checkButton in self.Elements):
            self.Elements.remove(self.checkButton)
            self.Interactive.remove(self.checkButton)
            self.Elements.append(self.nextButton)
            self.Interactive.append(self.nextButton)
        else:
            self.Elements.remove(self.nextButton)
            self.Interactive.remove(self.nextButton)
            self.Elements.append(self.checkButton)
            self.Interactive.append(self.checkButton)

    def recenter(self, center_X, center_Y):
        self.center_X = center_X
        self.center_Y = center_Y
        for element in self.Elements:
            element.recenter(center_X, center_Y)

class modScreen:

    def __init__(self, screen, center_X, center_Y):

        self.screen = screen

        self.Elements = []
        self.Interactive = []

        self.InteractiveText = []

        self.center_X = center_X
        self.center_Y = center_Y

        self.problemsDone = 0

        self.colors = {"darkBlue": (53, 63, 112), "screenGrey": (230,230,230), "lightBlue":(38, 176, 237)}

        self.titleTextSize = 50

        self.textDrawer = Elements.TextDrawer(screen, center_X, center_Y)
        self.textDrawer.add("Modular Arithmetic Practice", "cX", 95/2, self.titleTextSize, self.colors["darkBlue"], "ariel")

        self.topDivider = Elements.divider(screen, "horizontal", center_X, center_Y, 95, 7, self.colors["darkBlue"])
        self.bottomDivider = Elements.divider(screen, "horizontal", center_X, center_Y, "2*cY-175", 7, self.colors["darkBlue"])
        self.problemNumberBox = Elements.problemNumberBox(screen, 25, 140, 60, 60, str(self.problemsDone+1), self.colors["darkBlue"])

        self.problemController = Elements.problemController(screen, self.center_X, self.center_Y, self.colors["darkBlue"])
        self.loadProblem()
        self.Elements.append(self.problemController)

        buttonColor = (self.colors["darkBlue"], self.colors["screenGrey"], self.colors["darkBlue"])

        menuButton = Elements.Button(screen, "cX-50", "50-cY", 68, 68, buttonColor, 6, 10, "image", "menuButton.png", 0.6, center_X, center_Y, 3800, True)

        self.Elements.append(menuButton)
        self.Interactive.append(menuButton)

        self.checkButton = Elements.Button(screen, "cX-100", "cY-88", 100, 68, buttonColor, 6, 10, "text", "Submit", 30, center_X, center_Y, 6900, True)
        self.nextButton = Elements.Button(screen, "cX-100", "cY-88", 100, 68, buttonColor, 6, 10, "image", "arrowButton.png", 0.3, center_X, center_Y, 6901, True)

        self.Elements.append(self.checkButton)
        self.Interactive.append(self.checkButton)

        self.Elements.append(self.textDrawer)
        self.Elements.append(self.topDivider)
        self.Elements.append(self.bottomDivider)
        self.Elements.append(self.problemNumberBox)

        self.draw()

    def run(self):
        self.draw()

    def draw(self):
        for element in self.Elements:
            element.draw()

    def loadProblem(self):

        self.problemsDone += 1
        self.problemNumberBox.changeNumber(self.problemsDone)
        
        try:
            for textbox in self.problemController.inputElements:
                self.Interactive.append(textbox)
                self.InteractiveText.append(textbox)
        except:
            pass

        self.problemController.reset()

        self.problem = ModProblems.problemList[random.randint(0,4)]
        self.problem.create()
        self.problemController.loadProblemDisplay(self.problem)
        self.problemController.loadProblemInput(self.problem.answerReceiver)

        for textbox in self.problemController.inputElements:
            self.Interactive.append(textbox)
            self.InteractiveText.append(textbox)

    def swapButton(self):
        if (self.checkButton in self.Elements):
            self.Elements.remove(self.checkButton)
            self.Interactive.remove(self.checkButton)
            self.Elements.append(self.nextButton)
            self.Interactive.append(self.nextButton)
        else:
            self.Elements.remove(self.nextButton)
            self.Interactive.remove(self.nextButton)
            self.Elements.append(self.checkButton)
            self.Interactive.append(self.checkButton)

    def recenter(self, center_X, center_Y):
        self.center_X = center_X
        self.center_Y = center_Y
        for element in self.Elements:
            element.recenter(center_X, center_Y)

class doomScreen:

    def __init__(self, screen, center_X, center_Y):

        self.screen = screen

        self.Elements = []
        self.Interactive = []

        self.InteractiveText = []

        self.center_X = center_X
        self.center_Y = center_Y

        self.problemsDone = 0

        self.colors = {"darkBlue": (53, 63, 112), "screenGrey": (230,230,230), "lightBlue":(38, 176, 237)}

        self.titleTextSize = 50

        self.textDrawer = Elements.TextDrawer(screen, center_X, center_Y)
        self.textDrawer.add("Doomsday Algorithm Practice", "cX", 95/2, self.titleTextSize, self.colors["darkBlue"], "ariel")

        self.topDivider = Elements.divider(screen, "horizontal", center_X, center_Y, 95, 7, self.colors["darkBlue"])
        self.bottomDivider = Elements.divider(screen, "horizontal", center_X, center_Y, "2*cY-175", 7, self.colors["darkBlue"])
        self.problemNumberBox = Elements.problemNumberBox(screen, 25, 140, 60, 60, str(self.problemsDone+1), self.colors["darkBlue"])

        self.problemController = Elements.problemController(screen, self.center_X, self.center_Y, self.colors["darkBlue"])
        self.loadProblem()
        self.Elements.append(self.problemController)

        buttonColor = (self.colors["darkBlue"], self.colors["screenGrey"], self.colors["darkBlue"])

        menuButton = Elements.Button(screen, "cX-50", "50-cY", 68, 68, buttonColor, 6, 10, "image", "menuButton.png", 0.6, center_X, center_Y, 3800, True)

        self.Elements.append(menuButton)
        self.Interactive.append(menuButton)

        self.checkButton = Elements.Button(screen, "cX-100", "cY-88", 100, 68, buttonColor, 6, 10, "text", "Submit", 30, center_X, center_Y, 6900, True)
        self.nextButton = Elements.Button(screen, "cX-100", "cY-88", 100, 68, buttonColor, 6, 10, "image", "arrowButton.png", 0.3, center_X, center_Y, 6901, True)

        self.Elements.append(self.checkButton)
        self.Interactive.append(self.checkButton)

        self.Elements.append(self.textDrawer)
        self.Elements.append(self.topDivider)
        self.Elements.append(self.bottomDivider)
        self.Elements.append(self.problemNumberBox)

        self.draw()

    def run(self):
        self.draw()

    def draw(self):
        for element in self.Elements:
            element.draw()

    def loadProblem(self):

        self.problemsDone += 1
        self.problemNumberBox.changeNumber(self.problemsDone)
        
        try:
            for textbox in self.problemController.inputElements:
                self.Interactive.append(textbox)
                self.InteractiveText.append(textbox)
        except:
            pass

        self.problemController.reset()

        self.problem = DoomProblems.problemList[random.randint(0,3)]
        self.problem.create()
        self.problemController.loadProblemDisplay(self.problem)
        self.problemController.loadProblemInput(self.problem.answerReceiver)

        for textbox in self.problemController.inputElements:
            self.Interactive.append(textbox)
            self.InteractiveText.append(textbox)

    def swapButton(self):
        if (self.checkButton in self.Elements):
            self.Elements.remove(self.checkButton)
            self.Interactive.remove(self.checkButton)
            self.Elements.append(self.nextButton)
            self.Interactive.append(self.nextButton)
        else:
            self.Elements.remove(self.nextButton)
            self.Interactive.remove(self.nextButton)
            self.Elements.append(self.checkButton)
            self.Interactive.append(self.checkButton)

    def recenter(self, center_X, center_Y):
        self.center_X = center_X
        self.center_Y = center_Y
        for element in self.Elements:
            element.recenter(center_X, center_Y)