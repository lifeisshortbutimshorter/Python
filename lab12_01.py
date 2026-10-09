number_of_areas = int(input("Enter the number of parking areas: "))

car_parking = []
for area_index in range(number_of_areas):
    area_vehicles = []
    for vehicle_index in range(4):
        vehicle_number = vehicle_index + 1
        vehicle_type = input(
            f"Enter the type of vehicle {vehicle_number} "
            f"in area {area_index + 1} (Car/Motorcycle): ").capitalize()
        parking_hours = int(input(
                f"Enter parking hours for vehicle {vehicle_number} "
                f"in area {area_index + 1}: "))
        area_vehicles.append([vehicle_type, parking_hours])

    car_parking.append(area_vehicles)

print("\nCar Parking Information")
for area_index in range(len(car_parking)):
    print(f"Parking Area: {area_index + 1}")
    for vehicle_index in range(len(car_parking[area_index])):
        print(
            f"Vehicle {vehicle_index + 1}:\t"
            f"{car_parking[area_index][vehicle_index]}")
    print()

print("Car Parking Fee")
for area_index in range(len(car_parking)):
    total_fee = 0
    print(f"Parking Area: {area_index + 1}")

    for vehicle_index in range(len(car_parking[area_index])):
        vehicle = car_parking[area_index][vehicle_index]
        vehicle_type = vehicle[0]
        parking_hours = vehicle[1]

        if vehicle_type == "Car":
            parking_fee = 100 + max(0, parking_hours - 2) * 50
        else:
            parking_fee = 50 + max(0, parking_hours - 2) * 20

        vehicle.append(parking_fee)
        total_fee += parking_fee
        print(f"Vehicle {vehicle_index + 1}:\t{vehicle}")

    print(f"Total Fee: {total_fee}")
    print()


