from question import questions

name = input("whats your name ? ")

print("welcome")

score = 0

for item in questions:
    answer = input(item["questions"])

    if answer.lower() == item["answer"]:
        print("correct")
        score += 1

    else:
        print("wrong")    

print("you score is : ", score, "out of ", len(questions))        

if score == len(questions):
    print("excellent job", name)
if score >= 2:
    print("good job", name)
else:
    print("leep praticing", name)    
    