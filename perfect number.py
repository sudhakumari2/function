# def ek_perfect(num):
#     i=1
#     s=0
#     while i<num:
#         if num%i==0:
#             s=s+i
#         i+=1
#     if num==s:
#         print("perfect number hai",num)
#     else:
#         print("perfect number nhi hai",num)
# num=int(input("enter any number"))
# ek_perfect(num)

#perfect number 1 to 100
def perfect():
    i=0
    while i<=100:
        j=1
        s=0
        while j<i:
            if i%j==0:
                s=s+j
            j+=1
        if s==i:
            print("perfect number hai",i)
        else:
            print("perfect number nhi h",i)
        i+=1
perfect()



