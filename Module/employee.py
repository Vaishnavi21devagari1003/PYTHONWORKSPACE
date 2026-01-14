import employee_util
import logging

logging.basicConfig(level=logging.INFO)

logging.info("Program Started")
Name=input("enter the name:")
designation=input("enter the designation:")
salary=float(input("enter basic salary:"))
leaves=int(input("enter the leaves:"))


bonus, deduction, final_salary = employee_util.cal_salary(salary, designation, leaves)

print("\n--- Salary Slip ---")
print(f"Name: {Name}")
print(f"Designation: {designation}")
print(f"Basic Salary: {salary}")
print(f"Bonus: {bonus}")
print(f"Deduction: {deduction}")
print(f"Final Salary: {final_salary}")
logging.info("The program ends")