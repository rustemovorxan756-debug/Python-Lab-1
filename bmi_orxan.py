a=int(input('enter the weight in kilograms'))
b=int(input('enter the height in meters'))
BMI=a/(b*b)
if BMI< 18.5:
    print('underweight')
elif BMI> 18.5 and BMI< 24.5:
    print('normal weight')
elif BMI> 25.0 and BMI< 29.9:
    print('overweight')
elif BMI> 30.0:
    print('obese')
