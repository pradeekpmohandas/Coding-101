#FOR STRING
wrd=input("Please enter a word")
wrd=str(wrd)
rvs=wrd[::-1] #reversing a string (https://stackoverflow.com/questions/509211/understanding-pythons-slice-notation#)
print(rvs)
if wrd == rvs:
    print("This word is a palindrome")
else:
    print("This word is not a palindrome")


#FOR INTEGER ( converting integer to string ) 
num = input('Enter any number : ')
try:
    val = int(num)
    if num == str(num)[::-1]:
        print('The given number is PALINDROME')
    else:
        print('The given number is NOT a palindrome')
except ValueError:
    print("That's not a valid number, Try Again !")
