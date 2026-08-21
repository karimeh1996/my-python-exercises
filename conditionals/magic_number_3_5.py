n = 1
while n != 0:
    n = int (input("please Enter a number (Enter 0 for Exit): ")) 
    if n==0:
        print ("goodbye  👋")
        
    if n % 3 == 0 and n % 5 == 0:
        print ("The number is legendary.")
    elif n % 5 == 0:
        print ("The number is cursed.")
    elif n % 3 == 0:
        print ("The number is magic.")
    else:
        print ("The number is normal")
    

    


