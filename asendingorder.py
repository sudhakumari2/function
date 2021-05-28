def asending_order(number):
    i=0
    while i<len(number):
        j=0
        while j<len(number)-1:
            if number[j]>number[j+1]:
                number[j],number[j+1]=number[j+1],number[j]
            j+=1
        i+=1
    print(number)
asending_order(number=[2,5,7,1,8])
