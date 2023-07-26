Unit = input( "P for pounds or K Kilograms: ")

if Unit.upper() != 'P' or unit.upper() != 'K':
    print("you need to enter a valid Unit")
    
weight = float(input("Weight: "))

if Unit.upper() == 'K' and weight > 0:
    print( "weight in Kgs: " + str(weight) )

elif Unit.upper() == 'P' and weight > 0:
    converted = weight * 0.45
    print( "weight in Kgs: " + str(converted))

else:
    print("you need to enter a valid number")

    
Unit = input( "I for Inches or C Centimeters: ")
if unit.upper() != 'I' or unit.upper() != 'i':
    print("you need to enter a valid Unit")
    

height = float(input("height: "))

if Unit.upper() == 'C' and height > 0:
    print( "Height in CMs: " + str(height)  )

elif Unit.upper() == 'I' and height > 0:
    converted = height * 2.54
    print( "Height in CMs: " + str(converted))

else:
    print("you need to enter a valid number")

print("Thank you")