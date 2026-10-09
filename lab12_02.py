number_of_employees = int(input("Enter number of employees: "))
employees = []

for employee_number in range(number_of_employees):
	print(f"\nEmployee {employee_number + 1}")
	employee = {
		"id": input("Enter employee ID: "),
		"name": input("Enter employee name: "),
		"department": input("Enter department: "),
		"salary": float(input("Enter salary: ")),
		"year": int(input("Enter working years: ")),
	}

	employee["bonus"] = [employee["salary"] * (0.10 if employee["year"] > 5 else 0.05)for _ in [employee]][0]
	employees.append(employee)

print("\nEmployee Information")
for employee in employees:
	print(f"ID\t\t{employee['id']}")
	print(f"Name\t\t{employee['name']}")
	print(f"Department\t{employee['department']}")
	print(f"Salary\t\t{employee['salary']}")
	print(f"Year\t\t{employee['year']}")
	print(f"Bonus\t\t{employee['bonus']}")
	print()
