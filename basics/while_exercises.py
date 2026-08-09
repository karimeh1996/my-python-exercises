# This code receives a number from the user and by performing an operation, it increases the number to one.
#That is, it increases any number we give it to one. We can call this code a magic machine. 
n = int(input("plz enter a number:"))
while n > 1:
    if n % 2 == 0:
        n = n // 2
    else:
        n = (n * 3 ) + 1
    print (n)


    