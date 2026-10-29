n = int(input("Enter number of buildings: "))
buildings = []
for i in range(n):
    name = input("\nEnter building name: ")
    e1 = float(input("Day 1 electricity units: "))
    e2 = float(input("Day 2 electricity units: "))
    w1 = float(input("Day 1 water litres: "))
    w2 = float(input("Day 2 water litres: "))
    if min(e1, e2, w1, w2) < 0:
        print("Invalid consumption values!")
        break
    cost1 = e1 * 8 + w1 * 2
    cost2 = e2 * 8 + w2 * 2
    change = ((cost2 - cost1) / cost1 * 100
              if cost1 != 0 else 0)
    score = e2 + w2 / 100
    excessive = e2 > 100 or w2 > 500
    buildings.append({
        "name": name,
        "cost": cost2,
        "change": change,
        "score": score,
        "excessive": excessive
    })
else:
    print("\n--- CAMPUS AUDIT REPORT ---")
    for b in buildings:
        print("\nBuilding:", b["name"])
        print("Day 2 Total Cost: Rs.", round(b["cost"], 2))
        print("Cost Change:", round(b["change"], 2), "%")
        print("Score:", round(b["score"], 2))
        print("Consumption:",
              "Excessive" if b["excessive"] else "Normal")
    buildings.sort(key=lambda b: b["score"], reverse=True)
    print("\n--- BUILDING RANKING ---")
    for rank, b in enumerate(buildings, start=1):
        print(rank, b["name"], "- Score:", round(b["score"], 2))

