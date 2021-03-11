# def max_number():
#     if num1==num2 and num2==num3:
#         print("all are equal")
#     elif num1>=num2 and num1>=num3:
#         print("num1 is maximum",num1)
#     elif num2>=num1 and num2>=num3:
#         print("num2 is maximum",num2)
#     elif num3>=num1 and num3>=num2:
#         print("third is maximum",num3)
#     else:
#         print("nothing")
# num1=int(input("enter first number"))
# num2=int(input("enter second number"))
# num3=int(input("enter third number"))
# max_number()
# 
# factorial_of_number
def factorial_of_number():
    i=1
    a=1
    num=int(input("enter the number"))
    while i<num:
        a=a*num
        num-=1
    print(a,"that is factorial")
factorial_of_number()

