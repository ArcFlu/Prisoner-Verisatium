from asyncore import loop
from random import random
import random
from re import search

def initBoxes() -> list[int]:
    boxes = [0] * numPrisoners
    currIndex = 0

    listPrisonerNums = []
    for n in range(0, numPrisoners):
        listPrisonerNums.append(n)

    while len(listPrisonerNums) > 0:
        number = random.choice(listPrisonerNums)
        listPrisonerNums.remove(number)
        boxes[currIndex] = number
        currIndex += 1

    # for b in range(0, len(boxes), 10):
    #     print(boxes[b:b+10])

    return boxes

def searchBoxes(boxes, prisonerNumber) -> int:
    currBox = boxes[prisonerNumber]
    loopLength = 1
    while currBox != prisonerNumber:
        if loopFlag:
            if loopLength > maxLoopLength:
                return loopLength

        currBox = boxes[currBox]
        loopLength += 1
    
    return loopLength

def simulation() -> bool:
    boxes = initBoxes()
    maxLoop = 0
    for i in range(0, numPrisoners):
        loopLength = searchBoxes(boxes, i)
        if loopFlag and loopLength > maxLoopLength:
            return False
        maxLoop = max(maxLoop, loopLength)

    sumLoops.append(maxLoop)
    if maxLoop > maxLoopLength:
        return False

    return True

numPrisoners = 100
maxLoopLength = 50
sumLoops = []
loopFlag = True
failures = 0
successes = 0
numCases = 1000
for i in range(0, numCases):
    if simulation():
        successes += 1
    else:
        failures += 1

successRate = float(successes/numCases)

print()
print('Success Rate: ' + f'{successRate:.3f}')
if loopFlag:
    print('Average size of successful loops: ' + str(sum(sumLoops)/successes))
else:
    print('Average size of all loops: ' + str(sum(sumLoops)/numCases))
print()