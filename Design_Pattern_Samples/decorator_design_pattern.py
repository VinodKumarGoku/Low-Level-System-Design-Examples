from abc import ABC, abstractmethod

# Base Elevator Interface
class Elevator(ABC):
    def __init__(self):
        self.utilities = []

    def add_utility(self, utility):
        """Add a utility to the elevator."""
        self.utilities.append(utility)

    def operate(self):
        """Operate the elevator and its utilities."""
        self.run_elevator()
        for utility in self.utilities:
            utility.perform_action()

    @abstractmethod
    def run_elevator(self):
        """Core elevator functionality."""
        pass


# Concrete Implementation of Elevator
class BasicElevator(Elevator):
    def run_elevator(self):
        # Core functionality of the elevator
        return "Elevator is moving."

# Abstract Utility Class
class Utility(ABC):
    @abstractmethod
    def perform_action(self):
        """Action performed by the utility."""
        pass

# Concrete Utility Classes
class Fan(Utility):
    def __init__(self, speed=1):
        self.speed = speed

    def perform_action(self):
        # Fan functionality logic
        return f"Fan is running at speed {self.speed}."

class AC(Utility):
    def __init__(self, temperature=24):
        self.temperature = temperature

    def perform_action(self):
        # AC functionality logic
        return f"AC is maintaining temperature at {self.temperature}°C."

class Light(Utility):
    def __init__(self, brightness=5):
        self.brightness = brightness

    def perform_action(self):
        # Light functionality logic
        return f"Lights are set to brightness level {self.brightness}."

class Music(Utility):
    def __init__(self, song="Default Tune"):
        self.song = song

    def perform_action(self):
        # Music functionality logic
        return f"Playing music: {self.song}."

# Assemble Elevator with Utilities
if __name__ == "__main__":
    # Create a basic elevator
    elevator = BasicElevator()

    # Add utilities
    elevator.add_utility(Fan(speed=3))
    elevator.add_utility(AC(temperature=22))
    elevator.add_utility(Light(brightness=7))
    elevator.add_utility(Music(song="Classical Symphony"))

    # Operate elevator with utilities
    actions = [elevator.run_elevator()]  # Start with elevator's core action
    actions.extend([utility.perform_action() for utility in elevator.utilities])

    # Return combined results
    for action in actions:
        print(action)  # Replace with logging or any output method
