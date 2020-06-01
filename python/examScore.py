def score(homework, assessment, final_exam):
    print(homework,"/50")
    print(assessment,"/50")
    print(final_exam,"/50")

def printname(name):
    return "Hello"+" "+name

name=input("What's your name? ")

yourname=printname(name)

print(yourname)

homework_score=int(input("Homework score: "))
assessment_score=int(input("Assessment score: "))
final_exam_score=int(input("Final exam score: "))

score(homework_score,assessment_score,final_exam_score)


