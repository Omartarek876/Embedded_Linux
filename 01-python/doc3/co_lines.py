f = open("file.txt" , "r") 
lines = f.readlines()
print(len(lines)) 
f.close()

f = open("file.txt" , "r") 
words = f.read()
print(len(words.split()))
f.close()
