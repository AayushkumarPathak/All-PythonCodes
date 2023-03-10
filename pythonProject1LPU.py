# A Group project by Team Happiness(Serena Sinha, Aayush Kumar Pathak, Lakshay )
''' SECTION - KOC09'''


# Function to print the name of student who
# stood first after updation in rank
def nameRank(names, marks, updates, n):
	
	# list for student
	x = [[0 for j in range(3)] for i in range(n)]
	for i in range(n):
		
		# Store the name of the student
		x[i][0] = names[i]
		
		# Update the marks of the student
		x[i][1]= marks[i] + updates[i]
		
		# Store the current rank of the student
		x[i][2] = i + 1
		
	highest = x[0]
	for j in range(1, n):
		if (x[j][1] >= highest[1]):
			highest = x[j]
			
	# Print the name and jump in rank
	print("Name: ", highest[0], ", Jump: ",abs(highest[2] - 1), sep="")

#___main___

# Names of the students
names= ["Aayush", "Serena", "Lakshay"]

# Marks of the students
marks = [80, 79, 90]

# Updates that are to be done
updates = [0, 5, -9]

# Number of students
n = len(marks)

nameRank(names, marks, updates, n)

 
