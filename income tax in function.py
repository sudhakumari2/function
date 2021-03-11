def taxes(income):
    while True:
        if income < 10000:
            tax = 0
        elif income > 10000 and income <= 30000:
            tax = (income-10000)*(0.1)
        elif income > 30000 and income <= 70000:
            tax = (income-30000)*(0.2) + 2000
        elif income > 70000:
            tax = (income - 70000)*(0.3) + 10000
        return tax
income=int(input("enter salary"))
print(taxes(income))
