def check_numbers(a,b):
	i=0
	while i<len(a):
		j=0
		while j<len(b):
			if i==j:
				if a[i]%2==0 and b[j]%2==0:
					print('dono even hai',a[i],b[j])
				else:
					print('dono even nhi hai',a[i],b[j])
			j+=1
		i+=1
check_numbers([2, 6, 18, 10, 3, 75] ,[6, 19, 24, 12, 3, 87])
# Check odd ya even