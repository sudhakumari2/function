# def exponent(base,exp):
#     a=base**exp
#     return a
# base=int(input("enter any base"))
# exp=int(input("enter exp"))
# print(exponent(base,exp))

# prime number

# def prime_number():
#     i=1
#     while i<=100:
#         j=2
#         c=0
#         while j<i:
#             if i%i==0:
#                 c+=1
#         if c==2:
#             print("prime no",i)
#         i+=1
# prime_number()

# def prime_number(num):
#     i=1
#     c=0
#     while i<=num:
#         if num%i==0:
#             c+=1
#         i+=1
#     if c==2:
#         print("prime ",num)
#     else:
#         print("not prime",num)
# num=int(input("enter any number"))
# prime_number(num)

def prime_number():
    i=1
    while i<100:
        j=1
        c=0
        while j<=i:
            if i%j==0:
                c+=1
            j+=1
        if c==2:
            print("prime",i)
        else:
            pass
        i+=1
prime_number()
            