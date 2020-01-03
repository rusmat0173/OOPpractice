""" Practicing OOP, with an organisational example """

class Staff:

    def __init__(self, staff_name, staff_role, staff_ID):
        self.staff_name = staff_name
        self.staff_role = staff_role
        self.staff_ID = staff_ID

    # in python we change staff_name and staff_role directly

    def __str__(self):
        return 'Name: {}, Role: {}, ID: {}'.format(self.staff_name, self.staff_role, self.staff_ID)

class Dept:

    # create a class instance. Used if no head
    # ^ this took me ages to work out!!!
    nobody = Staff('None', 'no job', 0)


    # the value with default setting has to go at end
    def __init__(self, budget_ID, dept_name, dept_head=nobody):
        self.dept_name = dept_name
        self.dept_head = dept_head
        self.budget_ID = budget_ID
        self.dept_people = []
        # nobody has to be accessed as self.nobody
        if self.dept_head != self.nobody:
            self.dept_people.append(self.dept_head)

    # add one person at a time
    def add_person(self, person):
        self.dept_people.append(person)

    # * A single star means that the variable 'a' will be a tuple of extra parameters that were supplied to the function. The double star means the variable 'kw' will be a variable-size dictionary
    # of extra parameters that were supplied with keywords.
    # https://stackoverflow.com/questions/400739/what-does-asterisk-mean-in-python
    def add_people(self, *names):
        for person in names:
            self.dept_people.append(person)


    # remove one person at a time
    def remove_person(self, person):
        self.dept_people.remove(person)

    # print out all names of staff.
    # automatically updates if person has chaned their name, e.g.
    # v.imp: because the list generates anew each time from the embedded staff 'instances'
    def people(self):
        staff_list = []
        for person in self.dept_people:
            if person.staff_name != 'No one':
                staff_list.append(person.staff_name)
        print(staff_list)

    def __str__(self):
        return 'Budget ID: {}, Dept Name: {}, Dept Head: {}'.format(self.budget_ID, self.dept_name, self.dept_head.staff_name)

class Project:

    # create a class instance. Used if no leader
    nobody = Staff('None', 'no job', 0)

    def __init__(self, project_name, project_ID, dept, project_leader = nobody):
        self.project_name = project_name
        self.project_ID = project_ID
        self.dept = dept
        self.project_leader = project_leader
        self.open = False
        self.project_people = []
        if self.project_leader != self.nobody:
            self.project_people.append(self.project_leader)

    # onboarding, offboarding staff, and printing list of all people
    # actually, the single person command is somewhat redundant,
    # as you can use the multiple people command with one person
    def onboard_person(self, person):
        self.project_people.append(person)

    def onboard_people(self, *names):
        for person in names:
            self.project_people.append(person)

    def offboard_person(self, person):
        self.project_people.remove(person)

    def people(self):
        staff_list = []
        for person in self.project_people:
            if person.staff_name != 'No one':
                staff_list.append(person.staff_name)
        print(staff_list)

    # summary
    def __str__(self):
        return 'Project Open: {}, Project ID: {}, Project Name: {}, Project Dept: {}, Project Leader: {}'.format(self.open, self.project_ID, self.project_name, self.dept.dept_name, self.project_leader.staff_name)

class ProjectList:

    def __init__(self):
        self.open_projects = []
        self.closed_projects = []

    def open(self, project):
        project.open = True
        self.open_projects.append(project)

    def close(self, project):
        project.open = False
        project.project_people =[]
        self.open_projects.remove(project)
        self.closed_projects.append(project)

    def create_list(self, a_list):
        self.b_list = []
        for item in a_list:
            self.b_list.append(item.project_name)
        return self.b_list

    def __str__(self):
        return 'Open Projects: {} \nClosed Projects: {}'.format(self.create_list(self.open_projects), self.create_list(self.closed_projects))

# = = = = = = =
Rusmat = Staff('Rusmat Roland Ahmed', 'Head of Sales, EMEA', 215)
Rusty = Staff('David Orwin', 'UK Head of Sales', 220)
Craig = Staff('Craig Turner', 'Business Development Director', 219)
Will = Staff('William Day', 'Senior TSS', 2017)
print(Rusmat.staff_name)
print(Rusty.staff_name)
print(Craig)

SalesEMEA = Dept(110, 'Sales EMEA')
print(SalesEMEA)
# ^ note it has given string name

SalesEMEA.add_person(Rusty)

SalesEMEA.add_people(Will, Craig)

SalesEMEA.people()
SalesEMEA.remove_person(Will)
SalesEMEA.people()


Rusty.staff_name = 'Fiona Orwin'
Rusty.staff_role = 'Store Manager'
SalesEMEA.people()
print(Rusty)

VRLT = Project('VRLT', 1000, SalesEMEA, Rusty)
print(VRLT)
VRLT.onboard_people(Will, Craig)
VRLT.people()

BISProjects = ProjectList()
BISProjects.open(VRLT)

BISProjects.close(VRLT)
VRLT.people()
print(VRLT)

print(BISProjects)




