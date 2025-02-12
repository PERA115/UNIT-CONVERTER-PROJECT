#SMALL PROJECT ~ CREATE A MEASUREMENT UNIT CALCULATOR


#List of valid units

valid_units = ['meters','centimeters','kilometers']

#Conversion factors (for example)
conversion_f = {
    ('meters', 'centimeters'): 100,
    ('meters','kilometers'): 0.001,
    ('centimeters', 'meters'): 0.01,
    ('centimeters','kilometers'):0.00001,
}



#Ask teh user for the numeric value
while True:
    try:
        value = float(input('Enter the value to convert: '))
        break
    except ValueError:
        print('Error: Please enter a valid number.')



#Ask for he source unit
while True:
 source_unit = input('Enter the source unit (meters, centimeters, kilometers): ').strip().lower()  
 if source_unit in valid_units:
        break
 else:
     print('Error: Invalir unit. Try again.')



#Ask for the target unit
while True:
    target_unit = input('Enter the target unit (meters, centimeters, kilometers: ').strip().lower()
    if target_unit in valid_units:
        break
    print('Error: Invalid unit. Try again.')



# Convert the value using the conversion factors
if (source_unit, target_unit) in conversion_f:
    result = value * conversion_f[(source_unit,target_unit)]
    print(f'{value} {source_unit} is {result} {target_unit}.')
else:
    print('Conversion is not suported')

