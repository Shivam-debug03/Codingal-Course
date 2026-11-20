import random

print("TRAIN TICKET COUNTER")

passenger_name = input("Enter your name: ")
number_of_passengers = int(input("Enter the number of people (passengers): "))
ticket_types = [
    ("Sleeper", 500),
    ("AC", 1200),
    ("Non-AC", 300)
]
coach_capacity = 72

if number_of_passengers < 1 or number_of_passengers > coach_capacity:
    print("Please enter between 1 and", coach_capacity, "passengers to book seats together.")
else:
    section, ticket_price = random.choice(ticket_types)
    total_price = number_of_passengers * ticket_price
    first_seat = random.randint(1, coach_capacity - number_of_passengers + 1)

    print("\nTicket Booking Details")
    print("Name:", passenger_name)
    print("Number of people:", number_of_passengers)
    print("Section:", section)
    print("Price per ticket: Rs", ticket_price)
    print("Total price: Rs", total_price)
    print("\nSeats together:")
    for passenger_number in range(1, number_of_passengers + 1):
        seat_number = first_seat + passenger_number - 1
        print("Passenger", passenger_number, "- Seat", seat_number)

    print("Your train tickets are booked!")