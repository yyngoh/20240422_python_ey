
person = {
    "fn": "joh",
    "ln": "jones",
    "age": 35}

print(person)

print (person["ln"])
print (person["fn"])
print (person["age"])

person["age"] = 45

person["race"] = "hispanic"

for key in person:
    print(key, person[key])
    
try:

    print (person["home"])
    
except KeyError:
    print("keyerrro")
    
print(person.get("home", "N/A"))