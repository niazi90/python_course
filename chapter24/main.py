#  chapter 24 changing case
name="Azhar"
# lowecase
name=name.lower()
print(name)

# uppar case
name="azhar"
name=name.upper()

# title first letter is capatilized
name=name.title()
print(name)


cleanest_cities = ["karachi", "mianwali","islamabad"]
city_to_check = input("Enter your city: ")
city_to_check = city_to_check.lower()
for a_clean_city in cleanest_cities:
  if city_to_check == a_clean_city:
   print("It's one of the cleanest cities")
   break
  else:
   print("error")