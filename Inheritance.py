class TeamLead():  
    def work(self):
        print("Managing tasks")

class Manager:
    def work(self):
        print("Overseeing team progress")

class Employee(TeamLead,Manager):
    def work(self):
        print("Completing assigned tasks")

emp = Employee()
emp.work() 



class Employee:
    def work(self):
        print("Completing assigned tasks.")

class Manager(Employee):  
    def work(self):
        print("Overseeing team progress.")

class TeamLead(Manager):  
    def work(self):
        print("Managing tasks and working on projects.")

lead = TeamLead()
lead.work() 
