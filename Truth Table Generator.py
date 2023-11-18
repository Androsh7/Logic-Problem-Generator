import random

# solves a logic problem by taking two 8 digit long truth tables and uses the operator to create a new 8 integer truth table
# problem setup is as follows:  inputTable1 Operator inputTable2
# example:                          p          ^         q

# takes a 1d array (inputTable) and puts it as the subarray of outTable at location outTableNum
def copy2dArray (inputTable, outTable,outTableNum):
    for i in range(0,8):
        inputTable[i] = outTable[outTableNum][i]

# takes two logic arrays and creates a solution table based on the operator
def solve2varLogic (inputTable1, inputTable2, operator):
    outTable = [2,2,2,2,2,2,2,2] # array is set to 2 for output debugging purposes
    i = 0
    for x in outTable:  
        
        # not operand 
        # note: this only looks at inputTable1
        if operator == '/':
            if inputTable1[i] == 1:
                outTable[i] = 0
            else:
                outTable[i] = 1
        
        # and operand
        elif operator == '|':
            if inputTable1[i] == 1 or inputTable2[i] == 1:
                outTable[i] = 1
            else:
                outTable[i] = 0
        
        # or operand
        elif operator == '&':
            if inputTable1[i] == 1 and inputTable2[i] == 1:
                outTable[i] = 1
            else:
                outTable[i] = 0

        # xor operand
        elif operator == '^':
            if (inputTable1[i] == 1 and inputTable2[i] == 0) or (inputTable1[i] == 0 and inputTable2[i] == 1):
                outTable[i] = 1
            else:
                outTable[i] = 0

        # conditional operand
        elif operator == '>':
            if inputTable1[i] == 1 and inputTable2[i] == 0:
                outTable[i] = 0
            else:
                outTable[i] = 1
        
        # bi-conditional operand
        elif operator == '=':
            if (inputTable1[i] == 1 and inputTable2[i] == 1) or (inputTable1[i] == 0 and inputTable2[i] == 0):
                outTable[i] = 1
            else:
                outTable[i] = 0
        
        # placeholder operand
        elif operator == '@':
            outTable[i] = inputTable1[i]

        i = i + 1
    print ("solving:",inputTable1,operator, inputTable2, "answer:",outTable)
    return outTable

inputTable1 = [3,3,3,3,3,3,3,3]
inputTable2 = [4,4,4,4,4,4,4,4]

# takes an array of logic problems and appends each output to outputArray
def solve3varLogic (inputArray,outputArray):
    p = [1,1,1,1,0,0,0,0] 
    q = [1,1,0,0,1,1,0,0]
    r = [1,0,1,0,1,0,1,0]
    
    # not p, not q, not r
    t = [0,0,0,0,1,1,1,1]
    u = [0,0,1,1,0,0,1,1]
    v = [0,1,0,1,0,1,0,1]
    
    i = 0
    for x in inputArray:
        
        # sets inputTable1
        if inputArray[i][0] == 'p':
            inputTable1 = p
        elif inputArray[i][0] == 'q':
            inputTable1 = q
        elif inputArray[i][0] == 'r':
            inputTable1 = r
        elif inputArray[i][0] == 't':
            inputTable1 = t
        elif inputArray[i][0] == 'u':
            inputTable1 = u
        elif inputArray[i][0] == 'v':
            inputTable1 = v
        elif int(inputArray[i][0]) >= 0:
            copy2dArray(inputTable1,outputArray,inputArray[i][0])
        
        # sets inputTable2
        if inputArray[i][2] == 'p':
            inputTable2 = p
        elif inputArray[i][2] == 'q':
            inputTable2 = q
        elif inputArray[i][2] == 'r':
            inputTable2 = r
        elif inputArray[i][2] == 't':
            inputTable2 = t
        elif inputArray[i][2] == 'u':
            inputTable2 = u
        elif inputArray[i][2] == 'v':
            inputTable2 = v
        elif int(inputArray[i][2]) >= 0:
            copy2dArray(inputTable2,outputArray,inputArray[i][2])
        
        outputArray.append(solve2varLogic(inputTable1,inputTable2,inputArray[i][1]))
        #copy2dArray(solve2varLogic(inputTable1,inputTable2,inputArray[i][1]),outputArray,i)
        i = i + 1

