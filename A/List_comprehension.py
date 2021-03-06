#REF (http://www.pythonforbeginners.com/basics/list-comprehensions-in-python)

#Print a list with even numbers
a = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
even = [x for x in a if x%2==0 ]
print(even)

#AGE
 years_of_birth = [1990, 1991, 1990, 1990, 1992, 1991]
  ages = []
  for year in years_of_birth: 
    ages.append(2014 - year)
print(ages)

#EQUIVALENT :
years_of_birth = [1990, 1991, 1990, 1990, 1992, 1991]
ages = [2014 - year for year in years_of_birth]


#another example 
import random
a = random.sample(range(1,30), 12)
b = random.sample(range(1,30), 16)
result = [i for i in set(a) if i in b]


#prime check using list comprehension 

num = int(raw_input('Insert a number: '))
a = [x for x in range(2, num) if num % x == 0]

def is_prime(n):
	if num > 1:
		if len(a) == 0:
			print 'prime'
		else:
			print 'NOT prime'
	else:
		print 'NOT prime'
	
is_prime(num)
