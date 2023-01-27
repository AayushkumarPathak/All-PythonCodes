file = open("Story.txt",'r')

# print(file.readlines())
count = 0
lines = file.readlines()
for line in lines:
    count+=1
    print("lines{}:{}".format(count,line.strip()))



file.close()