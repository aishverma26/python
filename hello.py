# single line comment
#print("hello")

'''
multi line comment
my name is yush
bhopal
'''

'''
three data types
number
ex - n=10, 10.2

string
a= "aishwarya"

boolean
x = True/False


'''


'''

n1 =  10 # this is number 
n2 =  20
n3 = n1 + n2
print("sum of ", n1, "+" , n2 , "is ", n3)

n4 = n2 - n1
print("subtraction of", n2, "-", n1, "is", n4 )


n5 = n2 * n1
print("multiplication of", n2," * ", n1, "is", n5 )


n6 = n2 / n1
print("div of", n2, "/", n1, "is", n6 )

'''

'''
page 14

n1 = input("enter a number: ")
n1 = float(n1)
print(type(n1))

n2 = input("enter a number:")
n2 = float(n2)

n3 = n1 + n2
print("addition of", n1, "+", n2, "is", n3)

n4 = n1 * n2
print("multiplication of", n1, "*", n2, "is", n4 )

'''

'''
page 16

n1  = 100

n2 = input("value of your card is:")
n2 = float(n2)

n3 = n1 / n2
print ("total rides left on your card is", n1, "/", n2, "is", n3)

'''

'''
page 34

p1 = float(input("enter price value of 1st product:"))
p2 = float(input("enter price value of 2nd product:"))
p3 = float(input("enter price value of 3rd product:"))

p4 = (p1 + p2 + p3)//3

print("average price of three products is", p4)

'''
'''
page 39

n1 = float(input("enter seconds:"))
n2 = 60
n3 = n1 // n2
n4 = n1 % n2

print("That's", n3, "minute and", n4, "seconds")
'''

'''
#page 42

p = float(input("enter the principal amount:"))
r = float(input("enter the rate of interest:"))
t = float(input("enter the time period:"))
s = p * ((1 + r)**t)

print ("You will need", p, "dollars to generate", s, "dollars at", r,"% over", t, "years.")

'''

#slide no 2 
#page 21
'''
t1 = 72
t2 = 86
t = float(input("enter temperature:"))

if t < t1:
    print("you're going to freeze your fish!")

if t > t2:
    print("you're going to boil your fish!")

if t > 81 and t > 8

'''

'''

a = int(input("Enter a number between 1 to 10:"))
b = 6  #my secret number
if a==b:
    print("you win!")

if a<b:
    print("you are below the secret number, Try again!")

if a>b:
    print("you are above the secret number, Try again!")   

'''

'''
a = 10000
b =  float(input("Enter your monthly sales amount:"))
if a <= b:
    print("You are eligible for a bonus of $500.")
    print("Good job!")
    print("You will recieve a bonus of $500.")    
if a > b:
    print("You will recieve a bonus of $0.")

'''

'''

a = 10000
b =  float(input("Enter your monthly sales amount:"))
if a <= b:
    print("You are eligible for a bonus of $500 and 1% commission.")
    print("Good job!")
if b > 50000:    
    print("Your total take home amount is $500 and 5% commission instead of 1% commission.")
    print("Good job!")    
if a > b:
    print("You will receive 0$ bonus.")

'''

'''
p = float(input("Enter hourly rate of pay:"))
t = float(input("enter no. of hours worked in a week:"))
if t < 40:
    w = p * t
    print("Your pay is", w)
if t > 40:
    w = p * t
    o = t - 40
    p1 = o * 1.5 * p
    w1 = p1 + w 
    print("your pay is", w1)    
'''

'''
p1 = "secret"
p = input("Enter password:")

if p == p1:
    print("Welcome!")

else:
    print("Try again!")

'''

'''

secretnumber = 5
usernumber = int(input("Guess a number:"))
if usernumber == secretnumber:
    print("you guessed it!")
else:
    if usernumber < secretnumber:
        print("Your number is too low!")
    else:
        print("Your number is too high!")        

'''

'''

n1 =input("Enter 1st name:")
n2 =input("Enter 2nd name:")
if n1 > n2:
    print(n2, "and", n1)
else:
    print(n1, "and", n2)

'''

'''

s = int(input("Enter your yearly salary:"))
t = int(input("Enter number of years working in current company:"))
if s >= 50000 and t >= 2:
    print("You qualify for loan!")
else:
    if s >= 100000 and t < 2:
        print("You qualify for loan!")
    else:
        print("You do not qualify!")    

'''

'''

a = 5
b = 10
print( a > b and a > 1 )
print ( a > 1 and b > a )
print ( a == 5 and b < 100)
print ( a > 1 and b < 1 and b > a)
print( a > 1 and b > 1 and b > a)

'''

'''

s = float(input("Enter gross sales:"))
r = float(input("Enter commission rate:"))
c = s*r
while c == s*r:
    print("commission earned is", c)
    break

'''



