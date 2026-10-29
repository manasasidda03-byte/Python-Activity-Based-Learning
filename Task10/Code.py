n = int(input("Enter number of products: "))
products = []
total_revenue = 0
for i in range(n):
    print("\nEnter details for product", i + 1)
    name = input("Product name: ")
    price = float(input("Price: "))
    stock = int(input("Initial stock: "))
    ordered = int(input("Ordered quantity: "))
    dispatched = int(input("Dispatched quantity: "))
    returned = int(input("Returned quantity: "))
    actual_stock = int(input("Actual stock: "))

    if (price < 0 or min(stock, ordered, dispatched,
                         returned, actual_stock) < 0
            or dispatched > ordered
            or returned > dispatched
            or dispatched > stock):
        print("Invalid product or order details!")
        break
    order_value = price * ordered
    discount_rate = 0.10 if order_value >= 5000 else 0
    discounted_price = price * (1 - discount_rate)
    revenue = (dispatched - returned) * discounted_price
    total_revenue += revenue
    expected_stock = stock - dispatched + returned
    discrepancy = actual_stock - expected_stock
    products.append({
        "name": name,
        "revenue": revenue,
        "expected": expected_stock,
        "actual": actual_stock,
        "discrepancy": discrepancy
    })
else:
    print("\n--- E-COMMERCE AUDIT REPORT ---")
    print("Total Net Revenue: Rs.", round(total_revenue, 2))
    for p in products:
        print("\nProduct:", p["name"])
        print("Net Revenue: Rs.", round(p["revenue"], 2))
        print("Expected Stock:", p["expected"])
        print("Actual Stock:", p["actual"])

        if p["discrepancy"] == 0:
            print("Inventory: Matched")
        else:
            print("Discrepancy:", p["discrepancy"], "units")
    print("\n--- FINAL INVENTORY SUMMARY ---")
    for p in products:
        print(p["name"], ":", p["expected"], "units expected")

