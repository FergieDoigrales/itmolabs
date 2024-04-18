import decimal

def getSolution(matrix):
    #print('Все работает??')
    diagMatrix = getDiagonal(matrix) #сюда передаем полную матрицу коэффициентов Х и свободных членов
    if diagMatrix != False:
        getCoeffMatrix(diagMatrix)
        #eps = input(f"Введите значение epsilon: ")
    else:
        print('Решить данную СЛАУ методом простых итераций нельзя.')

#проверка матрицы на соответствие виду диагонального преобладания
def checkDiagonal(matrix): # сюда передаем матрицу X
    count = 0
    result = False
    sum = 0
    for i in range(0, len(matrix)):
        for j in range(0, len(matrix[i])):
            sum+= abs(matrix[i][j])
        sum-= abs(matrix[i][i])          

        if abs(matrix[i][i]) >= sum:
            count+=1
        sum = 0
    
    if count == len(matrix):
        result = True
    return result

#приведение матрицы к виду диагонального преобладания и проверка на соответствие ему 
def getDiagonal(matrix): #сюда передаем полную матрицу
    alreadyDone = [[0] for _ in range(len(matrix[0]))]
    Xmatrix = getX(matrix)
    Bmatrix = getB(matrix)
    # for i in range(0, len(matrix)):
    #     for j in range (0, len(matrix[i])):
    #         if matrix[i][i] != max(matrix[i]):
    if checkDiagonal(Xmatrix) != True:
        for i in range(0, len(Xmatrix)):
            if Xmatrix[i][i] != max(Xmatrix[i]):
                if i not in alreadyDone:
                    for j in range(0, len(Xmatrix[i])):
                                max_index = Xmatrix[i].index(max(Xmatrix[i])) #индекс j строки, номер элемента 
                                tempX = Xmatrix[max_index]
                                tempB = Bmatrix[max_index]
                                Xmatrix[max_index] = Xmatrix[i]
                                Xmatrix[i] = tempX
                                Bmatrix[max_index] = Bmatrix[i]
                                Bmatrix[i] = tempB
                                alreadyDone.append(max_index)


        #return matrix
    if checkDiagonal(Xmatrix) == True:
        print('\n - Матрица находится в виде диагонального преобладания. - ')
        return matrix
    else:
        print('Заданную матрицу невозможно привести к виду диагонального преобладания.')
        for j in range(0, len(Xmatrix)):
            print(matrix[0][j])
            print(' ')
        print('\n')
                
        return False
                    
def checkNorm(CoeffMatrix):
        #absMatrix = CoeffMatrix
        result = False
        current = 0
        sumAbs = 0
        for i in range(0, len(CoeffMatrix)):
            CoeffMatrix[i][i] = 0
            for j in range(0, len(CoeffMatrix[i])):
                sumAbs+= abs(CoeffMatrix[i][j])
            if sumAbs > current:
                current = sumAbs
                sumAbs = 0

        if current < 1:
            result = True
            print(f"\nНорма матрицы ||C|| =  {current} < 1 ")
            print('Условие сходимости выполняется. \n')
        else:
            print("Условие сходимости не выполняется: норма матрицы больше 1, невозможно решить СЛАУ методом простых итераций.")
        return  result

