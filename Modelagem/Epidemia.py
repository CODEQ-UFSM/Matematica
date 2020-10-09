from numpy import *
import matplotlib.pyplot as p
from scipy import integrate

a = 1.32
b = 0.23
t = linspace(0, 25, 1000)
inicial = array([0.99, 0.01, 0])

def EDO(var, t = 0):
    S = var[0]
    I = var[1]
    R = var[2]

    dS_dt = -a * S * I
    dI_dt = a * S * I - b * I
    dR_dt = b * I

    return array([dS_dt, dI_dt, dR_dt])

X, infodict = integrate.odeint(EDO, inicial, t, full_output=True)
S_t = X[:, 0]
I_t = X[:, 1]
R_t = X[:, 2]

f1 = p.figure()
p.plot(t, S_t, 'b-', label='Suscetíveis')
p.plot(t, I_t, 'r-', label='Infectados')
p.plot(t, R_t, 'g-', label='Recuperados/Mortos')
p.grid()
p.legend(loc='best')
p.xlabel('Tempo')
p.ylabel('População')
p.title('População x Tempo')
f1.savefig('epidemia.png')

p.show()

