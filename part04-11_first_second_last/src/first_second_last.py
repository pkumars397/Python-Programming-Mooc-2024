# Write your solution here
def first_word(sentence):
    str='';
    i=0
    while sentence[i]!=" ":
        str+=sentence[i]
        i+=1
    return str;
def second_word(sentence):
    countspaces=0;
    i=0
    while i<len(sentence):
        if sentence[i]==" ":
            countspaces+=1
        i+=1
    if countspaces>1:
        str=''
        i=0
        while sentence[i]!=" ":
              i+=1
        i=i+1
        while sentence[i]!=" ":
            str+=sentence[i]
            i+=1
        return str;
    else:
        return last_word(sentence)
def last_word(sentence:str)->str:
    str=''
    i=len(sentence)-1
    while sentence[i]!=" ":
        i-=1
    i=i+1;
    while i!=len(sentence):
        str+=sentence[i]
        i+=1
    return str;
    
# You can test your function by calling it within the following block
if __name__ == "__main__":
    sentence = "once programmer"
    print(first_word(sentence))
    print(second_word(sentence))
    print(last_word(sentence))