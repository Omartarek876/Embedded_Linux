players = ["Alice", "Bob", "Charlie", "Diana", "Eve"]

with open("file.txt" , "w") as mylist : 
    mylist.write(" ".join(players))  

with open("file.txt" , "r") as myfile : 
    print(myfile.read())
