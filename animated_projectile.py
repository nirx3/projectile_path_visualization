#Version-1.0.0 : plotting graph with animation
#Version-1.0.1 : adding max height label dynamically



import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import numpy as np
import math 

initial_velocity=float(input("Enter initial velocity: "))
angle_of_launch_in_degree=float(input("Enter an angle of launch:"))
angle_of_launch_in_radian=math.radians(angle_of_launch_in_degree)
g=9.8065
t=0
horizontal_position=[]
vertical_position=[]
time_of_flight=(2*initial_velocity*math.sin(angle_of_launch_in_radian))/g
while t<=time_of_flight:
    horizontal_position.append(initial_velocity*math.cos(angle_of_launch_in_radian)*t)
    vertical_position.append((initial_velocity*math.sin(angle_of_launch_in_radian)*t)-(0.5*g*(t**2)))
    t+=0.0025

fig, axe = plt.subplots()
line, =axe.plot([],[],label="Path of a projectile")
axe.set_xlim(0, max(horizontal_position)+2.5)
axe.set_ylim(0, max(vertical_position)+10)

def update(frame):
    line.set_xdata(horizontal_position[:frame])
    line.set_ydata(vertical_position[:frame])
    if frame == (len(horizontal_position)/2)-1:
        plt.annotate(f"Max height: {max(vertical_position):.2f} m",
             xy=(horizontal_position[vertical_position.index(max(vertical_position))],
                 max(vertical_position)),
             xytext=(5, max(vertical_position)+2),
             arrowprops=dict(facecolor='black', arrowstyle='->'))
    return line
animation=FuncAnimation(fig=fig,func=update,frames=len(horizontal_position),interval=2, repeat=False)
plt.grid(True)
plt.title("Visual simulation of motion of a projectile")
plt.legend()
plt.show()






