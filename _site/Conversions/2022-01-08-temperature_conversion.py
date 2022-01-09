"""
Temperature conversion
- C means Celsius
- F means Fahrenheit
- K means Kelvin

"""
convert_to_Kelvin_table = {
    "K": lambda x: x,
    "C": lambda x: x + 273.15,
    "F": lambda x: (x - 32)*5.0/9.0 + 273.15,
}

#Convert to wanted unit from Kelvin
convert_to_table = {
    "K": lambda x: x,
    "C": lambda x: x - 273.15,
    "F": lambda x: (x - 273.15)*9.0/5.0 + 32 ,
}

def convert_to_Kelvin(number, unit_from):
    return convert_to_Kelvin_table[unit_from](number)

def convert_to(number, unit_to):
    return convert_to_table[unit_to](number)

def convert_temperature(number,unit_from, unit_to):
    return convert_to(convert_to_Kelvin(number, unit_from), unit_to)
