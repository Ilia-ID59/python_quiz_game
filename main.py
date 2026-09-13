print("welcome")

score = 0

answer_1 = input("what language are we using ? ") #pyhton
if answer_1.lower() == "puthon":
    print("bravo")
    score += 1


answer_2 = input("what command starts a git ? ")
if answer_2.lower() == "git init":
    print("bravo")
    score += 1

else:
    print("wrong")

print("you score is : ", score)        
