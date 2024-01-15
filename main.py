print("The Love Calculator is calculating your score...")
name1 = input("What is your name? ")
name2 = input("What is their name? ") 
true_occurance_name1 = name1.upper().count("T") + name1.upper().count("R") + name1.upper().count("U") + name1.upper().count("E")
true_occurance_name2 = name2.upper().count("T") + name2.upper().count("R") + name2.upper().count("U") + name2.upper().count("E")
total_true = true_occurance_name1 + true_occurance_name2

love_occurance_name1 = name1.upper().count("L") + name1.upper().count("O") + name1.upper().count("V") + name1.upper().count("E")
love_occurance_name2 = name2.upper().count("L") + name2.upper().count("O") + name2.upper().count("V") + name2.upper().count("E")
total_love = love_occurance_name1 + love_occurance_name2

score = str(total_true) + str(total_love)
score = int(score)
if score < 10 or score > 90:
  print(f"Your score is {score}, you go together like coke and mentos.")
elif score >=40 and score <= 50:
  print(f"Your score is {score}, you are alright together.")
else:
  print(f"Your score is {score}.")