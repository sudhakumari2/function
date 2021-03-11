marks = [[45, 21, 42, 63], [12, 42, 42, 53], [42, 90, 78, 13], [94, 89, 78, 76], [87, 55, 98, 99]] 
max=0
i=0
sub_marks=[]
while i<len(marks):
    j=0
    while j<len(marks[i]):
        sub_marks.append(marks[i][j])
        j+=1
    i+=1
index=0
while index<len(sub_marks):
    if sub_marks[index]>max:
        max=sub_marks[index]
    i+=1
print(max)

def max_marks(marks):
    max=0
    i=0
    sub_marks=[]
    while i<len(marks):
        j=0
        while j<len(marks[i]):
            sub_marks.append(marks[i][j])
            j+=1
        i+=1
    index=0
    while index<len(sub_marks):
        if sub_marks[index]>max:
            max=sub_marks[index]
        index+=1
    print(max)
max_marks(marks = [[45, 21, 42, 63], [12, 42, 42, 53], [42, 90, 78, 13], [94, 89, 78, 76], [87, 55, 98, 99]] 
) 