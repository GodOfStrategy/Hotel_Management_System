class Room:
    def __init__(self, available_rooms, unavailable_rooms, room_prices):
        self.available_rooms = available_rooms
        self.unavailable_rooms = unavailable_rooms
        self.room_prices = room_prices  # Dictionary to store room numbers and their corresponding prices

    def add_rooms(self):
        room_number = int(input("Please enter the room number: "))
        room_price = int(input("Please enter the price of the room (per night): "))
        room_type = input("Please enter the room type: ")
        self.available_rooms.append(room_number)  # Add the room to the list of available rooms
        self.room_prices[room_number] = room_price  # Store room price in the dictionary
        print(f"Room with number {room_number} added for {room_price} per night with type {room_type}")
        print("Available rooms:", self.available_rooms)


class RoomBooking:
    def __init__(self, available_rooms, unavailable_rooms, room_prices):
        self.available_rooms = available_rooms
        self.unavailable_rooms = unavailable_rooms
        self.room_prices = room_prices  # Dictionary to store room prices

    def booked_rooms(self):
        booked_room = int(input("Enter the number of the room to book: "))
        if booked_room in self.available_rooms:
            duration = int(input("Please enter the duration of stay (days): "))
            self.available_rooms.remove(booked_room)  # Remove the booked room from available rooms
            self.unavailable_rooms.append(booked_room)  # Add it to unavailable rooms

            # Check if the room price exists in the room_prices dictionary
            if booked_room in self.room_prices:
                room_price = self.room_prices[booked_room]  # Get the price of the booked room
                total_bill = room_price * duration  # Calculate the total bill
                print(f"Room number {booked_room} booked for {duration} days with a bill of {total_bill}")
            else:
                print(f"Error: Price for room number {booked_room} not found.")
        else:
            print("Room not found or already booked.")

    def checkout_room(self):
        checkout_room = int(input("Enter the room number to check out: "))
        if checkout_room in self.unavailable_rooms:
            self.unavailable_rooms.remove(checkout_room)  # Remove from unavailable rooms
            self.available_rooms.append(checkout_room)  # Add it back to available rooms
            print(f"Room number {checkout_room} has been checked out and is now available.")
        else:
            print("Room not found or already available.")

    def display_room(self):
        print("Available rooms:")
        for index, room in enumerate(self.available_rooms):
            print(f"{index + 1}. Room number: {room}")

    def display_unroom(self):
        print("Unavailable (booked) rooms:")
        for index, room in enumerate(self.unavailable_rooms):
            print(f"{index + 1}. Room number: {room}")


# Creating shared data structures
available_rooms = []  # List to track available rooms
unavailable_rooms = []  # List to track booked rooms
room_prices = {}  # Dictionary to store room prices

# Creating objects that share the same data
object1 = Room(available_rooms, unavailable_rooms, room_prices)  # Shared data
object2 = RoomBooking(available_rooms, unavailable_rooms, room_prices)  # Shared data

# Main function to run the program
def main():
    while True:
        print("\n=== Welcome To Hotel Management System ===")
        print("To select your choice, press the corresponding number!")
        print("1. Add Room(s)")
        print("2. Book Room")
        print("3. Show Available Rooms")
        print("4. Show Unavailable (Booked) Rooms")
        print("5. Check Out Room")
        print("6. Exit")
        choice = int(input("Please Enter your corresponding Choice: "))

        if choice == 1:
            object1.add_rooms()
        elif choice == 2:
            object2.booked_rooms()
        elif choice == 3:
            object2.display_room()
        elif choice == 4:
            object2.display_unroom()
        elif choice == 5:
            object2.checkout_room()
        elif choice == 6:
            print("Thank you! See you next time!")
            break
        else:
            print("Invalid Input, please try again 😃😃.")


# Running the main function
main()