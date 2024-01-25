# Write your solution here
def histogram(stri:str)->str:
    dict={};
    for i in stri:
        if i not in dict:
            dict[i]=1
        else:
            dict[i]+=1
    for key,val in dict.items():
        print(f"{key} {"*"*val}")