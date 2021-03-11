def check_harsad(range1,range2):
    for i in range(range1,range2+1):
        num2=i
        num=i
        sum=0
        while num!=0:
            rem=num%10
            num=int(num/10)
            sum=sum+rem
        if(num2%sum==0):
            print(i,end=" ")
range1=int(input("enter first range"))
range2=int(input("enter second range"))
check_harsad(range1,range2)

