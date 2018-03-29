"""
Pyramid-1
* 
* * 
* * * 
* * * * 
* * * * * 
"""
def pypart(n):
     
    # outer loop to handle number of rows
    # n in this case
    for i in range(0, n):
        for j in range(0,i):
          print("*",end =" ")
        print()
 
# Driver Code
n = 6
pypart(n)
# Driver Code
n = 10
pypart(n)



"""
Pyramid-2
        * 
      * * 
    * * * 
  * * * * 
* * * * * 

"""
def pypart2(n):
     
    # number of spaces
    k = 2*n - 2
 
    # outer loop to handle number of rows
    for i in range(0, n):
        for j in range(0, k):
            print(end=" ")
        # decrementing k after each loop
        k = k - 2
        for j in range(0, i+1):
            print("* ", end="")
        # ending line after each row
        print("\r")
 
# Driver Code
n = 5
pypart2(n)




""""
pyramid 3
       *
      **
    ***
  ****
*****
"""
print("*",end="") #instead of ==> print("* ",end="")
