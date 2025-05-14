class Vehicle:
    def move(self):
        """Base method to be overridden."""
        raise NotImplementedError("Subclasses must implement this method.")

class Car(Vehicle):
    def move(self):
        print("Driving 🚗")

class Plane(Vehicle):
    def move(self):
        print("Flying ✈️")

class Bicycle(Vehicle):
    def move(self):
        print("Pedaling 🚲")

# Example usage
def make_vehicle_move(vehicle):
    vehicle.move()

# Create instances of each vehicle
my_car = Car()
my_plane = Plane()
my_bicycle = Bicycle()

# Call the move method for each vehicle
make_vehicle_move(my_car)      # Output: Driving 🚗
make_vehicle_move(my_plane)    # Output: Flying ✈️
make_vehicle_move(my_bicycle)  # Output: Pedaling 🚲
