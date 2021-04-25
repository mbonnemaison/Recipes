"""
Convert volumes
1 tablespoon = 1 Tbsp
1 teaspoon = 1 tsp
1 cup is US legal cup.
Units are in US.
"""

number_ml_per_unit = {
    'Tbsp':  14.787,
    'tsp' :   4.929,
    'cup' : 236.588,
    'l'   :   1000,
    'dl'  :   100,
    'cl'  :   10,
    'ml'  :   1,
    'pint': 473.175,
    'fl oz': 29.573,
    'cubic cm': 1,
    'cubic dm': 1000,
    'cubic m' : 1000000,
    'cubic foot' : 28316.85,
    'cubic inch' : 16.387,
    'cubic yard' : 764554.933,
    'gallon': 3785.400,
}

def convert_volume(number, unit_from, unit_to):
    return number_ml_per_unit[unit_from] * number / number_ml_per_unit[unit_to]
