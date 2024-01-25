# Write your solution here
first_letter = input("1st letter: ")
second_letter = input("2nd letter: ")
third_letter = input("3rd letter: ")

# Compare the letters to find the middle one
if first_letter < second_letter < third_letter or third_letter < second_letter < first_letter:
    middle_letter = second_letter
elif second_letter < first_letter < third_letter or third_letter < first_letter < second_letter:
    middle_letter = first_letter
else:
    middle_letter = third_letter

# Print the letter in the middle
print(f"The letter in the middle is {middle_letter}")