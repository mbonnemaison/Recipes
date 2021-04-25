"""
Mass conversion
g = gram
kg = kilogram
dg = decigram
cg = centigram
mg = milligram
lb = pound
"""

number_gram_per_unit = {
    'g' : 1,
    'kg': 1000,
    'dg' : 0.1,
    'cg' : 0.01,
    'mg' : 0.001,
    'ounce' : 28.350,
    'lb' : 453.592,
}

def convert_mass(number, unit_from, unit_to):
    return number_gram_per_unit[unit_from] * number / number_gram_per_unit[unit_to]
