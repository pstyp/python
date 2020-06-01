#Grade Caluculator

print("Welcome to to Grade Calucaltor")

chemistry_mark=int(input("Please enter your chemistery mark: "))
maths_mark=int(input("Please enter your chemistery mark: "))
physics_mark=int(input("Please enter your chemistery mark: "))

final_score=((chemistry_mark+maths_mark+chemistry_mark)/300)*100

print("Your final score is "," ", final_score)

if final_score>=70:
    print("Your mark is A.")
elif final_score>=60:
    print("Your mark is B.")
elif final_score>=50:
    print("Your mark is C.")
elif final_score>=40:
    print("Your mark is D.")
else:
    print("You have failed.")