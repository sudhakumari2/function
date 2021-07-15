def show_length(st1,st2):
    a=len(st1)
    b=len(st2)
    if a>b:
        print(st1)
    elif b>a:
        print(st2)
st1=input("enter any first sentence")
st2=input("enter any second sentence")
show_length(st1, st2)