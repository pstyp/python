teams_file=open("teams.txt", 'r')
lines=""
for i in range(5):
    if i==0:
        teams_file.readline()
    else:
        lines+=teams_file.readline()
teams_file.close()

teams_file=open("teams.txt", 'w')
teams_file.write("This is a new line \n")
teams_file.write(lines)
teams_file.close()