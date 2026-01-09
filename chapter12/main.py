# chapter 12 Testing sets of conditions
a = 10
b = 20  
if a < b and b > 15:
    print("Both conditions are true")
if a > b or b > 15:
    print("At least one condition is true")
if not a > b:
    print("Condition is false, so this is true")