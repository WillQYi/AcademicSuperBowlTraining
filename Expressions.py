
def locationOperationValue(expression, center_X = int, center_Y = int):

    if (type(expression) is str):
        if (expression in ["cX", "cx", "centerX", "centerx", "CenterX", "Centerx", "Cx", "CX", "center_X", "center_x", "Center_X", "Center_x"]):
            return center_X
        elif (expression in ["cY", "cy", "centerY", "centery", "CenterY", "Centery", "y", "CY", "center_Y", "center_y", "Center_Y", "Center_y"]):
            return center_Y
        formatList = locationOperationFormatter(expression, center_X, center_Y)
    else:
        return expression
    
    #print(expression, type(expression))

    #print(formatList)

    exponentExists, processedListExponents = checkExponent(formatList, center_X, center_Y)
    while (exponentExists):
         exponentExists, processedListExponents = checkExponent(processedListExponents, center_X, center_Y)

    divisionExists, processedListDivision = checkDivision(processedListExponents, center_X, center_Y)
    while (divisionExists):
         divisionExists, processedListDivision = checkDivision(processedListDivision, center_X, center_Y)

    multiplicationExists, processedListMultiplication = checkMultiplication(processedListDivision, center_X, center_Y)
    while (multiplicationExists):
         multiplicationExists, processedListMultiplication = checkMultiplication(processedListMultiplication, center_X, center_Y)

    additionExists, processedListAddition = checkAddition(processedListMultiplication, center_X, center_Y)
    while (additionExists):
        additionExists, processedListAddition = checkAddition(processedListAddition, center_X, center_Y)

    subtractionExists, processedListSubtraction = checkSubtraction(processedListAddition, center_X, center_Y)
    while (subtractionExists):
        subtractionExists, processedListSubtraction = checkSubtraction(processedListSubtraction, center_X, center_Y)

    return processedListSubtraction[0]

# Computes values for exponents symbols
def checkExponent(formatList, center_X, center_Y):

    processedListExponents = []
    i = len(formatList)-1
    exponentExists = False
    while (i > 0):
        #print(str(processedListExponents) + " " + str(i))
        if (formatList[i-1] == "^" and exponentExists == False):
            processedListExponents.append(formatList[i-2]**formatList[i])
            exponentExists = True
            i -= 3
        else: 
            processedListExponents.append(formatList[i])
            i -= 1
    if (formatList[1] != "^"):
        processedListExponents.append(formatList[0])

    processedListExponents.reverse()

    #print(processedListExponents)

    return exponentExists, processedListExponents

# Computes values for division symbols
def checkDivision(formatList, center_X, center_Y):

    divisionExists = False
    processedListDivision = []
    i = 0
    while (i < len(formatList)-1):
        if (formatList[i+1] == "/"):
            divisionExists = True
            if (formatList[i+2] != 0):
                processedListDivision.append(formatList[i]/formatList[i+2])
            else:
                return "DIVISION BY 0"
            i += 3
        else: 
            processedListDivision.append(formatList[i])
            i += 1
    if (formatList[len(formatList)-2] != "/"):
        processedListDivision.append(formatList[len(formatList)-1])

    #print(processedListDivision)

    return divisionExists, processedListDivision

# Computes values for multiplication symbols
def checkMultiplication(formatList, center_X, center_Y):

    multiplicationExists = False
    processedListMultiplication = []
    i = 0
    while (i < len(formatList)-1):
        if (formatList[i+1] == "*"):
            multiplicationExists = True
            processedListMultiplication.append(formatList[i]*formatList[i+2])
            i += 3
        else: 
            processedListMultiplication.append(formatList[i])
            i += 1
    if (formatList[len(formatList)-2] != "*"):
        processedListMultiplication.append(formatList[len(formatList)-1])

    #print(processedListMultiplication)

    return multiplicationExists, processedListMultiplication

# Computes values for addition symbols
def checkAddition(formatList, center_X, center_Y):

    additionExists = False
    processedListAddition = []
    i = 0
    while (i < len(formatList)-1):
        if (formatList[i+1] == "+"):
            additionExists = True
            processedListAddition.append(formatList[i]+formatList[i+2])
            i += 3
        else: 
            processedListAddition.append(formatList[i])
            i += 1
    if (formatList[len(formatList)-2] != "+"):
        processedListAddition.append(formatList[len(formatList)-1])

    #print(processedListAddition)

    return additionExists, processedListAddition

# Computes values for subtraction symbols
def checkSubtraction(formatList, center_X, center_Y):

    subtractionExists = False
    processedListSubtraction = []
    i = 0
    while (i < len(formatList)-1):
        if (formatList[i+1] == "-"):
            subtractionExists = True
            processedListSubtraction.append(formatList[i]-formatList[i+2])
            i += 3
        else: 
            processedListSubtraction.append(formatList[i])
            i += 1
    if (formatList[len(formatList)-2] != "-"):
        processedListSubtraction.append(formatList[len(formatList)-1])

    #print(processedListSubtraction)

    return subtractionExists, processedListSubtraction

def locationOperationFormatter(string, center_X, center_Y):

    #Removing Spaces
    string = string.split(" ")

    string = "".join(string)

    value = 0
    
    formatList = []
    operations = ["+","-","*","/","^", "(",")"]

    #Turning into a list of numbers and operations
    substring = ""
    for i in range(len(string)):
        if (string[i] in operations):
            if (substring in ["cX", "cx", "centerX", "centerx", "CenterX", "Centerx", "Cx", "CX", "center_X", "center_x", "Center_X", "Center_x"]):
                formatList.append(center_X)
            elif (substring in ["cY", "cy", "centerY", "centery", "CenterY", "Centery", "y", "CY", "center_Y", "center_y", "Center_Y", "Center_y"]):
                formatList.append(center_Y)
            elif (substring == ""):
                formatList.append(0)
            else:
                formatList.append(float(substring))
            formatList.append(string[i])
            substring = ""
        else:
            substring += string[i]
    if (substring == "cX"):
        formatList.append(center_X)
    elif (substring == "cY"):
        formatList.append(center_Y)
    elif (substring == ""):
        formatList.append(0)
    else:
        formatList.append(float(substring))

    return formatList

#Testing
#print(locationOperationValue("5*5+10/cY + 100 -3^5", 500, 300))
