"""
    * 
   * * 
  * * * 
 * * * * 
* * * * * 
Triangle Pyramind

K decrement By 1
"""

def pattern(n):
  k = n*2 -2
  for i in range(1,n+1):
    for j in range(k):
      print(end=" ")
    k= k-1
    for l in range(i):
      print("* ",end="")
    print()
  
pattern(5)
