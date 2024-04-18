import matplotlib.pyplot as plt
import numpy as np

def f(x):
    return np.log(1 + x**2) - np.sin(x)

def df(x):
    return ((2 * x) / (1 + x**2)) - np.cos(x)

def d2fdx(x):
    return ((2-2*x**2)/(1+x**2)**2+np.sin(x))

def bisection_method(a, b, epsilon, delta, iteration_limit):

    iteration_cnt = 0

    while iteration_limit > 0:

        x1 = (b + a - delta) / 2
        x2 = (b + a + delta) / 2

        f_x1 = f(x1)
        f_x2 = f(x2)

        if (f_x1 <= f_x2):
            b = x2
        else:
            a = x1

        epsilon_n = (b - a) / 2

        print(f"Итерация №{iteration_cnt}: a = {round(a, 5)}, b = {round(b, 5)}, (b - a)/2 = {round(epsilon_n, 5)}, x1 = {round(x1, 5)}, x2 = {round(x2,5)}, f(x1) = {round(f_x1, 5)}, f(x2) = {round(f_x2, 5)}", end=', ')
        if f_x1 < f_x2:
            print(f"f(x1) < f(x2)")
        else:
            print(f"f(x1) > f(x2)")

        if epsilon_n <= epsilon:
            break
        iteration_cnt += 1
        iteration_limit -= 1

    print(f"Лимит итераций исчерпан: x* = {round(( (a+b) / 2), 5)}, f*(x) = {round( f( (a+b) / 2 ), 5)}")


def golden_section_method(a, b, epsilon, delta, iteration_limit):

    iteration_cnt = 0
    
    while iteration_limit > 0:

        x1 = a + (3 - np.sqrt(5)) / 2 * (b - a)
        x2 = a + (np.sqrt(5) - 1) / 2 * (b - a)

        f_x1 = f(x1)
        f_x2 = f(x2)

        T = ((np.sqrt(5) - 1)) / 2

        epsilon_n = (b - a) / 2
        if epsilon_n <= epsilon:
            break

        if f_x1 <= f_x2:
            b = x2
            x2 = x1
            f_x2 = f_x1
            x1 = b - T * (b - a)
            f_x1 = f(x1)
        else:
            a = x1
            x1 = x2
            f_x1 = f_x2
            x2 = a + T * (b - a)
            f_x2 = f(x2)
            epsilon_n *= T

        print(f"Итерация №{iteration_cnt + 1}: a = {round(a, 5)}, b = {round(b, 5)}, epsilon_n = {round(epsilon_n, 5)}, x1 = {round(x1, 5)}, x2 = {round(x2, 5)}, f(x1) = {round(f_x1, 5)}, f(x2) = {round(f_x2, 5)}", end=', ')
        if f_x1 < f_x2:
            print(f"f(x1) < f(x2)")
        else:
            print(f"f(x1) > f(x2)")
        
        iteration_cnt += 1
        iteration_limit -= 1

    print(f"Лимит итераций исчерпан: x* = {round(((a+b)/2), 5)}, f*(x) = {round(f((a+b)/2), 5)}")
    

def newton_method(x0, epsilon, iteration_limit):
    iteration_cnt = 0
    while iteration_limit > 0:

        df_dx = df(x0)
        d2f_dx2 = d2fdx(x0)

        x1 = x0 - (df_dx/d2f_dx2)

        print(f"Итерация №{iteration_cnt + 1}: k = {iteration_cnt}, xk = {round(x1, 5)}, f(xk) = {round(f(x1), 5)}, f'(xk) = {round(df(x1), 5)}")
        
        if abs(df(x1)) <= epsilon:
            break

        x0 = x1
        
        iteration_cnt += 1
        iteration_limit -= 1
    print(f"Достигнут критерий epsilon: x* = {round((x1), 5)}, f*(x) = {round(f(x1), 5)}, f*'(x) = {df(x1)}")

def graphical_method(a, b):
    x_values = np.linspace(a, b, 1000)
    y_values = [f(x) for x in x_values]
    plt.plot(x_values, y_values)
    plt.xlabel("x")
    plt.ylabel("f(x)")
    plt.title("Графическое решение:")
    plt.grid(True)
    plt.show()

# Параметры
a = 0 
b = np.pi / 4
epsilon = 1e-10
delta = epsilon
iteration_limit = 25
x0 = (a + b) / 2

print("Решение методом деления пополам:")
bisection_method(a, b, epsilon, delta, iteration_limit)
print()

print("Решение методом золотого сечения:")
golden_section_method(a, b, epsilon, delta, iteration_limit)
print()

print("Решение методом Ньютона:")
newton_method(x0, epsilon, iteration_limit)
print()

# Интервал и точки для построения графика
a = 0
b = np.pi / 4
x_values = np.linspace(a, b, 1000)
y_values = f(x_values)

# График
plt.plot(x_values, y_values, label='$f(x) = \ln(1 + x^2) - \sin(x)$')
plt.xlabel('x')
plt.ylabel('f(x)')
plt.title('График функции $f(x)$')
plt.grid(True)
plt.legend()
plt.show()