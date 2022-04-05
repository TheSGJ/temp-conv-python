f = float(input("Enter a Fahrenheit Temperature: "))

def conv(f):
    celcius = f*5/9-32
    return celcius 

c = conv(f)
print(f, "fahrenheit in celcius is", c)