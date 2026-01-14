import logging

logging.basicConfig(level=logging.INFO)
paid_leaves=15
working_days=30

def get_bonus(designation,salary):
    if designation=="coder":
        return salary*0.10
    elif designation=="designer":
        return salary* 0.15
    elif designation=="manager":
        return salary*0.5
    else:
         logging.warning("U have a selected wrong")
         return 0
    
def cal_salary(salary, designation, leaves):
    bonus = get_bonus(designation, salary)
    total_salary = salary + bonus

    # Check for unpaid leaves
    if leaves > paid_leaves:
        unpaid = leaves - paid_leaves
    else:
        unpaid = 0

    # Deduction per day is based on total salary
    day = total_salary / working_days
    deduction = unpaid * day

    # Final salary after deduction
    final_salary = total_salary - deduction
    return bonus, deduction, final_salary

