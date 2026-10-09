def calculate_revenue(selling_price_per_unit, number_of_units_sold, discount_percentage):
    gross_sales = selling_price_per_unit * number_of_units_sold
    customer_discount = gross_sales * (discount_percentage / 100)
    net_sales = gross_sales - customer_discount
    return gross_sales, customer_discount, net_sales


def calculate_operating_costs(number_of_units_sold, net_sales, production_cost_per_unit, packaging_cost_per_unit, shipping_subsidy_per_unit, marketplace_commission_percentage, payment_processing_fee_percentage, advertising_cost_per_unit, fixed_operating_costs):
    production_cost = production_cost_per_unit * number_of_units_sold
    fulfillment_cost = (packaging_cost_per_unit + shipping_subsidy_per_unit) * number_of_units_sold
    marketplace_commission = net_sales * (marketplace_commission_percentage / 100)
    payment_processing_fee = net_sales * (payment_processing_fee_percentage / 100)
    advertising_cost = advertising_cost_per_unit
    total_business_cost = production_cost + fulfillment_cost + marketplace_commission + payment_processing_fee + advertising_cost + fixed_operating_costs
    return production_cost, fulfillment_cost, marketplace_commission, payment_processing_fee, advertising_cost, total_business_cost


def calculate_operating_profit(net_sales, total_business_cost):
    operating_profit = net_sales - total_business_cost
    return operating_profit


selling_price_per_unit = float(input("Enter the selling price per unit: "))
number_of_units_sold = int(input("Enter the number of units sold: "))
discount_percentage = float(input("Enter the discount percentage ( % ): "))
production_cost_per_unit = float(input("Enter the production cost per unit: "))
packaging_cost_per_unit = float(input("Enter the packaging cost per unit: "))
shipping_subsidy_per_unit = float(input("Enter the shipping subsidy per unit: "))
marketplace_commission_percentage = float(input("Enter the marketplace commission percentage ( % ): "))
payment_processing_fee_percentage = float(input("Enter the payment processing fee percentage ( % ): "))
advertising_cost_per_unit = float(input("Enter the advertising cost per unit: "))
fixed_operating_costs = float(input("Enter the fixed operating costs: "))

gross_sales, customer_discount, net_sales = calculate_revenue(selling_price_per_unit, number_of_units_sold, discount_percentage)
production_cost, fulfillment_cost, marketplace_commission, payment_processing_fee, advertising_cost, total_business_cost = calculate_operating_costs(number_of_units_sold, net_sales, production_cost_per_unit, packaging_cost_per_unit, shipping_subsidy_per_unit, marketplace_commission_percentage, payment_processing_fee_percentage, advertising_cost_per_unit, fixed_operating_costs)
operating_profit = calculate_operating_profit(net_sales, total_business_cost)

print("========= E-Commerce Campaign Report =========")
print(f"Gross Sales                      : {gross_sales:.2f} Baht")
print(f"Customer discount                : {customer_discount:.2f}")
print(f"Net Sales                        : {net_sales:.2f} Baht")
print(f"Marketplace Commission           : {marketplace_commission:.2f} Baht")
print(f"Payment Processing Fee           : {payment_processing_fee:.2f} Baht")
print(f"Total Platform Fee               : {marketplace_commission + payment_processing_fee:.2f} Baht")
print(f"Product Cost                     : {production_cost:.2f} Baht")
print(f"Fulfillment Cost                 : {fulfillment_cost:.2f} Baht")
print(f"Advertising Cost                 : {advertising_cost:.2f} Baht")
print(f"Fixed Operating Cost             : {fixed_operating_costs:.2f} Baht")
print(f"Total Business Cost              : {total_business_cost:.2f} Baht")
print(f"Operating Profit                 : {operating_profit:.2f} Baht")