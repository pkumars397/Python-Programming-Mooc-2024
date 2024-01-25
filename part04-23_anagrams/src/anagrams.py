# Write your solution here
def anagrams(str1:str,str2:str):
    str1=sorted(str1)
    str2=sorted(str2)
    if len(str2)!=len(str1):
        return False;
    else:
        for i in range(len(str2)):
            if str1[i]!=str2[i]:
                return False
        return True
            