#выражение Х
def getCoeffMatrix(matrix): #Где-то принимать эпсилон

    #эту функцию, наверное, лучше выделить в getDxC и как-то посчитать там же матрицу C
    Xmatrix = getX(matrix)
    Bmatrix = getB(matrix)
    CoeffMatrix = Xmatrix #поделенная на диаг. коэффициент матрица Х
    Dmatrix = Bmatrix #получаем матрицу d
    
    #делим все члены матрицы на коэффициенты диагональных элементов, получаем матрицу d и матрицу коэффициентов
    for i in range(0, len(CoeffMatrix)): #пока в матрице есть строки  
        Xcoeff = CoeffMatrix[i][i]
        Dmatrix[i]/= Xcoeff

        for j in range(0, len(CoeffMatrix[i])):
            CoeffMatrix[i][j]/= Xcoeff 
    print('\nПолученная матрица коэффициентов C:')
    for i in range (0, len(CoeffMatrix)):
        CoeffMatrix[i][i] = 0
        for j in range(0, len(CoeffMatrix[i])):
            if CoeffMatrix[i][j] == 0:
                print('0 ', end='')
            else:
                print(f"-{CoeffMatrix[i][j]} ", end='')
        print('\n')
    
    print('\nЗададим начальное приближение d:')
    print(Dmatrix)

    # #сюда вставить функцию проверки нормы
    # def checkNorm(CoeffMatrix):
    #     norm = 10
    #     current = 0
    #     for i in range(0, len(CoeffMatrix)):
    #         CoeffMatrix[i][i] = 0
    #         absSum = sum(abs(CoeffMatrix))
    #         if current < absSum:
    #             current = absSum
    #     if current < 1:
    #         return True
    #     else:
    #         print("Норма матрицы больше 1, невозможно решить СЛАУ методом простых итераций.")
    if checkNorm(CoeffMatrix) == True:

        #выражаем все х и выводим выражения 
        x_seq = [[0] for _ in range(len(CoeffMatrix))] #массив Хi равный кол-ву строк
        print('Чтобы выразить все хn, возьмем d за x0 в качестве начального приближения:')
        for i in range (0, len(CoeffMatrix)):
            x_seq[i] = 0
        
            print(f"x{i+1}(0) = ", end='')
            for j in range(0, len(CoeffMatrix[i])):
                if j!=i: #проверку в теории можно убрать после функции checkNorm
                    print(f"- {CoeffMatrix[i][j]} * {Dmatrix[j]} ", end='') 
                    x_seq[i] -= CoeffMatrix[i][j] * Dmatrix[j]

            x_seq[i] += Dmatrix[i]
            print(f"+ { Dmatrix[i]} = {round(x_seq[i], 10)}") #здесь округляется вывод, переделать потом

        max_eps = checkEps(x_seq, Dmatrix)
       
        eps = float(input(f"Введите значение epsilon: ").replace(",","."))

    
        answer = solution(CoeffMatrix, Dmatrix, x_seq, eps, max_eps)
        print(f"Приближенное решение задачи при eps = {eps}:")
        for i in range(0, len(answer)):
            print(f"x{i+1} = {answer[i]}")









def checkEps(Xseq, Dmatrix): #две одинарные матрицы, где Xseq - x+1, а Dmatrix = х
    print('\nКритерий по абсолютным отклонениям:')

    current = 0
    maxEpsilon = 0
    for i in range(0, len(Xseq)):
        operand1 = Xseq
        operand2 = Dmatrix
        current = abs(operand1[i] - operand2[i])
        print(f"x[n]({i+1}) - x[n-1]({i+1}) = {current} ")
        if current > maxEpsilon:
            maxEpsilon = current
    print(f"max = {maxEpsilon} \n")
    return maxEpsilon



def getX(matrix): #X[[X1,X2],[X1,X2]] и [B1, B2]
    return matrix[0]

def getB(matrix):
    return matrix[1]






#last: solution(CoeffMatrix, x_seq, max_eps, eps)
def solution(coeffMatrix, Dmatrix, x_seq, eps, max_eps): #x_seq - текущие значения, before_seq - полученные ранее значения (которые были х1х2х3 как b)
        #x_seq = coeffmatrix многомерный, x_seq - одномерный

        new_value_xseq = [[0] for _ in range(len(x_seq))] #массив Хi равный кол-ву строк
        k = 1
        while max_eps > eps:
        #for m in range(0,2):
            k+= 1
            print('Чтобы выразить все х, возьмем xn в качестве следующего приближения:')
            for i in range (0, len(coeffMatrix)):
                new_value_xseq[i] = 0
                
                print(f"x{i+1}({k}) = ", end='')
                for j in range(0, len(coeffMatrix[i])):
                    if j!=i: #проверку в теории можно убрать после функции checkNorm
                        print(f"- {coeffMatrix[i][j]} * {x_seq[j]} ", end='') 
                        new_value_xseq[i] -= coeffMatrix[i][j] * x_seq[j]

                new_value_xseq[i] += Dmatrix[i]
                print(f"+ { Dmatrix[i]} = {round(new_value_xseq[i], 10)}") #здесь округляется вывод, переделать потом
                # checkEps(new_value_xseq, x_seq)
                # x_seq = new_value_xseq
                #x_seq[i] = new_value_xseq[i]
            max_eps = checkEps(new_value_xseq, x_seq)
            x_seq = new_value_xseq.copy()
        print(f"Количество произведенных в ходе решения СЛАУ итераций  - {k} ")
        return new_value_xseq

