print("###Temperature Converter###")
celsius = int(input("Enter a Celsius Temperature: ")) 

#fuction conv to convert celcius into fahrenheit
def conv(celsius):
    a = 9/5 * celsius + 32 #since F = 9/5 × C + 32
    return a 

fahrenheit = conv(celsius)
print(celsius,"degrees Celcius in fahrenheit is",fahrenheit,"degrees Fahrenheit")
