# Challenge of the day 03/06/20

#could be dictionary=dict()

dictionary = {}

def createdic(n):
    for i in range(1,n+1):
        dictionary[i] = i * i
    return dictionary

n = int(input("What's your number? "))

print(createdic(n))
