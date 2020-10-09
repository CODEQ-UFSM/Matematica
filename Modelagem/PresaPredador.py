from numpy import *
import matplotlib.pyplot as p
from scipy import integrate

a = 1
b = 1
c = 1
d = 1
X0 = array([3, 2]) # Condições iniciais
t = linspace(0, 15,  1000) # Tempo da simulação

def dX_dt(X, t = 0):
    u = X[0]
    v = X[1]
    return array([a*u - b*u*v, d*u*v - c*v])

X, infodict = integrate.odeint(dX_dt, X0, t, full_output=True)

rabbits, foxes = X.T

f1 = p.figure()
p.plot(t, rabbits, 'r-', label='Coelhos')
p.plot(t, foxes  , 'b-', label='Raposas')
p.grid()
p.legend(loc='best')
p.xlabel('Tempo')
p.ylabel('População')
p.title('População x Tempo')


f2 = p.figure()

X = integrate.odeint(dX_dt, X0, t)
p.plot( X[:, 0], X[:, 1], lw=2, color='black', label='X0=(%.f, %.f)' % ( X0[0], X0[1]))

ymax = p.ylim(ymin=0)[1]
xmax = p.xlim(xmin=0)[1]
nb_points   = 20

x = linspace(0, xmax, nb_points)
y = linspace(0, ymax, nb_points)

X1 , Y1  = meshgrid(x, y)
DX1, DY1 = dX_dt([X1, Y1])
M = (hypot(DX1, DY1))
M[ M == 0] = 1.
DX1 /= M
DY1 /= M

p.title('Espaço de Fase')
Q = p.quiver(X1, Y1, DX1, DY1, M, pivot='mid', cmap=p.cm.jet)
p.xlabel('Qtd. Coelhos')
p.ylabel('Qtd. Raposas')
p.legend()
p.grid()
p.xlim(0, xmax)
p.ylim(0, ymax)

p.show()
