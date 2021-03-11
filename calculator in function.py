def calculator(num1,operation,num2):
    if operation=="+":
        add_result=num1+num2
        return(add_result)
    elif operation=="-":
        sub_result=num1-num2
        return(sub_result)
    elif operation=="*":
        mul_result=num1*num2
        return(mul_result)
    elif operation=="/":
        divresult=num1/num2
        return(div_result)
num1=int(input("enter the  first number"))
num2=int(input("enter thesecond number "))
operation=input("enter operation")
print(calculator(num1,operation,num2))
    
        
