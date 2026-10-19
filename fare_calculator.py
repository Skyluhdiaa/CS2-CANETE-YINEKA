V1
# Travel Fare Calculator
FARE_RATE = 14

name = input("Enter passenger name: ")
distance = float(input("Enter distance (km): "))
passengers = int(input("Enter number of passengers: "))

total_fare = distance * FARE_RATE * passengers

print("\nPassenger:", name)
print("Total Fare: PHP", round(total_fare, 2))

# Validation rules
# 1. Passenger name -- Must not be empty
# 2. Distance -- Number greater than 0
# 3. Passengers -- Positive whole number

V2

FARE_RATE = 14

name = input("Enter passenger name: ")
if name.strip() == "":
    name = input("Error: Name cannot be empty. Please re-enter passenger name: ")

distance = float(input("Enter distance (km): "))
if distance <= 0:
    distance = float(input("Error: Distance must be greater than 0. Please re-enter distance (km): "))


passengers = int(input("Enter number of passengers: "))
if passengers <= 0:
    passengers = int(input("Error: Must be a positive whole number. Please re-enter number of passengers: "))


total_fare = distance * FARE_RATE * passengers

print("Passenger:", name)
print("Total Fare: PHP", round(total_fare, 2))
