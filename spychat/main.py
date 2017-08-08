str=raw_input("enter the string")
i=0
n=len(str)-1
print n

for i in range(n/2):
    if str[i]==str[n]  :
        n-1

    else:
        print"not palindrome"
        break
