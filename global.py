# a=30
# def show():
#     x=10
#     print(x)
#     print(a)
# show()
# print("global veriable",a)
 
#  local veriable:-local is used the inside the function not outside the function if we print outside the function then it show name error
# global veriable:- global veriable is decleared above a function it become globle veriable these veriable available all the function which are written after 
# it.

# i=1
# def my_fun():
#     i=3
#     i=i+1
#     print("my function",i)
# my_fun()

def disp(a,b):
    def show(x,y):
        sum=x+y
        print(sum)
    sum=a+b
    print(sum)
    show(2,3)
disp(4,5)