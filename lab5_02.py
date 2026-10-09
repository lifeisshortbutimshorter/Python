vehicle_brand = str(input("Enter the vehicle brand: "))
number_plate = str(input("Enter the vehicle number plate: "))
parking_duration = int(input("Enter the parking duration in hours: "))

parking_fee_per_hour = 30
total_parking_fee = parking_duration * parking_fee_per_hour

if parking_duration > 5:
    parking_service_fee = 150
else:
    parking_service_fee = 60

total_amount = total_parking_fee + parking_service_fee

print("\n========== HOTEL PARKING RECEIPT ==========\n")

print(f"Vehicle Brand: {vehicle_brand}")
print(f"Number Plate: {number_plate}")
print(f"Parking Duration: {parking_duration} hours")
print(f"Parking Fee per Hour: ${parking_fee_per_hour}")
print(f"Parking Fee: ${total_parking_fee}")
print(f"Parking Service Fee: ${parking_service_fee}")
print(f"Total Amount Due: ${total_amount}")
print("\nThank you for using our parking service!")

print("\n========================================\n")