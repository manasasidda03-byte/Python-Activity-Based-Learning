registrations = ["101", "102", "103", "104", "105", "106"]
seats = [[None, None, None],
         [None, None, None]]
entered = []
duplicates = []
invalid = []
n = int(input("Enter number of tickets to check: "))
for i in range(n):
    ticket = input("Enter registration ID: ")
    if ticket not in registrations:
        invalid.append(ticket)
    elif ticket in entered:
        duplicates.append(ticket)
    else:
        entered.append(ticket)
index = 0
for row in range(2):
    for col in range(3):
        if index < len(entered):
            seats[row][col] = entered[index]
            index += 1
available = 6 - len(entered)
print("\n--- EVENT SEATING REPORT ---")
print("Seat Assignments:")
for i, row in enumerate(seats, start=1):
    print("Row", i, ":", row)
print("Valid Entries:", len(entered))
print("Duplicate Entries:", duplicates)
print("Invalid Tickets:", invalid)
print("Available Seats:", available)

