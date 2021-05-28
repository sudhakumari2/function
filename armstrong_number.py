def Armstrong_number(num):
    i=num
    sum=0
    count=len(str(num))
    while i>0:
        rem=i%10
        sum=sum+rem**count
        i=i//10
    if sum==num:
        print("armstrong number hai",num)
    else:
        print("armstromg number nhi h",num)
num=int(input("enter any number"))
Armstrong_number(num)


