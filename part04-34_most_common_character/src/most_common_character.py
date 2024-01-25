# Write your solution here
def most_common_character(arr:list)->list:
    max_freq=0
    max_freq_char=""
    for item in arr:
        if arr.count(item)>max_freq:
            max_freq=arr.count(item)
            max_freq_char=item
    return max_freq_char