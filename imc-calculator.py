def calculate_imc(height, weight):
    return height / (weight ** 2)

weight = float(input("Enter your weight in kilograms: "))
height = float(input("Enter your height in meters: "))

print(f"Your IMC is: {calculate_imc(weight, height):.2f}")

if imc < 18.5:
    print("You are underweight.")
elif 18.5 <= imc < 24.9:
    print("You are at a normal weight.")
elif 25 <= imc < 29.9:
    print("You are overweight.")
else:
    print("You are obese.")
