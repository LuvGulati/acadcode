first=raw_input("enter the first name")
last=raw_input("enter the last no")
rlast=rev(last)

i=0

def rev(str):
    n = len(str) - 1
    for n in (range(n,-1,-1)) :

        k=k+str[n]

    return k

print (rev(last)+" "+rev(first))