#Ввод матрицы
#создать класс и к методам приписать Matrix.method ?

# Xmatrix = [] 
# Bmatrix = []
import random

#ввод строк матрицы с консоли
def inputFromConsole(n):
    strList = []
    try:
        if n > 20:
            print('Размерность матрицы не может превышать n=20!')
        else:
            i = 0
            print('Вводите матрицу и векторы по одной строке строго формата a11 a12 a13 a1n | b1.')
            while i < n:
                str = input(f"Введите {i+1}-ую строку матрицы: ") 
                strList.append(str) #обработать исключение, если пользователь ввел неправильную или пустую строку
                i+=1
            

#придумать где сохранять массивы, чтобы не переиспользовать ресурс
            #matrix = setMatrix(strList)
            # Xmatrix = setMatrix(strList).getMatrixCoefficients() 
            # Bmatrix = setMatrix(strList).getVectorCoefficients()

            # print('Проверьте Вашу матрицу:')
            # print(matrix)
        return setMatrix(strList)
            


    except Exception:
        print("Кажется, Вы не ввели число. Или ввели не число. Кто знает...")

#чтение строк матрицы с файла
def inputFromFile(path): #считать количество строк в файле как размерность n
    strList = []
    i = 0
    try:
        #file = open(path)
        with open(path) as file:
            # while True:
            #     str = file.readline() #можно использовать file.readlines() - список всех строк
            #     if len(str) == 0: 
            #         break
            #     else:
            #         for str in file:
            #             str.replace('//n','')
            #             strList.append(str)
            #             i+=1
            for line in file:
                str = line
                if len(str) == 0:
                    break
                else:
                    
                    strList.append(str.replace("\n",""))
                    i+=1
        #file.close
            #matrix = setMatrix(strList)
        return setMatrix(strList)
    except FileNotFoundError: #обработать потом все исключения
        print(f"Файл по указанному пути {path} не найден.")
        print('Во время чтения файла произошла какая-то ошибка. Попробуйте еще раз.')

#преобразование полученного массива строк в матрицу (коэффициенты х и свободные члены в отдельных массивах)
def setMatrix(strList): #сюда должен передаваться массив строк
    fullMatrix = [[0] for _ in range(2)] #итоговая матрица(кортеж матриц X  и B), над которой будут производиться вычисления
    #n рассчитываем из кол-ва переданных строк
    n = len(strList)

    str #придумать как эту строку передать
    matrix_of_coefficients = [[0]*n for _ in range(n)] #пустая матрица размерностью n*n
    matrix_of_vectors = [[0] for _ in range(n)]
    i = 0 #счетчик кол-ва строк
    try:
        while i < n:
            current_str = strList[i].replace(",", ".") #получаем первую строку матрицы

            elements = current_str.split()
            str_coefficient_count = (current_str.replace("| ","")).split() #убираем разделитель для подсчета кол-ва коэфф-ов

            element_count = (len(str_coefficient_count) - 1) #тут можно через matrix_coefficient.len потом сделать
            if element_count != n: 
                #тут прога ломается, если нарушена размерность
                #print('Возникла проблема со строкой №' + str(i+1))
                raise ValueError('Матрица не является квадратной.')
                matrix_of_coefficients.clear()
                matrix_of_vectors.clear()
                break # тут то ли не обнуляются массивы, то ли хз
            elif element_count == n: #тут мы получаем одномерный массив из введенной строки и вектор
                separator_index = elements.index("|")
                matrix_coefficients = list(map(float, elements[:separator_index]))
                #matrix_coefficients = list(map(float, list(elements[:separator_index])))
                vector_coefficient = float(elements[separator_index + 1])

                matrix_of_coefficients[i] = matrix_coefficients
                
                matrix_of_vectors[i] = vector_coefficient
            
        
                i+=1
                #тут логика заполнения массива строками
        #print('\nПерепроверьте матрицы:')
        #print(matrix_of_coefficients)
        #print(matrix_of_vectors)
        print('\nМатрица коэффициентов X:')
        for j in range(0, len(matrix_coefficients)-1):
            print(matrix_of_coefficients[j])
    
        print('\nМатрица свободных членов B:')
        print(matrix_of_vectors)

        fullMatrix[0] = matrix_of_coefficients
        fullMatrix[1] = matrix_of_vectors
        return fullMatrix
    except ValueError as e:
        if str(e) != "\'|\'is not in list":
            print("Возможно, Вы забыли обозначить разделитель матрицы и вектора - \"|\" или не соблюли размерность матрицы.\nПопробуйте снова.")

def getRandomMatrix(n):
    fullMatrix = [[0] for _ in range(2)]
    n = int(n)

    if n <= 20:

        matrix_of_coefficients = [[0]*n for _ in range(n)] 
        matrix_of_vectors = [[0] for _ in range(n)]

        i = 0 #счетчик кол-ва строк
        for i in range(0, len(matrix_of_coefficients)):
            for j in range(0, len(matrix_of_coefficients[i])):
                matrix_of_coefficients[i][j] = random.randint(-20, 20)

        for i in range(0, len(matrix_of_vectors)):
            matrix_of_vectors[i] = random.randint(-20, 20)
            #matrix_of_vectors.append(random.random())
        
        fullMatrix[0] = matrix_of_coefficients
        fullMatrix[1] = matrix_of_vectors
        return fullMatrix

    else:
        print('Размерность матрицы не может превышать n = 20.')






         
        
        



