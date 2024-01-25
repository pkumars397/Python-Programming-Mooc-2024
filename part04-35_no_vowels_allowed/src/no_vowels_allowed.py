# Write your solution here
def no_vowels(s:str)->str:
    vowels=["a","e","i","o","u"]
    newS=s
    for item in s:
        if item in vowels:
            newS=newS.replace(item,"")
    return newS;
    