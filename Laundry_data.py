import random

def data_generator_of_days(n=7):
    list_of_outputs = []
    for i in range(n):
        list_of_outputs.append(random.randint(20,40))
    list_of_outputs[4]= random.randint(30,50)
    list_of_outputs[5]= random.randint(40,60) 
    list_of_outputs[6]= random.randint(40,60) 
    return list_of_outputs

def data_generator_of_times(n=24, m=1):
    list_of_outputs = []
    for i in range(n):
        list_of_outputs.append(random.randint(10,20)*m)
    for i in range(17,21):
        list_of_outputs[i]=random.randint(30,40)*m
    for i in range(0,6):
        list_of_outputs[i]=0
    
    return list_of_outputs