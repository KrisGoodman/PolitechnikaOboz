import ipywidgets as widgets, matplotlib.pyplot as plt, time
from numpy import zeros, linspace, pi, cos, array


def oscylator(a):

    t0= time.time()
    omega = 2
    P = 2*pi/omega
    dt = P/a
    T = 10*P
    liczbaInterwalow = int(round(T/dt))

    #Naniesienie jednostki na oś poziomą
    osPozioma = linspace(0, liczbaInterwalow*dt, liczbaInterwalow+1)

    u = zeros(liczbaInterwalow+1)
    v = zeros(liczbaInterwalow+1)

    # warunki poczatkowe
    X_0 = 1
    u[0] = X_0
    v[0] = 0

    # kolejne kroki metoda Eulera
    for n in range(liczbaInterwalow):
        u[n+1] = u[n] + dt*v[n]
        v[n+1] = v[n] - dt*omega**2*u[n]
    t1 = time.time() - t0
    czas.append(t1)

czas = []
podzial = []
for i in range(1000):
    oscylator(i + 1)
    podzial.append(i + 1)
print(czas)
print(podzial)