# arrays_lists.py
# Dynamic Array implementation for storing and processing elements
# Author: Zoi Theofilakou | Turku University of Applied Sciences | Fall 2025

class DynamicArray:
    """A simple implementation of a dynamic array using Python list."""

    def __init__(self):
        self.temperatures = [12.5, 14.2, 15.8, 13.9, 11.6, 10.2, 12.0]

    def display(self):
        """Display all elements."""
        return self.temperatures

    def mean(self):
        """Return the average temperature."""
        return sum(self.temperatures) / len(self.temperatures)

    def get(self, index):
        """Return element at given index."""
        return self.temperatures[index]

    def update(self, index, new_value):
        """Update a specific temperature."""
        self.temperatures[index] = new_value

    def remove_last(self):
        """Remove and return last element."""
        return self.temperatures.pop()

    def append(self, value):
        """Add a new temperature."""
        self.temperatures.append(value)

    def get_all(self):
        """Return entire list."""
        return self.temperatures


if __name__ == "__main__":
    print("Run tests/test_arrays_lists.py to see the demo.")
