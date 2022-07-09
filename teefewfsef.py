import math

def simpson(my_func, a, b, n):
    delta_x = (b-a)/n
    total = 0
    for i in range(0, n, 2):
        x = a + delta_x * 2 * i
        total += delta_x * (my_func(x) + 4 * my_func(x+ delta_x) + my_func(x + 2 * delta_x)) /3
    return total

print(simpson(lambda x: math.e**-(x**2), 0.0, 1.0, 100))
