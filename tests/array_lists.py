"""
Data Structure: Python List (Array Example)
-------------------------------------------
Scenario: Weekly temperature recording and analysis.

Functions:
- week_temp(): Demonstrates basic list operations
  such as append, pop, replace, min, max, and mean.
"""

def week_temp():
    """Simulates weekly temperature operations."""
    
    # Create a list with 7 temperatures
    temperatures = [12.5, 14.2, 15.8, 13.9, 11.6, 10.2, 12.0]
    print("Temperatures of the week:", temperatures)

    # Calculate average temperature
    mean_temp = sum(temperatures) / len(temperatures)
    print("Average weekly temperature:", round(mean_temp, 1))

    # Access specific element (Wednesday)
    print("Wednesday's temperature is:", temperatures[3])

    # Display min and max
    print("Highest temperature:", max(temperatures))
    print("Lowest temperature:", min(temperatures))

    # Replace wrong value
    temperatures[2] = 15.0
    print("Corrected Thursday temperature:", temperatures[2])

    # Remove last temperature
    removed = temperatures.pop()
    print("Last day was removed:", removed)

    # Add a new temperature
    temperatures.append(18.2)
    print("One more day added:", temperatures)

    return temperatures  # Return final list for testing


# safety message when file runs directly
if __name__ == "__main__":
    print("Run tests/test_arrays_lists.py to see the demo.")
