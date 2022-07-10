def f(x,y):
    return x+y


#  LUB f = lambda x: x+y

# Euler
def euler(x0,y0,xn,n):
    
    # krok
    h = (xn-x0)/n

    print('\n-----------Rozw-----------')
    print('------------------------------')    
    print('x0\ty0\tslope\tyn')
    print('------------------------------')
    for i in range(n):
        slope = f(x0, y0)
        yn = y0 + h * slope
        print('%.4f\t%.4f\t%0.4f\t%.4f'% (x0,y0,slope,yn) )
        print('------------------------------')
        y0 = yn
        x0 = x0+h
    
    print('\nAt x=%.4f, y=%.4f' %(xn,yn))
    

# wejscie
print('Dane:')
x0 = float(input('x0 = '))
y0 = float(input('y0 = '))

print('punkt: ')
xn = float(input('xn = '))

print('liczba krokow:')
step = int(input('liczba krokow = '))

# wywyolanie
euler(x0,y0,xn,step)