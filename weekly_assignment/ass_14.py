"""Given a dictionary employee_details where the keys are employee IDs and 
values are dictionaries with name, department, and salary, filter and 
create a list of names of employees who have a salary greater than 50,000.
"""

employee_detail = {
    1: {'name':'xyz',
        'department':'AI',
        'salary':100000},
    2: {'name':'abc',
        'department':'Electronics',
        'salary':100000},
    3: {'name':'qwe',
        'department':'Software Development',
        'salary':100000},
    4: {'name':'rty',
        'department':'Marketing',
        'salary':80000},
    5: {'name':'poi',
        'department':'IT',
        'salary':80000},
    6: {'name':'jkl',
        'department':'Management',
        'salary':49000},
    7: {'name':'mnb',
        'department':'HR',
        'salary':48000},
    8: {'name':'hgf',
        'department':'Clerical',
        'salary':47000},
}


high_salary_employee = []
low_salary_employee = []

for i in employee_detail.values():
    if i['salary'] > 50000:
        high_salary_employee.append(i['name'])
    else:
        low_salary_employee.append(i['name'])
print("High Employee Salary",high_salary_employee)
print("Low Employee Salary",low_salary_employee)