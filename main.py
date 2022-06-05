import math

def func(p, a):
    sum = 0
    p.reverse()
    for i in range(len(p)):
        sum += p[i] * pow(a, i)
    p.reverse()
    return sum

def dfunc(p, a):
    dp = []
    p.reverse()
    for i in range(len(p)):
        coef = p[i] * i
        if (coef != 0):
            dp.append(coef)
    sum = 0
    for i in range(len(dp)):
        sum += dp[i] * pow(a, i)
    p.reverse()
    return sum

def bisection(a, b, p, epsilon):
    k = 0
    while abs(a - b) >= epsilon:
        k += 1
        c = (a + b) / 2
        if func(p, a) * func(p, c) <= 0.0:
            b = c
        else:
            a = c
        #print('a:', a, ' | b: ', b)
    return ((a + b) / 2, k)

def chord(a, b, p, epsilon):
    k = 0
    while True:
        k += 1
        c = ( (a * func(p, b)) - (b * func(p, a))) / (func(p, b) - func(p, a))
        if func(p, a) * func(p, c) <= 0.0:
            b = c
        else:
            a = c
        #print('a:', a, ' | b: ', b)
        if abs( func(p, c)) < epsilon:
            return c, k
        
def newton(a, b, p, epsilon):
    x = b
    k = 0
    while abs(func(p ,x)) >= epsilon:
        k += 1
        x -= func(p, x) / dfunc(p, x)
        if func(p, a) * func(p, x) <= 0.0:
            b = x
        else:
            a = x
        #print('a:', a, ' | b: ', b)
    return x, k

def calculate(intervals, epsilon, p):
    for i in range(len(intervals)):
        print('X' + str( i + 1) + ':')
        
        a = bisection(intervals[i][0], intervals[i][1], p, epsilon)
        print(a[0])
        print('Метод бісекцій. Ітерацій:', a[1])
        
        b = chord(intervals[i][0], intervals[i][1], p, epsilon)
        print(b[0])
        print('Метод хорд. Ітерацій:', b[1])
        
        c = newton(intervals[i][0], intervals[i][1], p, epsilon)
        print(c[0])
        print('Метод Ньютона. Ітерацій:', c[1])

def main():
    epsilon = pow(10, -5)
    p = [2, -2, -4, 0, 2, 1]
    intervals = ((-2.4142, -0.3864), (0.3864, 1), (1,3))
    calculate(intervals, epsilon, p)

if __name__ == "__main__":
    main()