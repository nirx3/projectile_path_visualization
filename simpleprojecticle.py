#path of a  projectile with ni animation

import matplotlib.pyplot as plt
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
max_x = max(horizontal_position) + 2.5
max_y = max(vertical_position) + 2.5
plt.plot(horizontal_position,vertical_position, color="Cadetblue", label="Path of a projectile")
plt.grid(True)
plt.scatter(horizontal_position[0], vertical_position[0], color='green', label='Launch',s=25)
plt.scatter(horizontal_position[-1], vertical_position[-1], color='red', label='Landing', s=25)
plt.xlim(0, max_x)
plt.ylim(0, max_y)
plt.annotate(f"Max height: {max(vertical_position):.2f} m",
             xy=(horizontal_position[vertical_position.index(max(vertical_position))],
                 max(vertical_position)),
             xytext=(10, max(vertical_position)+1),
             arrowprops=dict(facecolor='black', arrowstyle='->'))
plt.ylabel("Height")
plt.xlabel("Distance")
plt.title("Motion of projectile")
plt.legend()
plt.show()

