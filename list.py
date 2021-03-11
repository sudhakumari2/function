name=["sudha",2,4.5]
a=[]
i=0
while i<len(name):
    if (type(name[i]))==str:
        a.append(type(name[i]))
    elif (type(name[i]))==int:
        a.append(name[i]*name[i])
    elif (type(name[i]))==float:
        a.append(type(name[i]))
    i+=1
print(a)


# name=["sudha","seema","sunita","sushila","kiran","anil","radhika"]
# i=0
# n=input("enter any letter")
# while i<len(name):
#     if name[i][0]==n:
#         print(name[i])
#     i+=1

    


