print("welcome")
def select_language():
    language=input("enter language,hindi,english")
    if language=="english":
        return language
def select_pin():
    pin=int(input("enter any four digit pin"))
    if pin==1234:
        return("your pin is correct")
    else:
        return("invalid pin try again")
    
def showing_transction():
    transction=input("enter any transction,withdrawl,balance_enquiry,pin_change")
    return transction
    if transction=="withdraw":
        amount=int(input("enter amount")):
        if amount>0:
            print("collect your cash")
        else:
            print("enter vsalid amount")
    if transction()=="balance_enquiry":
        sleep=input("do you want sleep,y,n")
        if sleep=="y":
            print("your balance")
        else:
            print("your pin is wrong")
    if transction()=="pin_change":
        change_pin=int(input("enter pin"))
        if change_pin==2222:
            print("your pin is sucessfully")
        else:
            print("enter again")
print(select_language(english))
print(select_pin(1234))
print(showing_transction(withdrawl))
    
            
    
                
        
