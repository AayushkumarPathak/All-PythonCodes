""" list=[10,20,30]
print(list)
print(type(list))

#index  0  1  2  3   4       5
list1=[10,20,30,40,'apples','mango']
print(list1)
print(type(list1))

print(list1[0])
print(list1[4])

list2=[10,20,30,40,True,'orange']
print(list2) """


#--------------------------
#creting  a list through costructor
#list3=list((12,13,14,15))
#print(list3)
#----------------------------

#access iteams of a list
""" listOne=[10,20,30,40,50,60,70]
print(listOne[2:5])
print(listOne[:4])
print(listOne[2:]) """

#Modify list by index
""" listOne[0]=12
listOne[4]='hello'
print(listOne) """

""" #Change a range of list iteams
listOne[1:3]=['hi','bye']
print(listOne) """


#adding element in list 
#insert() iteams
listX=[10,20,30]
listX.insert(2,55)
print(listX)


#append()
listX.append(60)
listX.append(65)
listX.append(70)
print(listX)


# extend()
listY=[75,80,85]
listX.extend(listY)
print(listX)

tup=(90,100)
listX.extend(tup)
print(listX)


#Remove a specified element from the list.
#remove()
mylist = ['jhon','peter','raj']
mylist.remove('peter')
print(mylist)


#Remove iteam from a specified index.
#pop()
mylist = ['jhon','peter','raj','Ajay']
mylist.pop(3)
print(mylist)

''''delete()'''
mylist.delete


