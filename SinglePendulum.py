import numpy as math
from scipy.integrate import odeint
import matplotlib.pyplot as plt

# work in standard units of meters, seconds, and radians

l = 1
m = 1
g = 9.81


# initialize length and mass of pendulum
# Lagrangian is given as T-V = 1/2m(l^2)(omega)^2 - mglcos(theta)
# Solving Euler-Lagrange, we get ml^2alpha = mglsin(theta), or alpha = gsin(theta)/l

def derivative(y, t, l, m):
    theta, omega = y
    # insert derivative as defined by Euler-Lagrange
    dydt = [omega, (g / l) * math.sin(theta)]
    return dydt


# give initial conditions for pendulum
theta_naught, omega_naught = 90, 0.001

# create an array of times for the process, followed by initial conditions
intervals = 1001
t = math.linspace(0, 10, intervals)
y_naught = math.array([theta_naught, omega_naught])

# create vector array y with theta and omega for at any time
solution = odeint(derivative, y_naught, t, args=(l, m))
x = []
y = []
# change to cartesian coordinates
for i in range(intervals):
    x.append(l * math.sin(solution[i][0]))
    y.append(l * math.cos(solution[i][0]))

ax = plt.figure().add_subplot(projection='3d')

plt.plot(x, y, t)
plt.xlabel('x label')
plt.ylabel('y label')

plt.title("test plot")


plt.show(block=True)
plt.interactive(False)

plt.show
