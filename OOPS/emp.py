# # class Employee:
# #     def __init__(self,emp_id=None,emp_name=None,emp_salary=None):
# #         self.emp_id=emp_id
# #         self.emp_name=emp_name
# #         self.emp_salary=emp_salary

# #     def display(self):
# #         print("Employee Id:",self.emp_id)
# #         print("Employee Name:",self.emp_name)
# #         print("Employee Salary:",self.emp_salary)

# # emp=Employee(1,"Vaishu",25000)
# # # emp.display()
# # emp1=Employee(2,"Vaishnavi",30000)
# # # emp1.display()
# # emp2=Employee(3,"Vaish",35000)

# # emps=[emp,emp1,emp2]
# # emps.append(Employee(102,"Sai",20000))

# # def add_employee(emp_list,emp_new):
# #     for e in emp_list:
# #         if e.emp_id==emp_new.emp_id:
# #             print("The id is also exist")
# #             return 
# #     emp_list.append(emp_new)
# #     print("added successfully")

# # add_employee(emps, Employee(102, "Sai", 20000)) 
# # add_employee(emps, Employee(2, "Duplicate", 40000))

# # for item in emps: 
# #     item.display()

# class Employee:
#     def __init__(self, emp_id=None, emp_name=None, emp_salary=None):
#         self.emp_id = emp_id
#         self.emp_name = emp_name
#         self.emp_salary = emp_salary

#     def display(self):
#         print("Employee Id:", self.emp_id)
#         print("Employee Name:", self.emp_name)
#         print("Employee Salary:", self.emp_salary)


# # Existing employees
# emp = Employee(1, "Vaishu", 25000)
# emp1 = Employee(2, "Vaishnavi", 30000)
# emp2 = Employee(3, "Vaish", 35000)

# emps = {emp, emp1, emp2}
# emps.add(Employee(102, "Sai", 20000))


# def add_employee(emp_list, emp_new):
#     # Check for duplicate ID
#     for e in emp_list:
#         if e.emp_id == emp_new.emp_id:
#             print(f"Employee ID {emp_new.emp_id} already exists! Cannot add {emp_new.emp_name}.")
#             return  # Stop here, don’t append
#     emp_list.add(emp_new)
#     print(f"Employee {emp_new.emp_name} added successfully.")


# # Test adding employees
# add_employee(emps, Employee(102, "Sai", 20000))   # Duplicate → rejected
# add_employee(emps, Employee(2, "Duplicate", 40000))  # Duplicate → rejected
# add_employee(emps, Employee(103, "NewEmp", 28000))   # Unique → added

# # Display all employees
# for item in emps:
#     item.display()

class Employee:
    def __init__(self, emp_id=None, emp_name=None, emp_salary=None):
        self.emp_id = emp_id
        self.emp_name = emp_name
        self.emp_salary = emp_salary

    def display(self):
        print("Employee Id:", self.emp_id)
        print("Employee Name:", self.emp_name)
        print("Employee Salary:", self.emp_salary)


# Store employees in a dictionary with emp_id as key
emps = {
    1: Employee(1, "Vaishu", 25000),
    2: Employee(2, "Vaishnavi", 30000),
    3: Employee(3, "Vaish", 35000)
}


def add_employee(emp_dict, emp_new):
    if emp_new.emp_id in emp_dict:
        print(f"Employee ID {emp_new.emp_id} already exists! Cannot add {emp_new.emp_name}.")
    else:
        emp_dict[emp_new.emp_id] = emp_new
        print(f"Employee {emp_new.emp_name} added successfully.")


# Add employees
add_employee(emps, Employee(102, "Sai", 20000))   # Added
add_employee(emps, Employee(2, "Duplicate", 40000))  # Rejected

# Display all employees
for emp_id, emp_obj in emps.items():
    emp_obj.display()
