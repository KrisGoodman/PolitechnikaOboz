import math

def calkaTrapez(func, a, b, n): #chyba 
  delta_x = (b-a)/n
  total = 0
  for i in range(n):
    x = a + delta_x * i
    total += delta_x * (func(x) + func(x + delta_x)) / 2
  return total

def calkaProstokat(func, a, b, n):
  delta_x = (b - a)/n
  total = 0
  for i in range(n):
    x = a + i * delta_x
    total += delta_x * func(x)
  return total

print(calkaProstokat(lambda x: math.sin(x), 0.0, math.pi, 100))
print(calkaTrapez(lambda x: math.sin(x), 0.0, math.pi, 100))