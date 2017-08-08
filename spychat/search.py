n=int(raw_input("enter the size of list"))
print n
li=[]
for i in range(0,n):
    p=int(raw_input("enter the no"))
    li.append(p)

k=int(raw_input("no to be searched"))

for i in range(n):
    if(li[i]==k):
        print "element found"
    else:
        print "not find"