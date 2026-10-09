first_number = int(input("Enter the first number: "))
second_number = int(input("Enter the second number: "))

print("\n============ MENU ============\n")
print("1. Minimum")
print("2. Maximum")
print("\n===============================\n")

choice = int(input("Enter your choice (1 or 2): "))

print("\n========== OUTPUT ===========\n")
if choice == 1:
    if first_number <= second_number:
        result = first_number
    else:
        result = second_number
    print(f"The minimum of {first_number} and {second_number} is {result}")
elif choice == 2:
    if first_number >= second_number:
        result = first_number
    else:
        result = second_number
    print(f"The maximum of {first_number} and {second_number} is {result}")
else : 
    print("Invalid you dambass pick 1 or 2 you dumbass")

print("\n========DATTEBAYO=========\n")