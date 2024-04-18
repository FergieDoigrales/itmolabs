import validator
import numpy  as np
from scipy.misc import derivative
    
def f(quation, x):
    if quation == 1:
        return np.float64(x**3 + 2*x**2 - 5)
    if quation == 2:
        return np.float64(3*x**2 + 5*x - 4)
    if quation == 3:
        return np.float64(1 - 3*x + np.sin(x)) #трансцендентное


def fdx(quation, x):
    if quation == 1:
        return np.float64(3*x**2 + 4*x)
    if quation == 2:
        return np.float64(6*x + 5)
    if quation == 3:
        return np.float64(np.cos(x)) - 3

def f2dx(quation, x):
    if quation == 1:
        return np.float64(6*x + 4)
    if quation == 2:
        return 6
    if quation == 3:
        return -(np.sin(x)) #трансцендентное
    

def check_derivative_sign(f, a, b):
    # для генерации равномерно распределенных точек внутри отрезка [a, b]
    x_values = np.linspace(a, b, 100)
    
    for x in x_values:
        if derivative(f, x, dx=1e-6) == 0:
            continue
        derivative_sign = np.sign(derivative(f, x, dx=1e-6))
        
        if derivative_sign == 0:
            continue
        
        if derivative_sign != np.sign(f(a)):
            #"Производная не сохраняет знак внутри отрезка."
            return False
    
    return True


def count_roots(a, b, quation, e):
    b1 = b
    num_roots = 0
    x = a
    while x < b1:
        if f(quation, x) * f(quation, x + e) < 0:
            num_roots += 1
        x += e
    return num_roots

#работает
def chorde_method(a, b, quation_num, e): 
    if validator.check_epsilon(e) is False:
        return "Epsilon cannot be less than zero."
    if validator.check_range(a, b) is False:
        return "The left border cannot be larger than the right!" 
    
    if count_roots(a,b, quation_num, e) == 1:
        prev_x = 0
        x = a - ((b-a)/(f(quation_num, b)- f(quation_num, a)))* f(quation_num, a)
        iter_cnt = 1
        max_iter = 200
        answer = []

        while abs(f(quation_num, x)) <= e or abs(a-b) <= e or abs(x - prev_x) <= e or iter_cnt < max_iter:
            if (f(quation_num, a) * f(quation_num, x)) < 0: #проверка на то, что знаки у границ разные
                b = x
            else: 
                a = x
            prev_x = x
            x = a - ((b-a)/(f(quation_num, b)- f(quation_num, a)))* f(quation_num, a)
            iter_cnt += 1

            if abs(f(quation_num, x)) <= e or abs(a-b) <= e or abs(x - prev_x) <= e or iter_cnt >= max_iter: #критерий окончания итерационного процесса
                break

        answer.append(x)
        answer.append((f(quation_num, x)))
        answer.append(iter_cnt)

        return answer
    else:
        return "The system has several solutions \n or none at all."
    

def newton_method(a, b, quation_num, e):
    if validator.check_epsilon(e) is False:
        return "Epsilon cannot be less than zero."
    if validator.check_range(a, b) is False:
        return "The left border cannot be larger than the right!" 
    
    if count_roots(a, b, quation_num, e) == 1:
            
        iterations = 0
        max_iter = 250
        x = 0
        answer = []

        f_a = f(quation_num, a)
        f_b =  f(quation_num, b)
        dx2df_a = f2dx(quation_num, a)
        dx2df_b = f2dx(quation_num, b)

        if f_a * dx2df_a > 0:
            x = a
        elif f_b * dx2df_b > 0:
            x = b
        else:
            return "No suitable initial approximation\nfound on the interval [a, b]"
            
        while abs(f(quation_num,x)) > e and iterations < max_iter:
            x = x - f(quation_num,x) / fdx(quation_num,x)
            iterations += 1
                    
        answer.append(x)
        answer.append("{:.8f}".format((f(quation_num, x))))
        answer.append(iterations)
                    
        return answer
    else:
        return "The system has several solutions \nor none at all."


def iteration_method_single(a, b, quation_num, epsilon):
    if validator.check_epsilon(epsilon) is False:
        return "Epsilon cannot be less than zero."
    if validator.check_range(a, b) is False:
        return "The left border cannot be larger than the right!" 
    if count_roots(a, b, quation_num, epsilon) == 1:

        def phi(x, lambda_factor):
            phi = x + lambda_factor * f(quation_num, x)
            return phi
                
        def phi_dx(x, lambda_factor):
            phi_dx = 1 + lambda_factor * fdx(quation_num, x)
            return phi_dx
                
        answer = []
        iterations = 0

        x = a

        max_fdx = max(abs(fdx(quation_num, a)), abs(fdx(quation_num, b)))
        if fdx(quation_num, a) * fdx(quation_num, b) > 0:
            lambda_factor = -1/(max_fdx)
        elif fdx(quation_num, a) * fdx(quation_num, b) < 0:
            lambda_factor = 1/(max_fdx)
            
        if abs(phi_dx(x, lambda_factor)) < 0.79:

            while True:
                x_prev = x
                x = phi(x, lambda_factor)
                iterations += 1

                if abs(x - x_prev) < epsilon or abs(f(quation_num, x)) < epsilon:
                    break
                elif iterations > 100:
                    return "Convergence speed is too slow."
                            
            answer.append(x)
            answer.append(f(quation_num, x))
            answer.append(iterations)
            return answer
        else:
            return "The convergence condition is not met\nor the convergence rate is too slow." 
    else: 
        return "The system has several solutions \nor none at all."     
