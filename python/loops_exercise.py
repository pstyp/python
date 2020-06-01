numberofloops=int(input('Please enter the number of loops: '))
limit=int(input('Please enter the limit: '))
for i in range (1, 101):
    print(i,i**2)
    if i**2>=numberofloops:
        break
    if i==limit:
        break

      

    

