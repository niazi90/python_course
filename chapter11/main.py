#  chapter 11 else and elif statements
# question 10 If a equals b, display "ok". If not, then if c equals d, display "ok". If both tests fail, display "failed".
a=4
b=5
c=3
d=3

if (a==b):
    print("ok a equal b")
elif (c==d):
    print("ok c equal d")
else:
    print("failed")

# question 11
if "dog" == "cat":
  print ("That's crazy")
# On the next two lines, display "wrong" if the condition isn't met.
else:
    print("wrong")

if "dog" == "cat":
  proposition = "crazy"
# On the next two lines, if the condition above isn't met,
# test whether "cat" is equal to "cat"
# If so, display "ok"
elif "cat" == "cat":
    print("ok cat equal cat")