print("welcome to pnb atn")
print("insert your card")
print("select your pin")
language=input("enter any language,english,hindi")
if language=="english":
    pin=int(input("enter your four digit pin"))
    if pin==1234:
        Transction=("choose your any Trcnsction,withdrawl,change_pin,balace_enquiry")
        if Transction=="withdrawl":
            amount=int(input("enter amount"))
            if amount>0:
                print("collect your cash")
            else:
                print("enter valid amount")
        elif Transction=="balance_enquiry":
            sleep=input("do you want sleep,y,n")
            if sleep=="y":
                print("your sleep")
            else:
                print("thanks for using")
        elif Transction=="change_pin":
            change_pin=int(input("enter pin"))
            if change_pin==4444:
                print("your pin has been sucessfully")
            else:
                print("enter right pin")
        else:
            print("nothing")
    else:
        print("enter valid pin")
else:
    print("thanks")

