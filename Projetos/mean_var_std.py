import numpy as np

def meanCalculate(matrix):
    meanList = []
    meanAxis1 = matrix.mean(axis=0, dtype=float).tolist()
    meanAxis2 = matrix.mean(axis=1, dtype=float).tolist()
    meanMatrix = matrix.mean(dtype=float).tolist()

    meanList.append(meanAxis1)
    meanList.append(meanAxis2)
    meanList.append(meanMatrix)

    return meanList

def variance(matrix):
    varianceList = []
    varAxis1 = matrix.var(axis=0,dtype=float).tolist()
    varAxis2 = matrix.var(axis=1,dtype=float).tolist()
    varMatrix = matrix.var(dtype=float).tolist()

    varianceList.append(varAxis1)
    varianceList.append(varAxis2)
    varianceList.append(varMatrix)
    return varianceList

def standardDeviation(matrix):
    standarDeviation = []
    stdAxis1 = matrix.std(axis=0).tolist()
    stdAxis2 = matrix.std(axis=1).tolist()
    stdMatrix = matrix.std().tolist()

    standarDeviation.append(stdAxis1)
    standarDeviation.append(stdAxis2)
    standarDeviation.append(stdMatrix)
    return standarDeviation

def maxCalculate(matrix):
    maxList = []
    maxAxis1 = matrix.max(axis=0).tolist()
    maxAxis2 = matrix.max(axis=1).tolist()
    maxMatrix = matrix.max().tolist()

    maxList.append(maxAxis1)
    maxList.append(maxAxis2)
    maxList.append(maxMatrix)
    return maxList

def minCalculate(matrix):
    minList = []
    minAxis1 = matrix.min(axis=0).tolist()
    minAxis2 = matrix.min(axis=1).tolist()
    minMatrix = matrix.min().tolist()

    minList.append(minAxis1)
    minList.append(minAxis2)
    minList.append(minMatrix)
    return minList

def sumCalculate(matrix):
    sumList = []
    sumAxis1 = matrix.sum(axis=0).tolist()
    sumAxis2 = matrix.sum(axis=1).tolist()
    sumMatrix = matrix.sum().tolist()

    sumList.append(sumAxis1)
    sumList.append(sumAxis2)
    sumList.append(sumMatrix)
    return sumList

def calculate(numbers : list):
    if(len(numbers) != 9):
        print("List must contain nine numbers")
        return
    
    dicOfAllThings = {}
    matrix = np.array(numbers).reshape(3,3)
    dicOfAllThings['mean'] = meanCalculate(matrix)
    dicOfAllThings['variance'] = variance(matrix)
    dicOfAllThings['standard deviation'] = standardDeviation(matrix)
    dicOfAllThings['max'] = maxCalculate(matrix)
    dicOfAllThings['min'] = minCalculate(matrix)
    dicOfAllThings['sum'] = sumCalculate(matrix)

    print('{') 
    for key, value in dicOfAllThings.items(): 
        print(f" '{key}': {value},") 
    print('}')


list = []

for i in range(0,9):
    print("TYPE 12345 TO EXIT")
    number = int(input("Type a number: "))
    if number == 12345:
        break
    else:
        list.append(number)

calculate(list)
    

    