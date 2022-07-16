import math
def calka(my_func, a, b, n):
  
  delta_x = (b-a)/n
  
  total = 0  
  for i in range(n):
    x = a + delta_x * i
    total += delta_x * (my_func(x) + my_func(x + delta_x)) / 2
  return total



input 
integral = calka(lambda x: math.sin(x), 0.0, math.pi, 1000)

print(integral)
