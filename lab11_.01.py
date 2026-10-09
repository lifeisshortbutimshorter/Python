num_of_employees = int(input("Enter the number of employees: "))
list_name = []
list_sales = []
list_level = []
bonus = []

for i in range(num_of_employees):
    name = input(f"Enter the name of employee {i + 1}: ")
    total_sales = float(input(f"Enter the total sales for {name}: "))
    list_name.append(name)
    list_sales.append(total_sales)
    
    if total_sales >= 100000 :
        level = "A"
    elif total_sales < 50000 :
        level = "B"
    else :
        level = "C"
    list_level.append(level)
    if level == "A":
        bonus.append(total_sales * 0.15)
    elif level == "B":
        bonus.append(total_sales * 0.10)
    else:
        bonus.append(total_sales * 0.05)

print ("\n======== Empolyee Data ========")
print(f"Name List  : {list_name}")
print(f"Sales List : {list_sales}")
print(f"Level List : {list_level}")
print(f"Bonus List : {bonus}")

print("\n======== Level Summary ========")
print("Number of employees in level A: ", list_level.count("Level A"))
print("Number of employees in level B: ", list_level.count("Level B"))
print("Number of employees in level C: ", list_level.count("Level C"))

print("\n======== Highest Sales Employees ========")
max_sales = max(list_sales)
for i in range(len(list_sales)):
    if list_sales[i] == max_sales:
        
        print(f"Name   : {list_name[i]} ")
        print(f"Sales  : {list_sales[i]}")
        print(f"Level  : {list_level[i]}")
        print(f"Bonus  : {bonus[i]}")

