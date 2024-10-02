cake_1 = "Black Forest"
cake_2 = "Vanilla Cake"

#inventory cost for Black Forest Starts

material_cost_cake_1 = 180
transportation_cost_cake_1 = 50
material_transportation_cost_cake_1 = material_cost_cake_1 + transportation_cost_cake_1
utility_cost_cake_1 = (3*material_transportation_cost_cake_1)/100
space_cost_cake_1 = 60
staff_cost_cake_1 = 50

print("Material Cost",material_cost_cake_1)
print("Transportation Cost",transportation_cost_cake_1)
print("utility Cost",utility_cost_cake_1)
print("space Cost",space_cost_cake_1)
print("Staff Cost",staff_cost_cake_1)

inventory_cost_cake_1 = material_cost_cake_1+transportation_cost_cake_1+utility_cost_cake_1+space_cost_cake_1+staff_cost_cake_1

print("Inventory Cost",inventory_cost_cake_1)

sale_cost_cake1 = 1500

discount_cake_1 = sale_cost_cake1 - (3*1500)/100

profit_cake_1 = discount_cake_1 - inventory_cost_cake_1

total_profit_cake1= profit_cake_1*12

print("sale cost before discount",sale_cost_cake1)
print("sale cost after discount",discount_cake_1)
print("profit",profit_cake_1)
print("total_profit",total_profit_cake1)

#inventory cost for vanilla cake
