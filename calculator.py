def calculator(a,operation,b):
	if operation=='+':
		c=(a+b)
	elif operation=='-':
		c=(a-b)
	elif operation=='*':
		c=(a*b)
	elif operation=='/':
		c=(a/b)
	else:
		print('nothing')
	return c
print(calculator(4,'+',6))	
Calculator in function