import os , string 

if not os.path.exists("letters") : 
    os.makedirs("letter") 

for letter in string.ascii_uppercase : 
    with open("letter/" + letter + ".txt" , "w") as l : 
        l.writelines(letter*20)