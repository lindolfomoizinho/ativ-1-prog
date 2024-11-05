def converter_temp(celsius):
    return celsius * 1.8 + 32

tempCel = float(input("Enter temperature in Celsius: "))

print(f"The temperature in Fahrenheit is: {converter_temp(tempCel)}°F")