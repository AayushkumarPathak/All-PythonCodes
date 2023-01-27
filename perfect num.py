#perfect number
# num = int(input("Enter"))

# def perfect(num):
#     sum_n=0

#     for i in range(1,num):
#         if num%i==0:
#             sum_n+=i
        
#     if sum_n==num:
#         print("Perfect number")
#     else:
#         print("Not a perfect number")
# perfect(num)


#Armstrong number

# n = int(input("Enter the number"))
# sum = 0
# temp = n
# while temp>0:
#     dig = temp%10
#     sum+=dig**3
#     temp//=10

# if n==sum:
#     print("Armstrong number")
# else:
#     print("Not armstrong number")


def factorial(n):
    if (n==1 or n==0):
        return 1
    else:
        return n*factorial(n-1)

n = int(input("Enter to find factorial"))
print(factorial(n))