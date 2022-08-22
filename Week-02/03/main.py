#Using appropriate variables and constants write a program to convert a temperature value from
#Fahrenheit to Celsius. You may also try to enhance your program to a two-way convertor

print("Temperature Converter")
print("Which Function You are Looking for: \n• Celsius to Fahrenheit Converter - F\n• Fahrenheit to Celsius Converter  - C \n")
choice = input("Press Letter related to your choice \t:")
value = float(input("Enter value \t:"))

try:
    if (choice == 'F' or  choice=='f'):
        fahrenheit= ((9*value)/5)+32
        print("{0} Celsius \tEqual to  \t{1:.2f} Fahrenheit".format(value,fahrenheit ))
    
    elif (choice == 'C' or  choice=='c'):
        celsius= ((value-32)*5)/9
        print("{0} Fahrenheit \tEqual to  \t{1:.2f} Celsius".format(value,celsius ))
    
except:
    print("_________Invalid_________")