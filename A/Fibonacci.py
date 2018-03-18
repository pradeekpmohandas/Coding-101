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


#another code Fibonacci Numbers
def printFibonacciNumbers(n):
     
    f1 = 0
    f2 = 1
    if (n < 1):
        return
    for x in range(0, n):
        print(f2, end = " ")
        next = f1 + f2
        f1 = f2
        f2 = next
printFibonacciNumbers(7)
 
#Recussrsive Solution :
# Function for nth Fibonacci number
 
def Fibonacci(n):
    if n<0:
        print("Incorrect input")
    # First Fibonacci number is 0
    elif n==1:
        return 0
    # Second Fibonacci number is 1
    elif n==2:
        return 1
    else:
        return Fibonacci(n-1)+Fibonacci(n-2)
      
