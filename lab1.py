import math
from sympy import *

def calc(x):	
    x1, x2, x3 = symbols('x1, x2, x3', real=True)

    a, b, c = x[0], x[1], x[2]

    funk = 3*x1**2 + 2*x2**2 + 4*x3**2 + 3*x1*x2 - 2*x2 - sin(x1-x3*x2)

    print("\n Варiант 3(23124414341241): ", funk , "\n")

    funk1 = diff(funk, x1)
    funk2 = diff(funk, x2)
    funk3 = diff(funk, x3)
    
    return funk1.evalf(subs={x1: a, x2: b, x3: c}), funk2.evalf(subs={x1: a, x2: b, x3: c}), funk3.evalf(subs={x1: a, x2: b, x3: c})

def delta(Am, n):
	if n == 1:
		return float((1/Am) * ((1/10)** (n-1)))	 
	else:
		return float((1/(2*Am)) * ((1/10) ** (n-1)))	

def findF(array): 	
    x1 = float(array[0])
    x2 = float(array[1])
    x3 = float(array[2])
    F = 5*(math.pow(x1, 2)) + 4*(math.pow(x2, 2)) + 3*(math.pow(x3, 2)) - 5*x2*x3 - 3*x1 - simplify(sec(18*x2-x3))

    return F

def getNumber2(numb): 
    chars = ".,"
    for c in chars:
        numb = numb.replace(c, '')
    len_num = int(len(numb))
    numb = numb.replace('0','')
    first_num = int(numb[0])
    return first_num, len_num

if __name__ == "__main__":
    num_massive = []
    delta_num = []
    res_num = [0, 0, 0]
    math_massive = []

    for i in range(3):
        num_massive.append(input(" Введіть ваше значення: "))

    print('Введені числа: ', num_massive, '\n')

    for i in range(3):
        res = getNumber2(num_massive[i]) 
        delta_num.append(delta(res[0], res[1])) 
        print(f'Delta: перша цифра: {res[0]} кількість цифр: {res[1]} \n')


    delta_num = [3*10**-3]*3
    
    for i in range(3):
        res_num[i] = delta_num[i] * float(num_massive[i]) 

    print(res_num, '\n')

    math_massive = calc(num_massive) 
    print(math_massive, '\n') 

    delta_F = 0
    for i in range(3):
        delta_F += math_massive[i] * res_num[i] 

    fx1x2x3 = findF(num_massive) 
    print(fx1x2x3, '\n')
    print(" Виконав студент групи КНМС - 41 Штойка Максим; ""\n")
    print(" Абсолютна похибка: F = ", delta_F, "\n")
    print(" Вiдностна похибка: F = ", str(delta_F/fx1x2x3))
