n=int(raw_input("ente the value of n"))
sum=0
k=1
i=0
for i in range(n):
    if i==0:
        prev2=0
        print prev2
    elif i==1:
         prev1=1
         print prev1

    elif i>1:
        sum=prev1+prev2
        prev2 = prev1
        prev1=sum

        print sum





