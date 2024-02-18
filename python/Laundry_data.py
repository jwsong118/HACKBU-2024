import random

def data_generator_of_days(n=7):
    list_of_outputs = []
    f = open("laundrydaypercentage.txt")
    lines = f.read()
    list = lines.splitlines()
    f.close()
    if len(list)<=1:
        for i in range(n):
            list_of_outputs.append(random.randint(20,40))
        list_of_outputs[4]= random.randint(30,50)
        list_of_outputs[5]= random.randint(40,60) 
        list_of_outputs[6]= random.randint(40,60) 
    else:
        for i in range(n):
            list_of_outputs.append(random.randint(20,40)+float(list[i]))
        list_of_outputs[4]= (random.randint(30,50)+float(list[4]))/2
        list_of_outputs[5]= (random.randint(40,60)+float(list[5]))/2
        list_of_outputs[6]= (random.randint(40,60)+float(list[6]))/2
    with open("laundrydaypercentage.txt","w") as output:
        for row in list_of_outputs:
            output.write(str(row) + "\n")
        return list_of_outputs
        

def data_generator_of_times(n=24, m=1):
    list_of_outputs = []
    f = open("laundrytimepercentage.txt")
    lines = f.read()
    list = lines.splitlines()
    f.close()
    if len(list)<=1:
        for i in range(n):
            list_of_outputs.append(random.randint(10,20)*m)
        for i in range(17,21):
            list_of_outputs[i]=random.randint(30,40)*m
        for i in range(0,6):
            list_of_outputs[i]=0
    else:
        for i in range(n):
            list_of_outputs.append((random.randint(10,20)*m+float(list[i]))/2)
        for i in range(17,21):
            list_of_outputs[i]=(random.randint(30,40)*m+float(list[i]))/2
        for i in range(0,6):
            list_of_outputs[i]=0
    with open("laundrytimepercentage.txt","w") as output:
        for row in list_of_outputs:
            output.write(str(row) + "\n")
    
    return list_of_outputs