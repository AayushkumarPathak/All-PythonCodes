
# f = open('st.txt','w')

# for i in range(5):
#     name=input("JJ")
#     f.write(name)
# f.close()


# file = open('st.txt','w')
# for i in range(4):
#     des=input("Enter")
#     file.write(des)
#     file.write('\n')
# file.close()


op = open('st.txt','w')

l=[]
for i in range(3):
    name=input("Enter Your name")
    l.append(name+'\n')
op.writelines(l)
op.close()