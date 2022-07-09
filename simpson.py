import math

def simpson(func, a, b, n):
    H = (b - a) / (6 * n)
    pole = 0
    for k in range(n):
        temp = (H/6) * (func(x - 1)) + 4 * (func(x - 1 + H/2)) + (func(x))
        pole += temp
    return pole

print(simpson(lambda x: math.sin(x), 0, math.pi, 1000))
