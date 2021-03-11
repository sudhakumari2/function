def atm():
    print("wecome to the ICICI ","\U0001f600")
    language=int(input("enter a language = "))
    if language==1:
        print("Hindi")
    elif language==2:
        print("English")
atm()
def pin():
    chances=0
    while chances<3:
        pin=int(input("enter the pin"))
        if pin==1234:
            print("your pin is corrected")
            balance=20000
            print('please press 1 for your balance')
            print('please press 2 for your withdrawl')
            print('please press 3 for your pay in')
            print('please press 4 for your return card')
            option=int(input('what would you like to choose'))
            if option==1:
                print('your balance is $',balance)
            elif option==2:
                withdrawl=float(input('how much would you like to withdraw amount?'))
                if withdrawl in [100,200,300,400,600,800,1000]:
                    balance=balance -withdrawl
                    print('your balance is now $ ',balance)
            elif option==3:
                pay_in=float(input('how much would you like to pay in ?:'))
                balance = balance +pay_in
                print('your balance is now $',balance)
            elif option==4:
                print('please wait while card is returned ....')
                print('thank you for banking with ICICI ')
        else: 
            print("inviled try again")
            chances+=1
        
    print("you don't have any chance")
pin()