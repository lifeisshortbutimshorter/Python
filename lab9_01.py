def calculate_revenue(price_per_night, number_of_rooms_sold, number_of_nights, booking_comission):
    Gross_revenue = price_per_night * number_of_rooms_sold * number_of_nights
    booking_comission_amount = Gross_revenue * (booking_comission / 100)
    net_revenue = Gross_revenue - booking_comission_amount
    return Gross_revenue, booking_comission_amount, net_revenue


def calculate_operating_profit(number_of_rooms_sold, number_of_nights, housekeeping_fee, utility_fee, fixed_costs, net_revenue):
    housekeeping_cost = housekeeping_fee * number_of_rooms_sold * number_of_nights
    utility_cost = utility_fee * number_of_rooms_sold * number_of_nights
    fixed_operating_costs = fixed_costs
    total_operating_costs = housekeeping_cost + utility_cost + fixed_operating_costs
    operating_profit = net_revenue - total_operating_costs
    return operating_profit, housekeeping_cost, utility_cost, fixed_operating_costs, total_operating_costs

price_per_night = float(input("Enter the price per night: "))
number_of_rooms_sold = int(input("Enter the number of rooms sold: "))
number_of_nights = int(input("Enter the number of nights: "))
booking_comission = float(input("Enter the booking commission ( % ): "))
housekeeping_fee = float(input("Enter the housekeeping fee per room per night: "))
utility_fee = float(input("Enter the utility fee per room per night: "))
fixed_costs = float(input("Enter the fixed costs: "))

(
    gross_revenue,
    booking_comission_amount,
    net_revenue,
 ) = calculate_revenue(
    price_per_night,
    number_of_rooms_sold,
    number_of_nights,
    booking_comission,
)

(
    operating_profit,
    housekeeping_cost,
    utility_cost,
    fixed_operating_costs,
    total_operating_costs,
) = calculate_operating_profit(
    number_of_rooms_sold,
    number_of_nights,
    housekeeping_fee,
    utility_fee,
    fixed_costs,
    net_revenue,
)
print("----------------------------------------------")
print("\n   HOTEL ROOM OPERATING PROFIT SUMMARY\n")
print("----------------------------------------------")
print(f"Gross revenue                  : {gross_revenue:.2f} Bath")
print(f"Booking commission             : {booking_comission_amount:.2f} Bath")
print(f"Net revenue                    : {net_revenue:.2f} Bath")
print(f"Housekeeping cost              : {housekeeping_cost:.2f} Bath")
print(f"Utility cost                   : {utility_cost:.2f} Bath")
print(f"Fixed costs                    : {fixed_operating_costs:.2f} Bath")
print(f"Total operating costs          : {total_operating_costs:.2f} Bath")
print(f"The operating profit is        : {operating_profit:.2f} Bath")