import numpy as math
import imageio
from scipy.integrate import odeint
import matplotlib.pyplot as plt
from PIL import Image

# work in standard units of meters, seconds, and radians

l = 1
m = 1
g = 9.81


# initialize length and mass of pendulum
# Lagrangian is given as T-V = 1/2m(l^2)(omega)^2 - mglcos(theta)
# Solving Euler-Lagrange, we get ml^2alpha = mglsin(theta), or alpha = gsin(theta)/l

def derivative(y, t, l, m):
    theta1, omega1, theta2, omega2 = y
    # insert derivative as defined by Euler-Lagrange
    cosdif = math.cos(theta1 - theta2)
    sindif = math.sin(theta1 - theta2)
    alpha1 = (g * math.sin(theta2) * cosdif - sindif * (omega1 ** 2 * cosdif + omega2 ** 2) - (2) * g * math.sin(
        theta1)) / (1 + sindif ** 2)
    alpha2 = ((2) * (omega1 ** 2 * sindif - g * math.sin(theta2) + g * math.sin(
        theta1) * cosdif) + omega2 ** 2 * sindif * cosdif) / (1 + sindif ** 2)
    dydt = [omega1, alpha1 - 0.5 * omega1, omega2, alpha2 - 0.5 * omega2]
    return dydt


# give initial conditions for pendulum, theta given in degrees
theta1_naught, omega1_naught, theta2_naught, omega2_naught = 45, 0, 60, 8

# create an array of times for the process, followed by initial conditions
seconds = 20
intervals = seconds*10

t = math.linspace(0, seconds, intervals)
y_naught = math.array([theta1_naught * math.pi / 180, omega1_naught, theta2_naught * math.pi / 180, omega2_naught])

# create vector array y with theta and omega for at any time
solution = odeint(derivative, y_naught, t, args=(l, m))
x1 = []
y1 = []
x2 = []
y2 = []

# change to cartesian coordinates
for i in range(intervals):
    x1.append(l * math.sin(solution[i][0]))
    y1.append(-l * math.cos(solution[i][0]))
    x2.append(l * math.sin(solution[i][0]) + l * math.sin(solution[i][2]))
    y2.append(-l * math.cos(solution[i][0]) - l * math.cos(solution[i][2]))


# function creates frames at each portion of time
def create_frame(r):
    # plot the pendulum and the bar connecting to the origin
    plt.plot(x1[r], y1[r], marker="o", markersize=7, markeredgecolor="red", markerfacecolor="black")
    plt.plot([x1[r], 0], [y1[r], 0], 'k-')
    plt.plot(x2[r], y2[r], marker="o", markersize=7, markeredgecolor="red", markerfacecolor="black")
    plt.plot([x2[r], x1[r]], [y2[r], y1[r]], 'k-')
    # add axis preferences and titles to graph
    plt.xlim([-2.5, 2.5])
    plt.ylim([-2.5, 2.5])
    plt.xticks([])
    plt.yticks([])
    seconddisplay = (r / intervals) * seconds
    seconddisplay = round(seconddisplay, 2)
    plt.title(f'Pendulum position at {seconddisplay} seconds')
    plt.savefig(f'img_{r}.png')
    plt.close()


# calls function for frames, creating at different times throughout motion
for r in range(intervals):
    create_frame(r)
frames = []
# appends all frames into an array and uses imageio to make it into a gif
for r in range(intervals):
    image = imageio.v2.imread(f'img_{r}.png')
    frames.append(image)
# resultant gif is saved

imageio.mimsave('./example.gif', frames, fps=15)
a = Image.open("./example.gif")
a.show()
