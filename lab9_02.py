def calculate_fuel_cost(travel_distance, fuel_efficiency, fuel_price):
    fuel_cost = (travel_distance / fuel_efficiency) * fuel_price
    return fuel_cost


def calculate_hotel_cost(hotel_price_per_night, number_of_travel_days):
    hotel_cost = (hotel_price_per_night * 2) * number_of_travel_days
    return hotel_cost

def calculate_food_cost(food_cost_per_day, number_of_travel_days, number_travelers):
    food_cost = food_cost_per_day * number_of_travel_days * number_travelers
    return food_cost


def calculate_total_cost(fuel_cost, hotel_cost, food_cost):
    total_trip_cost = fuel_cost + hotel_cost + food_cost
    return total_trip_cost

num_travelers = int(input("Enter the number of travelers: "))
number_of_travel_days = int(input("Enter the number of travel days: "))
hotel_price_per_night = float(input("Enter the hotel price per night: "))
food_cost_per_day = float(input("Enter the food cost per day: "))
travel_distance = float(input("Enter the travel distance (in km): "))
fuel_efficiency = float(input("Enter the fuel efficiency (in km/liter): "))
fuel_price = float(input("Enter the fuel price (per liter): "))


fuel_cost = calculate_fuel_cost(travel_distance, fuel_efficiency, fuel_price)
hotel_cost = calculate_hotel_cost(hotel_price_per_night, number_of_travel_days)
food_cost = calculate_food_cost(food_cost_per_day, number_of_travel_days, num_travelers)
total_trip_cost = calculate_total_cost(fuel_cost, hotel_cost, food_cost)
print("====== Travel Cost Summary ======")
print(f"Fuel cost                 : {fuel_cost:.2f} Bath")
print(f"Hotel cost                : {hotel_cost:.2f} Bath")
print(f"Food cost                 : {food_cost:.2f} Bath")
print(f"Total trip cost           : {total_trip_cost:.2f} Bath")