# turns each row of the problemArray into a string as part of the outputStringArray
# then the function condenses the array based on problems referencing other problems
# step 1:   [['p','|','q'],[0,'&','r'] to ['p or q','0 and r']     translates symbols to words
# step 2:   [['p or q'],['0 and r']] to ['','(p or q) and r']      combines the logic strings
# step 3:   ['','(p or q) and r'] to '(p or q) and r'              turns the array into a single string
def logicToStr (inputArray):
    outputStringArray = []
    
    #step 1
    #converts each row into a string and places it in the array outputStringArray
    stringToPass = ""
    rows = 0
    columns = 0
    while rows < len(inputArray):
        while columns < 3:
            
            # char to str conversions
            if (inputArray[rows][columns]) == 'p':
                stringToPass = stringToPass + 'p'
            elif (inputArray[rows][columns]) == 'q':
                stringToPass = stringToPass + 'q'
            elif (inputArray[rows][columns]) == 'r':
                stringToPass = stringToPass + 'r'
            elif (inputArray[rows][columns]) == 't':
                stringToPass = stringToPass + 'not p'
            elif (inputArray[rows][columns]) == 'u':
                stringToPass = stringToPass + 'not q'
            elif (inputArray[rows][columns]) == 'v':
                stringToPass = stringToPass + 'not r'
            elif (inputArray[rows][columns]) == '|':
                stringToPass = stringToPass + ' or '
            elif (inputArray[rows][columns]) == '&':
                stringToPass = stringToPass + ' and '
            elif (inputArray[rows][columns]) == '^':
                stringToPass = stringToPass + ' xor '
            elif (inputArray[rows][columns]) == '@':
                stringToPass = stringToPass
            elif (inputArray[rows][columns]) == '>':
                stringToPass = stringToPass + ' --> '
            elif (inputArray[rows][columns]) == '/':
                stringToPass = stringToPass + ' not'
            elif (inputArray[rows][columns]) == '=':
                stringToPass = stringToPass + ' <-> '
            else:
                stringToPass = stringToPass + str(inputArray[rows][columns])
            columns = columns + 1
        outputStringArray.append(stringToPass)
        stringToPass = ''
        rows = rows + 1
        columns = 0
    
    #print("outputArray p1:",outputStringArray)
    
    #step 2
    #looks at the outputStringArray and replaces 0s through 3s with their corresponding sections in the outputStringArray to pass
    toDelete = []
    stringNum = 0
    charNum = 0
    stringToPass = ''
    for checkNum in range (0,len(inputArray)-1):
        while stringNum < len(inputArray):
            while charNum < 3:
                if inputArray[stringNum][charNum] == checkNum:
                    stringToPass = outputStringArray[stringNum]
                    stringToPass = stringToPass.replace(str(checkNum),"(" + outputStringArray[checkNum] + ")")
                    outputStringArray[stringNum] = stringToPass
                    toDelete.append(checkNum)
                    stringToPass = ""
                charNum = charNum + 1
            stringNum = stringNum + 1
            charNum = 0
        stringNum = 0
    
    #deletes duplicates
    for i in toDelete:
        outputStringArray[i] = ""
    
    
    # step 3
    # outputs the completed problem as a string
    FinalString = ""
    for i in range (0,len(outputStringArray)):
        FinalString = FinalString + outputStringArray[i]
    print(outputStringArray)
    return FinalString
    
