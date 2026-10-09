reservation_name = input("Enter the name for the reservation: ")
destination_country = input("Enter the destination country: ")
number_of_travelers = int(input("Enter the number of travelers: "))

if destination_country.lower() == "asia":
    if number_of_travelers >= 10 :
        cost_per_traveler = 1500.00
    elif number_of_travelers >= 5:
        cost_per_traveler = 2000.00
    else:
        cost_per_traveler = 2500.00
    
elif destination_country.lower() == "europe":
    if number_of_travelers >= 10 :
        cost_per_traveler = 3000.00
    elif number_of_travelers >= 5:
        cost_per_traveler = 3500.00
    else:
        cost_per_traveler = 4000.00
else:
    print("Invalid destination country.")
    exit()

member_condition = input("Enter the member condition (Gold, Silver, Platinum): ")
total_cost = cost_per_traveler * number_of_travelers

if member_condition == "Platinum":
    overall_cost = total_cost - (total_cost * 30 / 100)
    discount = 30
elif member_condition == "Gold":
    overall_cost = total_cost - (total_cost * 20 / 100)
    discount = 20
elif member_condition == "Silver":
    overall_cost = total_cost - (total_cost * 10 / 100)
    discount = 10
else:
    overall_cost = total_cost
    discount = 0
    print("You are not eligible for any discount.")

print("\n========== TRAVEL RESERVATION RECEIPT ==========\n")

print(f"Reservation Name              : {reservation_name}")
print(f"Destination Country           : {destination_country}")
print(f"Number of Travelers           : {number_of_travelers}")
print(f"Member Condition              : {member_condition}")
print(f"Cost per Traveler             : ${cost_per_traveler:.2f}")
print(f"Total travel cost             : ${total_cost:.2f}")
print(f"Discounted ( {discount}% )            : ${total_cost - overall_cost:.2f}")
print(f"Overall Cost                  : ${overall_cost:.2f}")

print("\n==============================================\n")