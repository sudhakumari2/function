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
