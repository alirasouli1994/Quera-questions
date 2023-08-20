a = float(input()) # WeightInKilograms
b = float(input()) # HeightInMeters
BMI = a/(b**2)
BMI = "{:.2f}".format(BMI)
print(BMI)
BMI = float(BMI)
if BMI < 18.5 :
    print('Underweight')
elif 18.5 <= BMI < 25 :
    print('Normal')
elif 25 <= BMI < 30 :
    print('Overweight')
elif 30 <= BMI :
    print('Obese')
