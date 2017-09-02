class Employee:
    raise_amount = 1.05
    no_of_emp = 0
    def __init__(self):
        pass
    def details(self,first,last,pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@mail.com'

        Employee.no_of_emp += 1

    def raise_pay(self):
        #self.pay = int(self.pay * Employee.raise_amount)
        self.pay = int(self.pay * self.raise_amount)


print(Employee.no_of_emp)

emp1 = Employee()
emp2 = Employee()
#emp3 = Employee()

emp1.details('Vishal','Karda',20000)
emp2.details('Pragya', 'Marodia',20000)
#Employee.details(emp3,'Aastha','Tamas',25000)

#print(emp1.email)
#print(emp2.email)
#print(emp3.email)

#print('{} {} '.format(emp1.first, emp1.last))

#Employee.raise_amount = 1.06
emp1.raise_amount = 1.04
#print(emp1.__dict__)
print(emp1.pay)
emp1.raise_pay()
print(emp1.pay)

#print(Employee.raise_amount)
#print(emp1.raise_amount)
#print(emp2.raise_amount)

print(Employee.no_of_emp)


#print(Employee.__dict__)