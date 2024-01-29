import pygame
import Elements
import random
import math

#Problem template
'''
class AlgebraProblem1: 

    def __init__(self):

        self.answerReceiver = "textBox"
        self.answer = 0

        pass
    
    def generateProblem(self):
        pass

    def checkCorrect(self):
        pass
'''

#Two linear equations with Integer Solutions
class AlgebraProblem1: 

    def __init__(self):

        self.answerReceiver = "textBox2"
        self.answer = 0

        pass

    def equationBuilder(self, coefficient1, coefficient2, LHS):
        equationString = ""
        if (coefficient1 == 1):
            pass
        elif (coefficient1 == -1):
            equationString += "-"
        else:
            equationString += str(coefficient1)

        if (abs(coefficient2) == 1):
            equationString += "x + "
        elif (coefficient2 == -1):
            equationString += "x - "
        elif(coefficient2 < 0):
            equationString += "x - " + str(abs(coefficient2))
        else:
            equationString += "x + " + str(coefficient2)
        equationString += "y = " + str(LHS)
        return equationString
    
    def generateProblem(self):
        
        multiplier = False

        choice = random.randint(1,100)
        if (choice <= 50):
            rangeAnswer = 10
            rangeCoefficient = 20
        elif (choice <= 90):
            rangeAnswer = 20
            rangeCoefficient = 50
        else:
            rangeAnswer = 50
            rangeCoefficient = 100

        answerX = random.randint(-1 * rangeAnswer , rangeAnswer)
        while (answerX == 0):
            answerX = random.randint(-1 * rangeAnswer , rangeAnswer)
        answerY = random.randint(-1 * rangeAnswer , rangeAnswer)
        while (answerY == 0):
            answerY = random.randint(-1 * rangeAnswer , rangeAnswer)

        #First equation coefficients
        coefficient1x = random.randint(-1*rangeCoefficient, rangeCoefficient)
        while (coefficient1x == 0):
            coefficient1x = random.randint(-1 * rangeAnswer , rangeAnswer)
        coefficient1y = random.randint(-1*rangeCoefficient, rangeCoefficient)
        while (coefficient1y == 0):
            coefficient1x = random.randint(-1 * rangeAnswer , rangeAnswer)        
        coefficient2x = random.randint(-1*rangeCoefficient, rangeCoefficient)

        #Second equation coefficients
        while (coefficient2x == 0):
            coefficient2x = random.randint(-1 * rangeAnswer , rangeAnswer)
        coefficient2y = random.randint(-1*rangeCoefficient, rangeCoefficient)
        while (coefficient2y == 0):
            coefficient2y = random.randint(-1 * rangeAnswer , rangeAnswer)
        
        LHS1 = answerX * coefficient1x + answerY * coefficient1y
        LHS2 = answerX * coefficient2x + answerY * coefficient2y

        print(self.equationBuilder(coefficient1x, coefficient1y, LHS1))
        print(self.equationBuilder(coefficient2x, coefficient2y, LHS2))
    

    def checkCorrect(self):
        pass

    def draw(self):
        pass

#Three linear equatons wtih integer solution 
class AlgebraProblem2: 

    def __init__(self):

        self.answerReceiver = "textBox2"
        self.answer = 0

        pass

    def equationBuilder(self, coefficient1, coefficient2, coefficient3, LHS):
        equationString = ""
        if (coefficient1 == 1):
            pass
        elif (coefficient1 == -1):
            equationString += "-"
        else:
            equationString += str(coefficient1)

        if (abs(coefficient2) == 1):
            equationString += "x + "
        elif (coefficient2 == -1):
            equationString += "x - "
        elif(coefficient2 < 0):
            equationString += "x - " + str(abs(coefficient2))
        else:
            equationString += "x + " + str(coefficient2)

        if (abs(coefficient3) == 1):
            equationString += "y + "
        elif (coefficient3 == -1):
            equationString += "y - "
        elif(coefficient3 < 0):
            equationString += "y - " + str(abs(coefficient3))
        else:
            equationString += "y + " + str(coefficient3)

        equationString += "z = " + str(LHS)
        return equationString
    
    def generateProblem(self):
        
        multiplier = False

        choice = random.randint(1,100)
        if (choice <= 90):
            rangeAnswer = 10
            rangeCoefficient = 15
        else:
            rangeAnswer = 15
            rangeCoefficient = 30

        answerX = random.randint(-1 * rangeAnswer , rangeAnswer)
        while (answerX == 0):
            answerX = random.randint(-1 * rangeAnswer , rangeAnswer)
        answerY = random.randint(-1 * rangeAnswer , rangeAnswer)
        while (answerY == 0):
            answerY = random.randint(-1 * rangeAnswer , rangeAnswer)
        answerZ = random.randint(-1 * rangeAnswer , rangeAnswer)
        while (answerZ == 0):
            answerY = random.randint(-1 * rangeAnswer , rangeAnswer)

        #First equation coefficients
        coefficient1x = random.randint(-1*rangeCoefficient, rangeCoefficient)
        while (coefficient1x == 0):
            coefficient1x = random.randint(-1 * rangeAnswer , rangeAnswer)
        coefficient1y = random.randint(-1*rangeCoefficient, rangeCoefficient)
        while (coefficient1y == 0):
            coefficient1x = random.randint(-1 * rangeAnswer , rangeAnswer)   
        coefficient1z = random.randint(-1*rangeCoefficient, rangeCoefficient)
        while (coefficient1z == 0):
            coefficient1z = random.randint(-1 * rangeAnswer , rangeAnswer)  

        #Second equation coefficients
        coefficient2x = random.randint(-1*rangeCoefficient, rangeCoefficient)
        while (coefficient2x == 0):
            coefficient2x = random.randint(-1 * rangeAnswer , rangeAnswer)
        coefficient2y = random.randint(-1*rangeCoefficient, rangeCoefficient)
        while (coefficient2y == 0):
            coefficient2y = random.randint(-1 * rangeAnswer , rangeAnswer)
        coefficient2z = random.randint(-1*rangeCoefficient, rangeCoefficient)
        while (coefficient2z == 0):
            coefficient2z = random.randint(-1 * rangeAnswer , rangeAnswer)   

        #Third equation coefficients
        coefficient3x = random.randint(-1*rangeCoefficient, rangeCoefficient)
        while (coefficient3x == 0):
            coefficient3x = random.randint(-1 * rangeAnswer , rangeAnswer)
        coefficient3y = random.randint(-1*rangeCoefficient, rangeCoefficient)
        while (coefficient3y == 0):
            coefficient3y = random.randint(-1 * rangeAnswer , rangeAnswer)
        coefficient3z = random.randint(-1*rangeCoefficient, rangeCoefficient)
        while (coefficient3z == 0):
            coefficient3z = random.randint(-1 * rangeAnswer , rangeAnswer)   
        
        LHS1 = answerX * coefficient1x + answerY * coefficient1y + answerZ * coefficient1z
        LHS2 = answerX * coefficient2x + answerY * coefficient2y + answerZ * coefficient2z
        LHS3 = answerX * coefficient3x + answerY * coefficient3y + answerZ * coefficient3z

        print(self.equationBuilder(coefficient1x, coefficient1y, coefficient1z, LHS1))
        print(self.equationBuilder(coefficient2x, coefficient2y, coefficient2z, LHS2))
        print(self.equationBuilder(coefficient3x, coefficient3y, coefficient3z, LHS3))
    

    def checkCorrect(self):
        pass

    def draw(self):
        pass

problem = AlgebraProblem2()
problem.generateProblem()