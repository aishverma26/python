
while True:
    f = float(input("Enter the temperature:"))  #tem in fahrenheit
    c = (f - 32)*5/9
    print("Temperature in celcius is", c)
    userinput = input("Do you want to continue (y/n)? ")
    if userinput == 'y':
        continue
    else:
        break
print("program end")
