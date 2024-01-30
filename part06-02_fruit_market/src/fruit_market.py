# write your solution here
def read_fruits():
    fruit_dict={}
    with open("./src/fruits.csv") as fruit_file:
        for fruit in fruit_file:
           fruit=fruit.replace("\n",'')
           fruit=fruit.split(";")
           fruit_dict[fruit[0]]=float(fruit[1])
        #    print(fruit_dict)
    return fruit_dict
            
            
# if __name__=="__main__":
#     read_fruits()