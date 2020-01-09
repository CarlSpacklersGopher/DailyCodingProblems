"""
PROBLEM STATEMENT:
Given a list of numbers and a number k, return whether any two numbers from the list add up to k.
For example, given [10, 15, 3, 7] and k of 17, return true since 10 + 7 is 17.

Bonus: Can you do this in one pass?
"""

def is_sum_in_list(list_of_numbers, k):
    # Can store all numbers already visited and look them up from this set in constant time.
    numbers_already_visited = set()
    for number in list_of_numbers:
        # number1 + number2 = k
        # Since we have number1 and k, we can calculate the necessary value of number2.
        number2 = k - number
        if number2 in numbers_already_visited:
            # If we've already seen number2, current value of number + number2 = k
            return True

        numbers_already_visited.add(number) # Store in set for following iterations
    return False