# Write your solution here
def same_chars(char,i1,i2):
    if i1>=len(char) or i2>=len(char):
        return False;
    elif char[i1]==char[i2]:
        return True;
    else:
        return False;
# You can test your function by calling it within the following block
if __name__ == "__main__":
    print(same_chars("coder", 1, 2))