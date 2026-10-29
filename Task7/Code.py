n = int(input("Enter number of registrations: "))
participants = []
duplicates = []
for i in range(n):
    reg_id = input("Enter registration ID: ")
    if reg_id in participants:
        duplicates.append(reg_id)
    else:
        participants.append(reg_id)
fee = 500
registration_income = len(participants) * fee
s = int(input("Enter number of sponsorships: "))
sponsorship = 0
for i in range(s):
    sponsorship += float(input("Enter sponsorship amount: "))
e = int(input("Enter number of expenses: "))
expenses = 0
for i in range(e):
    expenses += float(input("Enter expense amount: "))
total_income = registration_income + sponsorship
balance = total_income - expenses
print("\n--- FESTIVAL AUDIT REPORT ---")
print("Valid Participants:", len(participants))
print("Duplicate Registrations:", duplicates)
print("Registration Income: Rs.", registration_income)
print("Sponsorship Contributions: Rs.", sponsorship)
print("Total Income: Rs.", total_income)
print("Total Expenses: Rs.", expenses)
print("Final Financial Balance: Rs.", balance)
if balance > 0:
    print("Status: Profit")
elif balance < 0:
    print("Status: Loss")
else:
    print("Status: Break-even")
