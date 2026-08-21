def is_positive (a):
    """
    This function takes a number from the user
    and checks if it is positive or zero

    """
    if a>=0:
        return True
    else:
        return False
    
a= int (input())
print(is_positive(a))