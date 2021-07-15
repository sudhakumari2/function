def add(numbers):
    i=0
    sum=0
    while i<len(numbers):
        sum=sum+numbers[i]
        i+=1
    return sum
print(add(numbers=[8, 2, 3, 0, 7]))
