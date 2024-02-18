import matplotlib.pyplot as plt
from Graph import graph
from Gym_data import data_generator_of_days
from Minvalue import minvalue
import numpy as np

x_pos = ['Monday','Tuesday','Wednesday','Thursday','Friday','Saturday','Sunday']
data_of_people = data_generator_of_days(n=7)
for i in range(7):
    if data_of_people[i] == minvalue(percentage = data_of_people):
        x_min = x_pos[i]
        print("The best day to go is "+ str(x_min)+" because it will be filled by the lowest percentage")
graph(y = data_of_people)
plt.savefig('week_graph_gym.png')
plt.show()
