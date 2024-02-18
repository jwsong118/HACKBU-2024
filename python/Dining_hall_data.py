import random

def data_generator_of_days(n=7):
    list_of_outputs = []
    f = open("dining_halldaypercentage.txt")
    lines = f.read()
    list = lines.splitlines()
    f.close()
    if len(list)<=1:
        for i in range(n):
            list_of_outputs.append(random.randint(50,85))
    else:
        for i in range(n):
            list_of_outputs.append((random.randint(50,85)+float(list[i]))/2)
    with open("dining_halldaypercentage.txt","w") as output:
        for row in list_of_outputs:
            output.write(str(row) + "\n")
    
    return list_of_outputs

def data_generator_of_times(n=24):
    list_of_outputs = []
    f = open("dining_halltimepercentage.txt")
    lines = f.read()
    list = lines.splitlines()
    f.close()
    if len(list)<=1:
        for i in range(n):
            list_of_outputs.append(random.randint(10,20))
        list_of_outputs[12]= random.randint(20,30)
        list_of_outputs[18]= random.randint(20,30)
        for i in range(7):
            list_of_outputs[i]=0
        for i in range(21,24):
            list_of_outputs[i]=0
    else:
        for i in range(n):
            list_of_outputs.append((random.randint(10,20)+float(list[i]))/2)
        list_of_outputs[12]= (random.randint(20,30)+float(list[12]))/2
        list_of_outputs[18]= (random.randint(20,30)+float(list[18]))/2
        for i in range(7):
            list_of_outputs[i]=0
        for i in range(21,24):
            list_of_outputs[i]=0
    with open("dining_halltimepercentage.txt","w") as output:
        for row in list_of_outputs:
            output.write(str(row) + "\n")
    
    return list_of_outputs
    
    