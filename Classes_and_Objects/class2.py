class Employee:
    """Common base class for all employees"""
    empCount = 0

    def __init__(self,name,salary):
        self.name = name
        self.salary = salary
        Employee.empCount += 1

    def displayCount(self):
        print("The Total Employee %d" % Employee.empCount)

    def displayEmployee(self):
        print("Name : ",self.name, ", Salary : ", self.salary)


employee1 = Employee("King",150000)
employee2 = Employee("Mike",300000)
print("The Total Number of Employees is %d" % Employee.empCount)
print(employee1.name,employee1.salary)
print(employee2.name,employee2.salary)
