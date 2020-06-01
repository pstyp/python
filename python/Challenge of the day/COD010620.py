#Challenge of the Day (01/06/20)

listofnumbers=[]
for specialnumbers in range(2000, 3201):
    if (specialnumbers%7==0) and not (specialnumbers%5==0):
        listofnumbers.append(str(specialnumbers))
print("All numbers which are divisible by 7 but are not a multiple of 5, between 2000 and 3200: ")
print(','.join(listofnumbers))