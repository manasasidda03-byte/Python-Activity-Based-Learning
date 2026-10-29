roads = int(input("Enter number of roads: "))
intervals = int(input("Enter number of time intervals: "))
if roads <= 0 or intervals <= 0:
    print("Invalid number of roads or intervals.")
else:
    times = input("Enter time intervals separated by spaces: ").split()
    if len(times) != intervals:
        print("Error: Number of time intervals does not match.")
    else:
        traffic_data = {}
        capacities = {}
        for i in range(roads):
            name = input("\nEnter road name: ")
            capacity = int(input("Enter road capacity: "))
            if capacity <= 0:
                print("Invalid capacity!")
                break
            counts = list(map(int, input(
                "Enter vehicle counts for each interval: "
            ).split()))

            if len(counts) != intervals or min(counts) < 0:
                print("Invalid vehicle counts!")
                break
            capacities[name] = capacity
            traffic_data[name] = counts
        else:
            print("\n--- TRAFFIC ANALYSIS ---")
            totals = [
                sum(traffic_data[road][j] for road in traffic_data)
                for j in range(intervals)
            ]
            peak = totals.index(max(totals))
            print("Peak Traffic Period:", times[peak])
            for road, counts in traffic_data.items():
                capacity = capacities[road]
                maximum = max(counts)
                percentage = maximum / capacity * 100
                if percentage < 50:
                    level = "Low"
                elif percentage <= 80:
                    level = "Moderate"
                else:
                    level = "High"
                exceeded = any(c > capacity for c in counts)
                print("\nRoad:", road)
                print("Maximum Vehicles:", maximum)
                print("Congestion:", level)
                if exceeded:
                    print("Status: Capacity Exceeded")
                else:
                    print("Status: Within Capacity")

