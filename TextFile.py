# f = open("Student.txt",'w')
# f.write("Ram is a Good Friend\n")
# f.write("Akash is my Best friend\n\n\n")

f1 = open("emp.txt",'w')
lst = ['aayush\n','nitish\n','nikhil\n','abbhishek\n']
p = "ELEVATOR PITCH\n \n Hi my name is Aayush Kumar Pathak Persuing my Btch cse\n from lovely professional university jalahandar punjab india.\n I passoniate about computer programming\n "

p1 = "It is a long established fact that a reader will be\n distracted by the readable content of a page when looking at its\n layout. The point of using Lorem Ipsum is that it has a\n more-or-less normal distribution of letters, as opposed to using 'Content here, content here'\n, making it look like readable English.\n"

f1.writelines(lst)
f1.write(p)
f1.write(p1)

print(f1)








f1.close()