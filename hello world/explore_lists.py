from typing import Any


nums = [1,2,3,4,5,6]
letters = ["a","b","c"]

people: list[dict[str,Any]] =[
    {"name": "bob","age":23},
    {"name": "john","age":33},
    {"name": "harry","age":100}
    ]


for person in people:
    print(person)
    

print(people[1])

people.append({"name":"tom", "age":20})


for person in people:
    print(person)


print(people[1])   
