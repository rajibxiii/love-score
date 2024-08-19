
### Love Score Calculator

print("The Love Calculator is calculating your score...")
name1 = input() # What is your name?
name2 = input() # What is their name?

name1 = name1.lower()
name2 = name2.lower()

combinedName = name1 + name2

t = combinedName.count("t")
r = combinedName.count("r")
u = combinedName.count("u")
e = combinedName.count("e")

l = combinedName.count("l")
o = combinedName.count("o")
v = combinedName.count("v")
e = combinedName.count("e")

count1 = t+r+u+e
count2 = l+o+v+e

score = int(str(count1) + str(count2))

if score <10 or score >90:
    print (f"Your score is {score}, you go together like coke and mentos.")
elif score >= 40 and score  <=50:
    print (f"Your score is {score}, you are alright together.")
else: 
    print (f"Your score is {score}.")