def fahrenheit_to_celsius(fr):
    return (5 / 9) * (fr - 32)

fr = float(input("Enter temperature in Fahrenheit: "))
celsius = fahrenheit_to_celsius(fr)

print(f"{fr}°F is equal to {celsius:.2f}°C.")