# Write your solution here
def filter_solutions():
    with open("solutions.csv") as file:
        for line in file:
            parts=line.split(";")
            # print(parts)
            op=0
            if parts[1][1]=="+":
               op=parts[1][0]+parts[1][2]
            elif parts[1][1]=="-":
                op=parts[1][0]+parts[1][2]
            print(op)
                
            
            
            
if __name__=="__main__":
    filter_solutions()