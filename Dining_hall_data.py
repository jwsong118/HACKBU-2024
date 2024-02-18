import random

def data_generator_of_days(n=7):
    list_of_outputs = []
    for i in range(n):
        list_of_outputs.append(random.randint(50,85))
    
    return list_of_outputs

def data_generator_of_times(n=24):
    list_of_outputs = []
    for i in range(24):
        list_of_outputs.append(random.randint(10,20))
    list_of_outputs[12]= random.randint(20,30)
    list_of_outputs[18]= random.randint(20,30)
    for i in range(7):
        list_of_outputs[i]=0
    for i in range(21,24):
        list_of_outputs[i]=0
    
    return list_of_outputs
    
    