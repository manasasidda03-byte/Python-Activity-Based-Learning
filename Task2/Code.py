material = float(input("Enter material cost: "))
labour = float(input("Enter labour charges: "))
wastage = float(input("Enter wastage cost: "))
machine = float(input("Enter machine cost: "))
selling_price = float(input("Enter selling price: "))
target = float(input("Enter target profit percentage: "))
if min(material, labour, wastage, machine,
       selling_price, target) < 0:
    print("Invalid input! Values cannot be negative.")
else:
    total_cost = material + labour + wastage + machine
    profit = selling_price - total_cost
    if total_cost > 0:
        profit_percent = (profit / total_cost) * 100
    else:
        profit_percent = 0
    print("\n--- Manufacturing Report ---")
    print("Total Manufacturing Cost:", total_cost)
    print("Selling Price:", selling_price)
    print("Profit/Loss:", profit)
    print("Profit Percentage:", round(profit_percent, 2), "%")
    if profit_percent >= target:
        print("Result: Profit Target Achieved")
    else:
        print("Result: Profit Target Not Achieved")

