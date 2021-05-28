def ek_perfect():
	i=1
	while i<=1000:
			j=1
			s=0
			while j<i:
				if i%j==0:
					s=s+j
				j+=1
			if s==i:
				print('perfect no h',i)
			else:
				print('perfect no nhi hai ',i)
			i+=1
ek_perfect()
