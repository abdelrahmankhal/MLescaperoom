

temp = int(input("Enter temperature: "))
pressure = int(input("Enter pressure: "))
if temp > 75 and pressure > 120:
        result = "failed"
else:
        result = "pass"
print(f"The machine’s status is: {result}")

