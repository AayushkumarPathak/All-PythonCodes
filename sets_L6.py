#sets
#it is also used to store multiple iteams in a single variable
#here we use curly bracket to denote a set
#sets are unchangeable,unordered,unindexed and only can store unique
#values i.e no duplicates are allowed 
#still we can add and remove new iteams
#it can have multiple datatypes

myset={10,20,30,40,10,20}
print(myset)
print(len(myset))

myset1={'hello',10,20}
print(myset1)
#access the iteams in a set
#we cannot use index or a key to access iteams as they are unordered

myset1.add(5)
myset1.add("hi")
print(myset)
#add iteams from one set to another
set1={10,20,30,40}
set2={50,60}
set1.update(set2)
print(set1)