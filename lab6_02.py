patient_name = input("Enter the patient's name: ")
age = int(input("Enter the patient's age: "))
height = float(input("Enter the patient's height (cm): "))
weight = float(input("Enter the patient's weight (kg): "))
BMI = weight / ((height / 100) ** 2)

if BMI < 18.5:
    weight_status = "Underweight"
elif 18.5 <= BMI < 22.9:
    weight_status = "Normal weight"
elif 23.0 <= BMI < 24.9:
    weight_status = "Overweight"
elif 25.0 <= BMI < 29.9:
    weight_status = "Obesity Class 1"
else:
    weight_status = "Obesity Class 2"

print("\n============== OUTPUT ==============\n")

print(f"Patient Name  : {patient_name}")
print(f"Age           : {age} Years")
print(f"Height        : {height:.2f} cm")
print(f"Weight        : {weight:.2f} kg")
print(f"BMI           : {BMI:.2f}")
print(f"Weight Status : {weight_status}")

print("\n=====================================\n")