def genLogic (seed, length):
    outputLogic = []
    intsWrittenRaw = []
    intsWrittenSortedUnique = []
    
    random.seed(seed)
    
    varPlacesMax = length * 2
    varPlacesLeft = length * 2
    varWritten = 0
    
    charsToAdd = ['@','@','@']
    stringNum = 0
    charNum = 0
    while stringNum < length:
        x = 0  
        while charNum < 3:
            
            for value in intsWrittenRaw:
                if value not in intsWrittenSortedUnique:
                    intsWrittenSortedUnique.append(value)
            intsWrittenSortedUnique = sorted(intsWrittenSortedUnique)
            
            # determines the operand for the problem
            if charNum == 1:
                randomNum = random.randint(0,5)
                if randomNum == 0:
                    charsToAdd[charNum] = '&'
                elif randomNum == 1:
                    charsToAdd[charNum] = '|'
                elif randomNum == 2:
                    charsToAdd[charNum] = '&'
                elif randomNum == 3:
                    charsToAdd[charNum] = '^'
                elif randomNum == 4:
                    charsToAdd[charNum] = '>'
                elif randomNum == 5:
                    charsToAdd[charNum] = '='
            
            # checks to see if the program needs to start forcing integer inputs
            #      ints that need to be inputed  >= the remaining locations that integers can be placed in
            elif length - varWritten > varPlacesLeft:
                print("if",length - varWritten,varPlacesLeft)
                print("range:",len(intsWrittenSortedUnique) - 1,length - 2)
                for i in range (0, length -2):
                    if i not in intsWrittenSortedUnique:
                        if isinstance(charsToAdd[charNum], int):
                            print("skip")
                        elif i >= (len(intsWrittenSortedUnique) - 1):
                            charsToAdd[charNum] = i
                            intsWrittenRaw.append(i)
                            varPlacesLeft = varPlacesLeft - 1
                            varWritten = varWritten + 1
                            print("force1: ",i, "at",stringNum,charNum,x)
                        elif i != intsWrittenSortedUnique[i]:
                            charsToAdd[charNum] = i 
                            intsWrittenRaw.append(i)
                            varPlacesLeft = varPlacesLeft - 1
                            varWritten = varWritten + 1
                            print("force2: ",i, "at",stringNum,charNum,x)
                        

                    
                    print(charsToAdd)
            else:
                randomNum = random.randint(0,5 + stringNum)
                # char to str conversions
                if randomNum == 0:
                    charsToAdd[charNum] = 'p'
                elif randomNum == 1:
                    charsToAdd[charNum] = 'q'
                elif randomNum == 2:
                    charsToAdd[charNum] = 'r'
                elif randomNum == 3:
                    charsToAdd[charNum] = 't'
                elif randomNum == 4:
                    charsToAdd[charNum] = 'u'
                elif randomNum == 5:
                    charsToAdd[charNum] = 'v'
                else:
                    charsToAdd[charNum] = randomNum - 6
                    intsWrittenRaw.append(randomNum - 6)
                varPlacesLeft = varPlacesLeft - 1
            charNum = charNum + 1
            
            # updates the sorted and unique array
            for value in intsWrittenRaw:
                if value not in intsWrittenSortedUnique:
                    intsWrittenSortedUnique.append(value)
            intsWrittenSortedUnique = sorted(intsWrittenSortedUnique)
        print("intsWrittenRaw = ",intsWrittenRaw)
        print("intsWrittenSortedUnique = ",intsWrittenSortedUnique)
    
        stringNum = stringNum + 1
        charNum = 0
        outputLogic.append(charsToAdd)
        print("Added chars: ",charsToAdd)
        charsToAdd = ['@','@','@']
    return outputLogic
        
# contains the output of the corresponding problemArray section
solutionArray = []

#example:
#problemArray = [['r','|','q'],['p','&','q'],[0,'&',1],[1,'^',2]]
#                p1 = r|q    p2 = p&q       p3 = p1&p2  p2^p3
# text output:        (p v q) -> r
# @ = placeholder value

while True:
    userSeed = int(input("seed = "))
    userSize =int(input("size = "))
    if userSize < 3:
        print("ERROR SIZE < 3")
    else:
        problemArray = genLogic(userSeed,userSize)
        print("raw problem:",problemArray)
        print("str problem:",logicToStr(problemArray))
        solve3varLogic(problemArray,solutionArray)
        print("solution: ", solutionArray)
        problemArray = []
        solutionArray = []
    print("---------")
