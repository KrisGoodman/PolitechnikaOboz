import math
def simpson(my_func, a, b, n):
    delta_x = (b-a)/n
    total = 0
    for i in range(1, n+1):
        x = a + delta_x * (i-1)
        total += delta_x * (my_func(x) + 4 * my_func(x+ (delta_x)/2) + my_func(x + delta_x)) /6
    return total

print(simpson(lambda x: math.e**-(x**2), 0.0, 1.0, 100))