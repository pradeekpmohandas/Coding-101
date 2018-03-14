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
