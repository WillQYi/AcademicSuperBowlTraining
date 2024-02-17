import pygame
import Elements
import Screens
import PopUp

pygame.init()
screen = pygame.display.set_mode((1280,720),pygame.RESIZABLE)
clock = pygame.time.Clock()
running = True
Buttons = []

center_X = 640
center_Y = 360
currScreen = Screens.homescreen(screen, center_X, center_Y)
popUp = PopUp.popUpInPracticeMenu(screen, center_X, center_Y)

tabDown = False
popUpActive = False

while running:
    #Checks for user interactions
    for event in pygame.event.get():
        print(event)
        if event.type == pygame.QUIT:
            running = False

        #Window size is changed
        if event.type == 32778:
            if (pygame.display.get_window_size()[0] < 1280):
                center_X = 640
            else:
                center_X = pygame.display.get_window_size()[0]/2
            if (pygame.display.get_window_size()[1] < 720):
                center_Y = 360
            else:
                center_Y = pygame.display.get_window_size()[1]/2
            currScreen.recenter(center_X,center_Y)

        if event.type == pygame.MOUSEBUTTONUP:
            mousePos = pygame.mouse.get_pos()
            for Button in currScreen.Interactive:
                Button.clicked(mousePos)

        if event.type == pygame.KEYDOWN:
            for textbox in currScreen.InteractiveText:
                if (textbox.isActive):
                    textbox.inputText(event)

            if (event.key == pygame.K_LCTRL or event.key == pygame.K_LCTRL):
                tabDown = True
                homeScreenOperPart1 = True

            if (tabDown and event.key == pygame.K_t):
                currScreen = Screens.testScreen(screen, center_X, center_Y)
            elif (tabDown and event.key == pygame.K_h):
                currScreen = Screens.homescreen(screen, center_X, center_Y)
            elif (tabDown and event.key == pygame.K_p):
                currScreen = Screens.practiceSelectScreen(screen, center_X, center_Y)

        if event.type == pygame.KEYUP:
            if (event.key == pygame.K_LCTRL or event.key == pygame.K_LCTRL):
                tabDown = False

        #Custom events
                
        if event.type >= 3700 and event.type <= 3900:
            popUpActive = True
            if (Screens.eventDict[event.type] == "popUpExit"):
                popUpActive = False
            elif (Screens.eventDict[event.type] == "popUpInPractice"):
                popUp = PopUp.popUpInPracticeMenu(screen, center_X, center_Y)

        if event.type >= 4100 and event.type <= 4300:
            if Screens.eventDict[event.type] == "home":
                currScreen = Screens.homescreen(screen, center_X, center_Y)
                continue
            elif Screens.eventDict[event.type] == "credits":
                currScreen = Screens.creditsScreen(screen, center_X, center_Y)
                continue
            elif Screens.eventDict[event.type] == "pracSelect":
                currScreen = Screens.practiceSelectScreen(screen, center_X, center_Y)
                continue
            elif Screens.eventDict[event.type] == "algebra":
                currScreen = Screens.algebraScreen(screen, center_X, center_Y)
                continue
            elif Screens.eventDict[event.type] == "mod":
                currScreen = Screens.modScreen(screen, center_X, center_Y)
                continue
            elif Screens.eventDict[event.type] == "dooms":
                currScreen = Screens.doomScreen(screen, center_X, center_Y)
                continue

        if event.type >= 6900 and event.type <= 7000:
            if (Screens.eventDict[event.type] == "answerInputted"):
                currScreen.problemController.checkCorrect()
            elif (Screens.eventDict[event.type] == "newProblem"):
                currScreen.loadProblem()
            currScreen.swapButton()


    #print("-----------")   

    screen.fill((230,230,230))
    
    currScreen.run()
    if (popUpActive):
        popUp.draw()

    pygame.display.flip()

    clock.tick(60)

pygame.quit()