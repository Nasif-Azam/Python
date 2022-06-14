import Modules_Converter
from Modules_Converter import pounds_to_kg

kg_weight = float(input("Enter a weight in KG: "))
lbs_weight = float(input("Enter a weight in Pounds: "))
print(f"KG to Pounds is: {Modules_Converter.kg_to_pounds(kg_weight)} Pounds")
print(f"Pounds to KG is: {pounds_to_kg(lbs_weight)} KG")
