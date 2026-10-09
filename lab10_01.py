employee_name = input("Enter the employee's name: ")
basic_salary = float(input("Enter the basic salary: "))
years_of_work = int(input("Enter the number of years of work: "))
overtime_hours = float(input("Enter the number of overtime hours: "))
overtime_rate = float(input("Enter the overtime rate: "))
social_security = float(input("Enter the social security contribution: "))
tax_rate = float(input("Enter the tax rate ( % ): "))

def calculate_income(basic_salary, years_of_work, overtime_hours, overtime_rate):
    if years_of_work < 3:
        bonus_rate = 0
    elif years_of_work < 5:
        bonus_rate = 0.05
    elif years_of_work <= 10:
        bonus_rate = 0.10
    else:
        bonus_rate = 0.15
    gross_salary = basic_salary + (basic_salary * bonus_rate) + (overtime_hours * overtime_rate)
    overtime_pay = overtime_hours * overtime_rate
    return gross_salary, overtime_pay

def calculate_deductions(social_security, tax_rate, gross_salary, basic_salary, overtime_pay):
    social_security_amount = gross_salary * (social_security / 100)
    tax_amount = gross_salary * (tax_rate / 100)
    total_deductions = social_security_amount + tax_amount
    net_salary = gross_salary - total_deductions
    service_bonus = gross_salary - basic_salary - overtime_pay
    return social_security_amount, total_deductions, tax_amount, net_salary, service_bonus

gross_salary, overtime_pay = calculate_income(basic_salary, years_of_work, overtime_hours, overtime_rate)
social_security_amount, total_deductions, tax_amount, net_salary, service_bonus = calculate_deductions(social_security, tax_rate, gross_salary, basic_salary, overtime_pay)


print("\n============== OUTPUT ==============\n")
print(f"Employee Name    : {employee_name}")
print(f"Basic Salary     : {basic_salary:.2f} Bath")
print(f"Overtime Pay     : {overtime_pay:.2f} Bath")
print(f"Service Bonus    : {service_bonus:.2f} Bath")
print(f"Gross Salary     : {gross_salary:.2f} Bath")
print(f"Social Security  : {social_security_amount:.2f} Bath")
print(f"Total Deductions : {total_deductions:.2f} Bath")
print(f"Tax Amount       : {tax_amount:.2f} Bath")
print(f"Net Salary       : {net_salary:.2f} Bath")
print("\n=====================================\n")