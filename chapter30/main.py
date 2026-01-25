# chapter 30  Dictionaries: Removing and changing items
name={
    "name":"azhar",
    "age":24
}
print(name)
name["class"]=34

print("add the new item")
print(name)
print("deleted item")

del name["class"]
print(name)
print("update item")
name["name"]="Ali"
name["age"]=18
print(name)
