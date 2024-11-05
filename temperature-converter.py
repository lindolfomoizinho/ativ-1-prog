def converter_temp(celsius):
    return celsius * 1.8 + 32

temp_cel = float(input("Enter temperature in Celsius: "))

print(f"The temperature in Fahrenheit is: {converter_temp(temp_cel)}°F")
