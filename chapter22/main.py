# chapter 22 for loop nested 

chosen_letter = "b"
letter_list = ["a", "b", "c", "d", "e", "f"]
for a_letter in letter_list:
  if a_letter == chosen_letter:
    print("It's a match. letter " + a_letter)
    break