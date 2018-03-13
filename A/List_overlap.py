a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
r = []
for number_a in a:
    for number_b in b:
        if (number_a==number_b):
            #checking if already added element - duplicate
            if(number_a not in r):
              r.append(number_a)
print ("The commmon values: ", r)
