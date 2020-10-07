#Write a python program to print prime numbers between 0 to 501.

for x in range(1,501):
    for y in range(2,x):
        if(x % y==0):
            break
    else:
        print(x)
        
      
      *******************
#Write a python program to print EVEN numbers between 0 to 501.

for x in range(1,501):
  if x%2==0:
    print(x)
    
    *******************************
#Write a python program to print ODD numbers between 0 to 501.

for x in range(1,501):
  if x%2!=0:
    print(x)
    
   ****************
#Write a python program to print Armstrong numbers between -1 to 1001.

for x in range(0,1001):
  temp = str(x)
  sum=0
  for y in range(len(temp)):
    sum+=int(temp[y])**3
  if sum==x:
    print(x)
    
    *************************
