def celsius_to_fahrenheit(celsius):
    fah = round((celsius * 9/5) + 32, 2)
    return fah

def fahrenheit_to_celsius(fahrenheit):
    cel = round((fahrenheit - 32) * 5/9, 2)
    return cel


def celsius_to_kelvin(celsius):
    kel = round(celsius + 273.15, 2)
    return kel


def convert_temperature(value, from_unit, to_unit):
    lowest = {"celsius": -273.15, "kelvin": celsius_to_kelvin(-273.15), "fahrenheit": celsius_to_fahrenheit(-273.15)}

    if from_unit == None or to_unit == None:
        raise ValueError("unsuppoerted unit")
    
    from_unit = from_unit.lower()
    to_unit = to_unit.lower()

    if not isinstance(value, (float, int)) or isinstance (value, bool):
        raise ValueError("value is not a number")

    if from_unit in lowest.keys() and value < lowest[from_unit]:
        raise ValueError("below absolute zero")
    elif from_unit not in lowest.keys() or to_unit not in lowest.keys():
        raise ValueError("unsupported unit")

    if from_unit == "fahrenheit" and to_unit == "celsius":
        return fahrenheit_to_celsius(value)
    elif from_unit == "kelvin" and to_unit == "celsius":
        return round(value - 273.15, 2)

    if from_unit == "kelvin" and to_unit == "fahrenheit":
        cel = round(value - 273.15, 2)
        return celsius_to_fahrenheit(cel)
    elif from_unit == "fahrenheit" and to_unit == "kelvin":
        cel = fahrenheit_to_celsius(value)
        return celsius_to_kelvin(cel)

    if from_unit == "celsius" and to_unit == "fahrenheit":
        return celsius_to_fahrenheit(value)
    elif from_unit == "celsius" and to_unit == "kelvin":
        return celsius_to_kelvin(value)

    return value