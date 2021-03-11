# def check_speed():
#     if speed<=70:
#         print("ok")
#     else:
#         speed1=(speed-70)//5
#         if speed1<=12:
#             print(speed1,"point")
#         else:
#             print("license suspended")
# speed=int(input("enter speed"))
# check_speed()

# print 1 to 20  number in list with square
# def poly():
#     i=1
#     l=[]
#     while i<=20:
#         a=i,i**2
#         l.append(a)
#         i+=1
#         print(a)
# poly()

# print salary par student
# def employee(name,salary=2000):
#     print(name,"your salary is:-",salary)
# employee("kartik",30000)
# employee("deepak")

# print area and perimeter of rectangle
# def area_rectangle(a,b):
#     print(a*b)
# def perimeter_rectangle(a,b):
#     print(2*(a+b))
# area_rectangle(4,6)
# perimeter_rectangle(5,6)

# print sum of digit sum_of digit
# def sum_of_digit(number):
#     sum=0
#     modulus=0
#     while number>0:
#         modulus=number%10
#         sum+=modulus
#         number//=10
#     return sum
# print(sum_of_digit(163))

# student ka kharcha

def student_budget(* number_of_student):
    i=0
    s=0
    budget=int(input("enter budget"))
    while i<len(number_of_student):
        print("student ka kharcha",budget)
        s+=budget
        i+=1
    if s<50000:
        print("budget ke andar hai")
    else:
        print("budget ke bahar hai")
student_budget("sudha","radhika","seema","kiran")
    















