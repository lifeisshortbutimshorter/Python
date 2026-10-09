trip_distance = float(input("Enter the trip distance in miles: "))
fuel_consumption = float(input("Enter the fuel consumption in miles per gallon: "))
fuel_price = float(input("Enter the fuel price per gallon: "))

fuel_used = trip_distance / fuel_consumption
total_cost = fuel_used * fuel_price

print(f"Fuel used: {fuel_used:.2f} gallons")
print(f"Total cost: ${total_cost:.2f}")