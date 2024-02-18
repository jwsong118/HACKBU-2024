import matplotlib.pyplot as plt
from Graph import graph
from Gym_data import data_generator_of_times
from Minvalue import minvalue
import numpy as np

def gym_monday(m=1.2):
    x_pos = ["00:00","01:00","02:00","03:00","04:00","05:00","06:00","07:00","08:00","09:00","10:00","11:00","12:00","13:00","14:00","15:00","16:00","17:00","18:00","19:00","20:00","21:00","22:00","23:00"]
    data_of_people = data_generator_of_times(n=24)

    for i in range(24):
        if data_of_people[i] == minvalue(percentage = data_of_people):
            x_min = x_pos[i]
            print("The best time to go is "+ str(x_min)+" because it will be filled by the lowest percentage")
    graph(figwidth = 15, x_pos = x_pos, x = [a for a in range(24)], y = data_of_people, graph_title= "day graph")
    plt.show()

def gym_tuesday(m=1.2):
    x_pos = ["00:00","01:00","02:00","03:00","04:00","05:00","06:00","07:00","08:00","09:00","10:00","11:00","12:00","13:00","14:00","15:00","16:00","17:00","18:00","19:00","20:00","21:00","22:00","23:00"]
    data_of_people = data_generator_of_times(n=24)

    for i in range(24):
        if data_of_people[i] == minvalue(percentage = data_of_people):
            x_min = x_pos[i]
            print("The best time to go is "+ str(x_min)+" because it will be filled by the lowest percentage")
    graph(figwidth = 15, x_pos = x_pos, x = [a for a in range(24)], y = data_of_people, graph_title= "day graph")
    plt.show()

def gym_wednesday(m=1.2):
    x_pos = ["00:00","01:00","02:00","03:00","04:00","05:00","06:00","07:00","08:00","09:00","10:00","11:00","12:00","13:00","14:00","15:00","16:00","17:00","18:00","19:00","20:00","21:00","22:00","23:00"]
    data_of_people = data_generator_of_times(n=24)

    for i in range(24):
        if data_of_people[i] == minvalue(percentage = data_of_people):
            x_min = x_pos[i]
            print("The best time to go is "+ str(x_min)+" because it will be filled by the lowest percentage")
    graph(figwidth = 15, x_pos = x_pos, x = [a for a in range(24)], y = data_of_people, graph_title= "day graph")
    plt.show()
    
def gym_thursday(m=1.2):
    x_pos = ["00:00","01:00","02:00","03:00","04:00","05:00","06:00","07:00","08:00","09:00","10:00","11:00","12:00","13:00","14:00","15:00","16:00","17:00","18:00","19:00","20:00","21:00","22:00","23:00"]
    data_of_people = data_generator_of_times(n=24)

    for i in range(24):
        if data_of_people[i] == minvalue(percentage = data_of_people):
            x_min = x_pos[i]
            print("The best time to go is "+ str(x_min)+" because it will be filled by the lowest percentage")
    graph(figwidth = 15, x_pos = x_pos, x = [a for a in range(24)], y = data_of_people, graph_title= "day graph")
    plt.show()

def gym_friday():
    x_pos = ["00:00","01:00","02:00","03:00","04:00","05:00","06:00","07:00","08:00","09:00","10:00","11:00","12:00","13:00","14:00","15:00","16:00","17:00","18:00","19:00","20:00","21:00","22:00","23:00"]
    data_of_people = data_generator_of_times(n=24)

    for i in range(24):
        if data_of_people[i] == minvalue(percentage = data_of_people):
            x_min = x_pos[i]
            print("The best time to go is "+ str(x_min)+" because it will be filled by the lowest percentage")
    graph(figwidth = 15, x_pos = x_pos, x = [a for a in range(24)], y = data_of_people, graph_title= "day graph")
    plt.show()
    
def gym_saturday():
    x_pos = ["00:00","01:00","02:00","03:00","04:00","05:00","06:00","07:00","08:00","09:00","10:00","11:00","12:00","13:00","14:00","15:00","16:00","17:00","18:00","19:00","20:00","21:00","22:00","23:00"]
    data_of_people = data_generator_of_times(n=24)

    for i in range(24):
        if data_of_people[i] == minvalue(percentage = data_of_people):
            x_min = x_pos[i]
            print("The best time to go is "+ str(x_min)+" because it will be filled by the lowest percentage")
    graph(figwidth = 15, x_pos = x_pos, x = [a for a in range(24)], y = data_of_people, graph_title= "day graph")
    plt.show()

def gym_sunday():
    x_pos = ["00:00","01:00","02:00","03:00","04:00","05:00","06:00","07:00","08:00","09:00","10:00","11:00","12:00","13:00","14:00","15:00","16:00","17:00","18:00","19:00","20:00","21:00","22:00","23:00"]
    data_of_people = data_generator_of_times(n=24)

    for i in range(24):
        if data_of_people[i] == minvalue(percentage = data_of_people):
            x_min = x_pos[i]
            print("The best time to go is "+ str(x_min)+" because it will be filled by the lowest percentage")
    graph(figwidth = 15, x_pos = x_pos, x = [a for a in range(24)], y = data_of_people, graph_title= "day graph")
    plt.show()