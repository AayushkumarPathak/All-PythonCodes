n=int(input("Enter the number"))
temp=str(n)
def hybrid(n):
    if n%n==0:
        if n%1==0:
            if temp[0::]==temp[::-1]:
                print("Hybrid number")
    else:
        print("Invalid")

hybrid(n)
        
   
