"""
PROBLEM STATEMENT:
Given a list of numbers and a number k, return whether any two numbers from the list add up to k.
For example, given [10, 15, 3, 7] and k of 17, return true since 10 + 7 is 17.

Bonus: Can you do this in one pass?
"""
def is_sum_in_list(list_of_numbers, k):
    # Brute force.
    for outer_loop_idx in range(len(list_of_numbers)):
        number1 = list_of_numbers[outer_loop_idx]
        for inner_loop_idx in range(outer_loop_idx + 1, len(list_of_numbers)):
            number2 = list_of_numbers[inner_loop_idx]
            if number1 + number2 == k:
                return True
    return False