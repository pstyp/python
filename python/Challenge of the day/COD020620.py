#Challenge of the day 02/06/20
def factorial(n):
    if n == 0:
        return 1
    else:
        return n*factorial(n-1)

    
n = int(input("Please input an integer: "))
answers=[]
answers.append(factorial(n))
print(answers)
