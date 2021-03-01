# Write classes for the following class hierarchy:
#
#  [Vehicle]->[FlightVehicle]->[Starship]
#      |                |
#      v                v
# [GroundVehicle]      [Airplane]
#   |       |
#   v       v
# [Car]  [Motorcycle]
#
# Each class can simply "pass" for its body. The exercise is about setting up
# the hierarchy.
#
# e.g.
#
# class Whatever:
#     pass
#
# Put a comment noting which class is the base class

# Note - I put Vehicle as the base class because it would be redundant to state the parent class since it says it in
# the definition


class Vehicle:
    pass


class FlightVehicle(Vehicle):
    # Vehicle is the base class
    pass


class Starship(FlightVehicle):
    # Vehicle is the base class
    pass


class Airplane(FlightVehicle):
    # Vehicle is the base class
    pass


class GroundVehicle(Vehicle):
    # Vehicle is the base class
    pass


class Car(GroundVehicle):
    # Vehicle is the base class
    pass


class Motorcycle(GroundVehicle):
    # Vehicle is the base class
    pass
