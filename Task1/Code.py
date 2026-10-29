consultation = float(input("Enter consultation charges: ₹"))
diagnostic = float(input("Enter diagnostic charges: ₹"))
treatment = float(input("Enter treatment charges: ₹"))
if consultation < 0 or diagnostic < 0 or treatment < 0:
    print("Invalid charges! Charges cannot be negative.")
else:
    total_bill = consultation + diagnostic + treatment
    if total_bill >= 10000:
        concession = total_bill * 0.10
        concession = min(concession, 2000)
    else:
        concession = 0
    final_bill = total_bill - concession
    if final_bill < 5000:
        category = "Low Payment"
    elif final_bill <= 15000:
        category = "Medium Payment"
    else:
        category = "High Payment"
    print("\n----- HOSPITAL BILL -----")
    print(f"Consultation Charges: ₹{consultation:.2f}")
    print(f"Diagnostic Charges:   ₹{diagnostic:.2f}")
    print(f"Treatment Charges:    ₹{treatment:.2f}")
    print(f"Total Bill:           ₹{total_bill:.2f}")
    print(f"Concession:           ₹{concession:.2f}")
    print(f"Final Payable Amount: ₹{final_bill:.2f}")
    print(f"Patient Classification: {category}")

