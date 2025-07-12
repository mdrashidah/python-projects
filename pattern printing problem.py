#q1 pattern printing problem
''' n=3
  *
 ***   
*****
'''
n=int(input("enter the number of rows:"))
for i in range(1,n+1):
    print(" "*(n-i),end="")
    print("*"*(2*i-1),end="")
    print()
#q2 pattern printing problem
''' n=3
*
**
***
'''
n=int(input("enter the number of rows:"))
for i in range(1,n+1):
    print("*"*i,end="")
    print()
#q3 pattern printing problem
''' n=3
*****
***
*
'''
n=int(input("enter the number of rows:"))
for i in range (n,0,-1):
    print("*"*i,end="")
    print()
