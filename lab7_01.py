number = int(input("Enter a number: "))

print("\nMultiplication Table for", number)

print("\n----------------------------\n")
for i in range(1, 13):
    result = number * i
    print(number, "x", i, "=", result)