# Write your solution here
def dict_of_numbers():
    dix={1:"one",2:"two",3:"three",4:"four",5:"five",6:"six",7:"seven",8:"eight",9:"nine",10:"ten",11:"eleven",12:"twelve",13:"thirteen",14:"fourteen",15:"fifteen",16:"sixteen",17:"seventeen",18:"eighteen",19:"nineteen",20:"twenty",30:"thirty",40:"forty",50:"fifty",60:"sixty",70:"seventy",80:"eighty",90:"ninety",0:"zero"}
    for i in range(1,100):
        if i not in dix:
            str=dix[i-i%10]+"-"+dix[i%10]
            dix[i]=str
    return dix