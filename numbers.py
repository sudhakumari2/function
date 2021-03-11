# print between slash like sudha
# name = "http://www.navgurukul.org/sudha/1"
# a=(name.split("/"))
# print(a[3])

# print odd and even number
def even_number(num):
    if num%2==0:
        if num>2 and num<5:
            print("not weird one",num)
        elif num>5 and num<10:
            print("weird one ",num)
        elif num>10:
            print("not weird two",num)
    else:
        print("weird two",num)
num=int(input("enter any number"))
even_number(num)

