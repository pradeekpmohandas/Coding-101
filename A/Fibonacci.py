def printFibno(n):
  if(n==0):
    fib = []
  elif(n==1):
    fib = [1]
  elif(n==2):
    fib = [1,1]
  elif(n>2):
    fib = [1,1]
    i = 1 
    while(i< n-1):
      fib.append(fib[i]+fib[i-1])
      i = i +1
  return fib 

print(printFibno(int(input("Enter Number"))))
