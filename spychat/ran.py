import random
a=random.randint(0,9)

for i in range(0,10,1):

    c=raw_input("enter the no")
    if(c=="exit"):
        print "bye"
        exit()
    else:
      c=int(c)
      if(c==a):
         print "u r right"

      elif(c>a):
         print "too high "

      elif(c<a):
         print "low"
