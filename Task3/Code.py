from datetime import datetime
from math import ceil
rates = {
    "two-wheeler": 20,
    "car": 40,
    "heavy": 60
}
daily_limits = {
    "two-wheeler": 200,
    "car": 400,
    "heavy": 600
}
try:
    vehicle = input("Enter vehicle type (two-wheeler/car/heavy): ").lower()
    entry = input("Enter entry date and time (YYYY-MM-DD HH:MM): ")
    exit_time = input("Enter exit date and time (YYYY-MM-DD HH:MM): ")
    if vehicle not in rates:
        print("Invalid vehicle category!")
    else:
        entry_time = datetime.strptime(entry, "%Y-%m-%d %H:%M")
        exit_datetime = datetime.strptime(exit_time, "%Y-%m-%d %H:%M")
        if exit_datetime <= entry_time:
            print("Invalid time! Exit must be after entry.")
        else:
            minutes = (exit_datetime - entry_time).total_seconds() / 60
            hours = ceil(minutes / 60)
            full_days = hours // 24
            remaining_hours = hours % 24
            rate = rates[vehicle]
            daily_limit = daily_limits[vehicle]
            fee = (full_days * daily_limit) + min(
                remaining_hours * rate, daily_limit
            )
            penalty = 100 if hours > 24 else 0
            total = fee + penalty
            print("\n--- PARKING BILL ---")
            print("Vehicle Type:", vehicle)
            print("Parking Duration:", hours, "hours")
            print("Parking Fee: Rs.", fee)
            print("Penalty: Rs.", penalty)
            print("Total Parking Fee: Rs.", total)
except ValueError:
    print("Invalid date or time format!")


