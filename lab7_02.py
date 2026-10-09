start_value = int(input("Enter the starting value: "))
end_value = int(input("Enter the ending value: "))
increment = int(input("Enter the increment value: "))

print ("\nThe Square of \tResult")
print("----------------------------")
for i in range(start_value, end_value, increment):
    square = i ** 2
    print(i, "\t\t", square)