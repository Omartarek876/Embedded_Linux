import os

# Access a specific environment list1iable
list1 = ['OneDrive','PyCharm' , 'TEMP' ] 

for var in list1 : 
    value = os.getenv(var)
    if value:
       print(f"The value of {var} is: {value}")
       print("****")
    else:
       print(f"{var} is not set.")


""" # You can also set environment list1iables for the current process
os.environ['NEW_list1IABLE'] = 'omar'
print(f"NEW_list1IABLE is set to: {os.getenv('NEW_list1IABLE')}")
 """ 