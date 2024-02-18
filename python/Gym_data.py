import random

def data_generator_of_days(n=7):
    list_of_outputs = []
    f = open("gymdaypercentage.txt")
    lines = f.read()
    list = lines.splitlines()
    f.close()
    if len(list)<=1:
        for i in range(n):
            list_of_outputs.append(random.randint(30,60))
        list_of_outputs[4]= random.randint(20,40)
        list_of_outputs[5]= random.randint(20,40)
        list_of_outputs[6]= random.randint(20,40)
    else:
        for i in range(n):
            list_of_outputs.append((random.randint(30,60)+float(list[i]))/2)
        list_of_outputs[4]= (random.randint(20,40)+float(list[4]))/2
        list_of_outputs[5]= (random.randint(20,40)+float(list[5]))/2
        list_of_outputs[6]= (random.randint(20,40)+float(list[6]))/2
    with open("gymdaypercentage.txt","w") as output:
        for row in list_of_outputs:
            output.write(str(row) + "\n")
    return list_of_outputs

def data_generator_of_times(n=24,m=1):
    list_of_outputs = []
    f = open("gymtimepercentage.txt")
    lines = f.read()
    list = lines.splitlines()
    f.close()
    if len(list)<=1:
        for i in range(n):
            list_of_outputs.append(random.randint(20,30)*m)
        for i in range(16,19):
            list_of_outputs[i]=random.randint(60,80)*m
        for i in range(5):
            list_of_outputs[i]=0
        for i in range(23,24):
            list_of_outputs[i]=0
    else:
        for i in range(n):
            list_of_outputs.append((random.randint(20,30)*m+float(list[i]))/2)
        for i in range(16,19):
            list_of_outputs[i]=(random.randint(60,80)*m+float(list[i]))/2
        for i in range(5):
            list_of_outputs[i]=0
        for i in range(23,24):
            list_of_outputs[i]=0
    with open("gymtimepercentage.txt","w") as output:
        for row in list_of_outputs:
            output.write(str(row) + "\n")
 
    return list_of_outputs
