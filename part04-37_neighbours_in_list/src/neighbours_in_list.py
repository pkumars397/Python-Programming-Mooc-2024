# Write your solution here
def longest_series_of_neighbours(lst):
    max_length = 0
    current_length = 1

    for i in range(1, len(lst)):
        if abs(lst[i] - lst[i - 1]) == 1:
            current_length += 1
        else:
            max_length = max(max_length, current_length)
            current_length = 1

    # Check for the last sequence
    max_length = max(max_length, current_length)

    return max_length


