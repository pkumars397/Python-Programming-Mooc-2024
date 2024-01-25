# Write your solution here
# You can test your function by calling it within the following block
if __name__ == "__main__":
    hash_square(5)
def hash_square(times):
    str="#"*times
    while times>0:
        print(str)
        times-=1