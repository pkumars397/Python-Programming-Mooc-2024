# Write your solution here
def invert(dictionary: dict):
    inverted_dict = {}
    for key, value in dictionary.items():
        inverted_dict[value] = key
    dictionary.clear()
    dictionary.update(inverted_dict)


def invert(dictionary: dict):
	copy = {}
	for key in dictionary:
		copy[key] = dictionary[key]
	for key in copy:
		del dictionary[key]
	for key in copy:
		dictionary[copy[key]] = key