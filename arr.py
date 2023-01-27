'''
Q Take a array from pre-defined from and check each iteam of list under the array whether the element is odd or even and print
  separately in another arrays. 

'''
#Sample Test Cases:
#   arr=[[1,2,8,9,10,11,20,23,22,],[12,13,14,15,16]]
#   output_line1- The Even number iteams is- [2,8,10,20,22,12,14,16]
#   output_line2-  The Odd number iteams is- [1,9,11,23,13,15]
#   output_line3- [2,8,10,20,22,12,14,16,1,9,11,23,13,15]

arr=[[1,2,8,9,10,11,20,23,22,],
      [12,13,14,15,16]]

new_even=[]
new_odd =[]

for i in arr:
    for j in i:
        if j%2==0:
            
            new_even.append(j)
        elif j%2!=0:
            new_odd.append(j)
            
        else:
            continue
print("The Even number iteams is-",new_even)
print("The Odd number iteams is-",new_odd)
print(list(new_even+new_odd))
           
        






# l=[12,21,3,1,3,4,5]
# for i in l:
#     print(i,end=" ")




# print(arr[0])
# print(arr[0][2:8:2])

# print(arr[1][3:5])
