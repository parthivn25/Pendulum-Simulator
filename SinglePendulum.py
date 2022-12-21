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
    dydt = [omega, - (g / l) * math.sin(theta)]
    return dydt


# give initial conditions for pendulum, theta given in degrees
theta_naught, omega_naught = 60, 0

# create an array of times for the process, followed by initial conditions
intervals = 100
t = math.linspace(0, 10, intervals)
y_naught = math.array([theta_naught*math.pi/180, omega_naught])

# create vector array y with theta and omega for at any time
solution = odeint(derivative, y_naught, t, args=(l, m))
x = []
y = []

# change to cartesian coordinates
for i in range(intervals):
    x.append(l * math.sin(solution[i][0]))
    y.append(-l * math.cos(solution[i][0]))

ax = plt.figure().add_subplot(projection='3d')
plt.plot(x, y, t)
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Time')
plt.xticks(range(-2, 3))
plt.yticks(range(-2, 3))
plt.title("Pendulum Position as a Parametric Equation of Time")
plt.show(block=True)
plt.interactive(False)
plt.show
