num_of_bookings = int(input("Enter the number of bookings: "))
list_bookings = []

list_destinations = []
list_types_of_transportation = []
list_types_of_rooms = []
list_types_of_activity_packages = []
list_number_of_nights = []
list_transportation_costs = []
list_hotel_costs = []
list_activity_costs = []
list_total_costs = []

for i in range(num_of_bookings):
    def transport_cost(destination, transportation):
        if destination == "Chaing Rai" :
            if transportation == "Bus":
                transportation_cost = 500
                return transportation_cost
            elif transportation == "Van":
                transportation_cost = 800
                return transportation_cost
            elif transportation == "Flight":
                transportation_cost = 1800
                return transportation_cost
            else:
                return 0
            
        elif destination == "Phuket" :
            if transportation == "Bus":
                transportation_cost = 1200
                return transportation_cost
            elif transportation == "Van":
                transportation_cost = 1500
                return transportation_cost
            elif transportation == "Flight":
                transportation_cost = 3000
                return transportation_cost
            else:
                return 0
            
        elif destination == "Bangkok" :
            if transportation == "Bus":
                transportation_cost = 700
                return transportation_cost
            elif transportation == "Van":
                transportation_cost = 1000
                return transportation_cost
            elif transportation == "Flight":
                transportation_cost = 2200
                return transportation_cost
            else:
                return 0
        else:
            return 0
        
    def hotel_cost(room_type, number_of_nights):
            if room_type == "Standard":
                return 1200 * number_of_nights
            elif room_type == "Deluxe":
                return 1800 * number_of_nights
            elif room_type == "Suite":
                return 2500 * number_of_nights
            else:
                return 0
    def activity_cost(activity_package):
        if activity_package == "Basic":
            return 800
        elif activity_package == "Standard":
            return 1000
        elif activity_package == "Premium":
            return 2500
        else:
            return 0
  
    print(f"Booking {i + 1}:")
    destination = input("Enter the destination (Chaing Rai/Phuket/Bangkok): ")
    transportation = input("Enter the transportation type (Bus/Van/Flight): ")
    room_type = input("Enter the room type (Standard/Deluxe/Suite): ")
    number_of_nights = int(input("Enter the number of nights : "))
    activity_package = input("Enter the activity package (Basic/Standard/Premium): ")

    transportation_cost_value = transport_cost(destination, transportation)
    hotel_cost_value = hotel_cost(room_type, number_of_nights)
    activity_cost_value = activity_cost(activity_package)
    list_destinations.append(destination)
    list_number_of_nights.append(number_of_nights)
    list_transportation_costs.append(transportation_cost_value)
    list_hotel_costs.append(hotel_cost_value)
    list_activity_costs.append(activity_cost_value)
    list_total_costs.append(transportation_cost_value + hotel_cost_value + activity_cost_value)
    list_types_of_transportation.append(transportation)
    list_types_of_rooms.append(room_type)
    list_types_of_activity_packages.append(activity_package)

    print("\n======== Booking Summary ========\n")
    print(f"Booking {i + 1}")
    print(f"Destination: {destination}")
    print(f"Transportation: {transportation}")
    print(f"Room Type: {room_type}")
    print(f"Number of Nights: {number_of_nights}")
    print(f"Activity Package: {activity_package}")
    print(f"Transportation Cost: {transportation_cost_value} Baht")
    print(f"Hotel Cost: {hotel_cost_value} Baht")
    print(f"Activity Cost: {activity_cost_value} Baht")
    print(f"Total Cost: {transportation_cost_value + hotel_cost_value + activity_cost_value} Baht")
