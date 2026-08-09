# This code gets a number (x) and repeats a change n times
# If x is even: divide it by 2
# If x is odd: multiply it by 2 and subtract 1
# Then print the final result

n = int (input("enter a number:\n"))
x = int (input("enter another number"))
for i in range (n):
    if x % 2 ==0:
        x=x//2
    else:
        x = (x*2)-1

print (x)