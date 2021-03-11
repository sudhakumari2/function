def add_numbers_list(a,b):
    i=0
    while i<len(a):
        j=0
        while j<len(b):
            if i==j:
                c=a[i]+b[j]
                print(c)
            j+=1
        i+=1
add_numbers_list([50,60,10],[10,20,13])
#add_number_list
#check dono list ki same index number even hai ya nhi

def check_numbers(a,b):
    i=0
    while i<len(a):
        j=0
        while j<len(b):
            if i==j:
                if a[i]%2==0 and b[j]%2==0:
                    print("dono even h")
                else:
                    print("dono even nhi h")
            j+=1
        i+=1
check_numbers([2,6,18,3,75],[6,19,24,12,3,87])


