print("welcome to my computer quizz")

playing = input("Do you want to play ? ")

if playing.lower() != "yes":
    quit()
print("oky")
score = 0

answer = input("what does cpu stand for ? ")
if answer.lower() == "Central processing unit":
    print("CXorrect!!")
    score += 1
else:
    print("Incorrect!!!")   

answer = input(" what is gpu ? ")
if answer.lower() == "graphics processing unit":
    print("CXorrect!!")
else:
    print("Incorrect!!!") 
    score += 1

answer = input("ram? ")
if answer.lower() == "random access memmory":
    print("CXorrect!!")
else:
    print("Incorrect!!!") 
    score += 1

answer = input(" atm? ")
if answer.lower() == "atomated telling mechine":
    print("CXorrect!!")
else:
    print("Incorrect!!!")             
    score += 1
print("You got " + str(score) + "questions correct!!")    
print("You got " + str((score/4)* 100) + "%") 