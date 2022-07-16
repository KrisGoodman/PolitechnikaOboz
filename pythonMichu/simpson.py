import math

def simpson(func, a, b, n):


    
    H = (b - a)/(6*n)


    
    pole =0
    
    for k in range(n):
        
        
        temp = (H/6)*(lambda x: 5(x-1) + 4*(lambda x: 5(x-1 + H/2)) + (lambda x: 5(x)))

        pole += temp
    
    
    return pole

print(simpson(0, math.pi, 1000))
