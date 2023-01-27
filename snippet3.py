import pickle as p
# bi = open("names.dat","wb")
# l=['aayush','akash','chandan','sanjay','rohit']

# p.dump(l,bi)
# print("Inserted successfully")

#---Reading data from binary file--- 
file = open('names.dat','rb')
r = p.load(file)
print(r)


