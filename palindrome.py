name = str(input("Enter the string :"))

if name[0::] == name[::-1]:
    print("Palindrome ")
else:
    print("Not pallindrome ")