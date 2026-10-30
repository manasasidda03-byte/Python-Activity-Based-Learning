teams = []
n = int(input("Enter number of teams: "))
min_size = 2
max_size = 4
for i in range(n):
    print("\nTeam", i + 1)
    name = input("Enter team name: ")
    members = int(input("Enter number of members: "))
    if members < min_size or members > max_size:
        print("Invalid team size! Team rejected.")
        continue
    r1 = int(input("Enter Round 1 score: "))
    r2 = int(input("Enter Round 2 score: "))
    r3 = int(input("Enter Round 3 score: "))
    total = r1 + r2 + r3
    teams.append({
        "name": name,
        "members": members,
        "total": total,
        "final": r3
    })
teams.sort(key=lambda t: (t["total"], t["final"]), reverse=True)
print("\n--- Hackathon Rankings ---")
for rank, team in enumerate(teams, start=1):
    print(rank, team["name"],
          "| Members:", team["members"],
          "| Total Score:", team["total"],
          "| Final Round:", team["final"])

       
                
