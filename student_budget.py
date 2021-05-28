def student_budget(*number_of_student):
	i=0
	s=0
	budget=int(input('enter budget'))
	while i<len(number_of_student):
		print('student ka kharcha',budget)
		s+=budget
		i+=1
	if s<50000:
		print('budget ke andar h',s)
	else:
		print('budget ke bahar h',s)
student_budget('sudha','rani','prerti','reena')