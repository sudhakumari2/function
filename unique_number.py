def unique_num(list):
    i=0
    a=[]
    while i<len(list):
        if list[i] not in a:
            a.append(list[i])
        i+=1

    return a
print(unique_num(list= [1,2,3,3,3,3,4,5]))

