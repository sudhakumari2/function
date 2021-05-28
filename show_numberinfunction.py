def show_number(num):
	i=1
	while i<=num:
		if i%3==0 and i%5==0:
			print(i)
		i+=1
num=int(input('enter any number'))
show_number(num)