def minvalue(percentage =[0,0,70,0]):
    non_zero_percentage = []
    i = 0
    while i < len(percentage):
        if percentage[i] != 0:
            non_zero_percentage.append(percentage[i])
        i = i + 1
    min = non_zero_percentage[0]   
    for n in range(len(non_zero_percentage)):
        if non_zero_percentage[n] <= min:
            min = non_zero_percentage[n]
    
    return min
