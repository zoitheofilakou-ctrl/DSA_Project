# test_arrays_lists.py
# ----------------------------------------------------------
# Test file for week_temp() from arrays_lists.py
# This test checks all key operations performed on the list:
# - calculating mean
# - replacing a value
# - removing the last element
# - appending a new element
# ----------------------------------------------------------

import sys, os
# Step 1: Allow Python to see the parent directory
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

# Step 2: Import the function to test
from data_structures.arrays_lists import week_temp

print("\n=== TESTING: Weekly Temperatures (List Example) ===")

# Step 3: Run the function
# It will print details and return the final list
result = week_temp()

# Step 4: Check if we got a list
if isinstance(result, list):
    print("The function returned a list.")
else:
    print("The function did NOT return a list.")

# Step 5: Verify mean calculation (average temperature)
# We can quickly calculate what it *should* be
expected_original = [12.5, 14.2, 15.8, 13.9, 11.6, 10.2, 12.0]
expected_mean = round(sum(expected_original) / len(expected_original))
print(f"Expected mean (approx.): {expected_mean}")

# Step 6: Check that the replaced temperature (index 2) is now 15.0
if abs(result[2] - 15.0) < 0.01:
    print("Replace operation worked correctly (index 2 is now 15.0).")
else:
    print(f"Replace failed. Found {result[2]} instead of 15.0.")

# Step 7: Check that the removed value (12.0) is not in the final list
if 12.0 not in result:
    print("Remove operation worked correctly (12.0 removed).")
else:
    print("Remove seems to have failed (12.0 still in list).")

# Step 8: Check that 18.2 was added at the end
if result[-1] == 18.2:
    print("Append operation worked correctly (18.2 added).")
else:
    print("Append failed. Last element is:", result[-1])

# Step 9: Final check on list length (should still be 7)
if len(result) == 7:
    print("Final list length is correct (7 elements).")
else:
    print("Final list length incorrect:", len(result))

# Step 10: Print final list for confirmation
print("\nFinal list of temperatures:", result)
print("\nAll list operations tested successfully!\n")
