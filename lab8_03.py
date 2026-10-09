grand_total = 0
for zone in range(1, 4):
    print(f"============ Zone {zone} ============")
    zone_total = 0
    for vehicles in range(1,5) :
        print(f"Vehicle {vehicles} : ")
        hour = int(input("Enter the number of hours parked: "))
        if hour <= 2:
            fee = hour * 20
        else :
            fee = 40 + (hour - 2) * 30
        zone_total += fee
        print(f"Parking fee: ${fee:.2f} Bath\n")
    print(f"\nTotal fees for Zone {zone}: {zone_total:.2f} Bath")
    grand_total += zone_total
print("\n=====================================")
print(f"Grand Total Parking Fees: {grand_total:.2f} Bath")
print("=====================================")