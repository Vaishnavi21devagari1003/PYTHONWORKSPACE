# myFriends = {"Sandy": 25, "John": 20, "Jane": 22}

# print(myFriends.items())   
# print(myFriends.keys())    
# print(myFriends.values())  
# print(myFriends["Sandy"])  

# myFriends["Sandy"] = 30   
# print(myFriends.items())

# myFriends.update({"Sandy": 40}) 
# print(myFriends.items())

# # Removing items
# myFriends.pop("Sandy")     # Removes Sandy specifically
# print(myFriends.items())

# myFriends.popitem()        # Removes the last inserted item
# print(myFriends.items())

# del myFriends["John"]      # Another way to delete a specific key
# print(myFriends.items())


information = {"name": "Alice",
               "age": 28,
               "address": {"home": {"street": "123 Main St","city": "Wonderland","zip": "12345"},
                           "work": {"street": "456 Work Rd","city": "Worktown","zip": "67890"},
                           "natives":{ "street": "456 Work Rd","city": "Worktown","zip": "67890"}},
               "hobbies": ["reading", "traveling", "swimming"]}

print(information["name"])  
print(information["address"]["home"]["city"])
print(information["hobbies"][1])
print(information["address"]["natives"]["zip"])