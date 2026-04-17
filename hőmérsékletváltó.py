
unit = input(" Is the temperature in Celsius or Fahrenheit (C/F): ")
tempreture = float(input(" Enter the temperature: "))

if unit == "C":
    result = tempreture * 1.8 + 32
    print(f"{round(result,2)}F")
elif unit == "F":
    result = (tempreture-32)*5/9
    print(f"{round(result,2)}C")
else:
    print(f"{unit}is an invalid unit!")