
unit_price = 2500

def commision_calculator(sales):
    commision = 0
    if sales >= 500:
        commision = sales * unit_price * 0.05
    elif sales >= 400:
        commision = sales * unit_price * 0.04
    elif sales >= 300:
        commision = sales * unit_price * 0.03
    elif sales >= 200:
        commision = sales * unit_price * 0.02
    elif sales >= 100:
        commision = sales * unit_price * 0.01
    else:
        commision = sales * unit_price * 0.005
    return commision


def tax_calculator(total):
    if total >= 500000:
        return total * 0.20
    elif total >= 400000:
        return total * 0.15
    elif total >= 300000:
        return total * 0.10
    elif total >= 200000:
        return total * 0.075
    elif total >= 100000:
        return total * 0.05
    else:
        return total * 0


def loan_installment_calculator(basic_salary):
    return basic_salary * 0.20


def medical_allounce_calculator(basic_salary):
    return basic_salary * 0.15


def housing_allounce_calculator(basic_salary):
    return basic_salary * 0.15


def bonus_calculator(sale_amt):
    if sale_amt >= 100000:
        return 25000
    elif sale_amt >= 50000:
        return 15000
    elif sale_amt >= 25000:
        return 7000
    else:
        return 0


def sales_amt_calculator(sales):
    sale_amt = sales * unit_price
    return sale_amt


def disbured_salary(emp_id, emp_name, basic_salary, sales):
    sale_amt = sales_amt_calculator(sales)
    bonus = bonus_calculator(sale_amt)
    commision = commision_calculator(sales)
    medical_allounce = medical_allounce_calculator(basic_salary)
    house_allounce = housing_allounce_calculator(basic_salary)
    loan_amt = loan_installment_calculator(basic_salary)
    
    total = basic_salary + bonus + commision + medical_allounce + house_allounce
    tax_amt = tax_calculator(total)
    deductions = loan_amt + tax_amt
    gross = total - deductions
    return gross, bonus, commision, medical_allounce, house_allounce, tax_amt, loan_amt


# ==== Main Program ====
emp_name = input("Please enter the employee name: ")
emp_id = input("Please enter the emp ID: ")
basic_salary = int(input("Enter the basic salary of the emp: "))
sales = int(input("How many units sold: "))

gross, bonus, commision, medical_allounce, house_allounce, tax_amt, loan_amt = disbured_salary(
    emp_id, emp_name, basic_salary, sales
)

print(f"""
                     Salary Slip
        ======================================

        Emp_Name         : {emp_name}
        Emp_ID           : {emp_id}
        Basic            : {basic_salary}
        Commision        : {commision}
        Medical Allounce : {medical_allounce}
        House Allounce   : {house_allounce}
        Bonus            : {bonus}
        Tax              : {tax_amt}
        Loan Deductions  : {loan_amt}

        GROSS Salary     : {gross}
""")
