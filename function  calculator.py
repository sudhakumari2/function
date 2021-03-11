def calculator(num1,operation,num2):
    if operation=="+":
        add_result=num1+num2
        return add_result
    elif operation=="-":
        sub_result=num1-num2
        return sub_result
    elif operation=="*":
        multiply_result=num1*num2
        return multiply_result
    elif operation=="/":
        divide_result=num1/num2
        return divide_result
num1=int(input("enter any number"))
num2=int(input("enter amy number"))
operation=input("enter operation")
print(calculator(num1,operation,num2))