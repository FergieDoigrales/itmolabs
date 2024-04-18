import numpy as np
import validator

    
def simple_iteration_method(x0, y0, system, e) :
    if validator.check_epsilon(e) is False:
        return "Epsilon cannot be less than zero."
    if validator.check_range(x0, y0):
        return "The left border cannot \nbe larger than the right!" 
    max_iter = 1000
    iteration = 0
    answer = []
    if not check_convergence(system, x0, y0):
        return "The convergence condition is not met."
        
    for i in range(max_iter):
        x = f1(x0, y0, system)
        y = f2(x0, y0, system)
        if (abs(x - x0)< e)and(abs(y - y0)< e):
            answer.append(x)
            answer.append(y)
            answer.append(iteration)
            answer.append(x - f1(x,y,system)) #точность x
            answer.append(y - f2(x,y,system)) #точность y
            return answer
        x0, y0 = x, y
        iteration += 1
    return "The convergence condition is not met."
  

def f1(x,y,system):
    if(system == 1):
        return 0.3 - 0.1*x*x- 0.2*y*y
    elif(system == 2):
        return 3*y*y+0.5*x*x

    
def f2(x,y,system):
    if(system == 1):
        return 0.7 -0.2*x*x - 0.1*x*y
    elif(system == 2):
        return np.sin(x)**2

def check_convergence(system, x0, y0):
    jacobian_matrix = np.array([[f1_dx(system, x0, y0), f1_dy(system, x0, y0)], 
                                [f2_dx(system, x0, y0), f2_dy(system, x0, y0)]])
    eigenvalues = np.linalg.eigvals(jacobian_matrix)
    if np.all(np.abs(eigenvalues) < 1):
        return True
    else:
        return False

def f1_dx(system, x, y):
    if system == 1:
        return -0.2 * x
    elif system == 2:
        return x


def f1_dy(system, x, y):
    if system == 1:
        return -0.4 * y
    elif system == 2:
        return 6*y

def f2_dx(system, x, y):
    if system == 1:
        return -0.4 * x - 0.1 * y
    elif system == 2:
        return np.sin(2*x)

def f2_dy(system, x, y):
    if system == 1:
        return 0
    elif system == 2:
        return 0


print(simple_iteration_method(0, 1, 1, 0.001))