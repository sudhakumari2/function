def unique_number(numbers):
    i=0
    a=[]
    while i<len(numbers):
        if numbers[i] not in a:
            a.append(numbers[i])
        i+=1
    print(a)
unique_number(numbers=[1,2,3,3,3,3,4,5])


