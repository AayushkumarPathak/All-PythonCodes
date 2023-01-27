import pickle as p

file = open('new1.dat','wb')
l=['aaayush','karan','probodh','dogesh']
l2=[1,2,3,4]
l.extend(l2)
print(l)
# p.dump(l,file)
# l1=[10,20,30]
# p.dump(l1,file)

# print(file)

# file=open('new1.dat','rb')

# d=p.load(file)
# print(d)
file.close()