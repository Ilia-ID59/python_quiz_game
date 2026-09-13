from question import questions

print("welcome")

score = 0

for item in questions:
    answer = input(item["questions"])

    if answer.lower() == item["answer"]:
        print("correct")
        score += 1

    else:
        print("wrong")    

print("you score is : ", score)        
