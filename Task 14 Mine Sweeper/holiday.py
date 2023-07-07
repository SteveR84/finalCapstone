"""
Calculate holday costs INCLUDING plane, hotel and car rental.
Get 3 inputs.
1 - city_flight - choice of locations (make options) each has a different cost.
2 - num_nights - number of nights at hotel.
3 - rental_days - how many days to rent a car for.

next make finctions
hotel_cost is num_nights * cost per night (my choise)
plane_cost is city_flight --- hint == use if else statment to calculate
car_rental is rental_days * car cost (my choise)

make holiday_cost be the 3 functions together and print out in a readable way.
"""
# Variables
locations = { 1 :"London" , 2 : "Paris" , 3 : "Mexico" , 4 : "New York"}
prices = { 1 : 199 , 2 : 299 , 3 : 750 , 4 : 900} # More locations can be added this way
loop_counter = 1 # Count loops
car_price = 5 # Per Day
hotel_price = 8 # Per Night
car_days = 0 # Days for car


# Functions
def plane_cost(a): # Didnt need if/esle statments as using 2 dictonaries.
    flight = prices[a]
    return flight

def hotel_cost(b):
    hotel = (hotel_price * 10) * b
    return hotel

def car_rental(c):
    car = (car_price * 5) * c
    return car

print(f"Please choose your destination number from the following list:")
for i in locations:
    print(f"{loop_counter}\t{locations[i]} at £{prices[i]} return flight")
    loop_counter += 1
city_flight = int(input("--> ")) # Requested

print(f"You have chosen {locations[city_flight]} at a cost of £{plane_cost(city_flight)} return")

num_nights = int(input(f"Each night is £{hotel_cost(city_flight)}. How many night stay?\n")) # Requested

print(f"So thats {num_nights} nights in {locations[city_flight]}.")
print(f"Do you need to rent a car at £{car_rental(city_flight)} per day?")
need_car = input("Yes or No\n")

if need_car.lower() == "yes" or need_car.lower() == "y":
    rental_days = int(input("Please enter how many days:\n")) # Requested
else:
    rental_days = 0

holiday_cost = plane_cost(city_flight) + (rental_days * car_rental(city_flight)) + (num_nights * hotel_cost(city_flight))

print(f"£{plane_cost(city_flight)} for the flight to {locations[city_flight]}.")
print(f"£{num_nights * hotel_cost(city_flight)} for {num_nights} night stay.")
if need_car.lower() == "yes" or need_car.lower() == "y":
    print(f"£{rental_days * car_rental(city_flight)} for car rental.")
else:
    print("There is no car rented")
print(f"The cost for your trip to {locations[city_flight]} will be £{holiday_cost}")