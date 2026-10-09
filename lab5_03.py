reservation_name = input("Enter the name for the reservation: ")
number_of_travelers = int(input("Enter the number of travelers: "))
destination_country = input("Enter the destination country (Asia/Europe): ")
member = input("Are you a member? (yes/no): ")

if destination_country.lower() == "asia":
    cost_per_traveler = 2500
elif destination_country.lower() == "europe":
    cost_per_traveler = 5000
if member.lower() == "yes":
    print("You are eligible for a 10% discount on the total cost.")

total_cost = number_of_travelers * cost_per_traveler
member_discount =   total_cost * 0.10 if member.lower() == "yes" else 0
travel_cost = total_cost - member_discount



print("\n========== TRAVEL RESERVATION RECEIPT ==========\n")

print(f"Reservation Name: {reservation_name}")
print(f"Number of Travelers: {number_of_travelers}")
print(f"Destination Country: {destination_country}")
print(f"Total Cost: ${total_cost}")
print(f"Member Discount: ${member_discount}")
print(f"Travel Cost : ${travel_cost} ")