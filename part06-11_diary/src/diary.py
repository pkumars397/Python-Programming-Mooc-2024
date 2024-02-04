# Write your solution here
while True:
  print("1 - add an entry, 2 - read entries, 0 - quit ")
  function=input('Function: ')
  
  if function=="1":
    entry=input("Diary entry: ")
    with open("diary.txt","a") as dairy_file:
        dairy_file.write(entry+"\n")
    print("Diary saved\n")
  elif function=="2":
    print("Entries: \n")
    with open("diary.txt") as dairy_file:
        for line in dairy_file:
            line=line.strip()
            print(line)
  else:
    print("Bye now!")
    break