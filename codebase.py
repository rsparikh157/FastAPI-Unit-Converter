from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from enum import Enum

unit_converter = FastAPI()

conversion = {
    "length": {"km": 1000, "m": 1, "cm": 0.01},
"mass": {
"kg": 1,
"g": 0.001,
"lb": 0.45359237
},
    "data_storage": {
        "B": 1,
        "kB": 1000,
        "MB": 1000000,
        "GB": 1000000000,
        "KiB": 1024,
        "MiB": 1048576,
        "GiB": 1073741824
    }
}
#Handling temperature separately
temperature_units = ["celsius", "fahrenheit", "kelvin"]

class Unit(str, Enum):
    km = "km"
    m = "m"
    cm = "cm"

    kg = "kg"
    g = "g"
    lb = "lb"

    B = "B"
    kB = "kB"
    MB = "MB"
    GB = "GB"
    KiB = "KiB"
    MiB = "MiB"
    GiB = "GiB"

    celsius = "celsius"
    fahrenheit = "fahrenheit"
    kelvin = "kelvin"


#Helper Function to completely check validity of any input unit
def valid_checker(unit):
    unit_category = None

    for category in conversion:
        if unit in conversion[category]:
            unit_category = category
            break

    return unit_category

def check_compatability(unit1, unit2):
    category1 = valid_checker(unit1)
    category2 = valid_checker(unit2)

    if category1 is None or category2 is None:
        return "Invalid unit"

    if category1 == category2:
        return "Successful"

    return "Incompatible units"


def calc(src, trgt, value):
        category = valid_checker(src)

        result = (value * conversion[category][src]) / conversion[category][trgt]

        return result

def temperature_calc(unit1, unit2, value):
    
    if unit1 == "celsius":
        celsius = value
    elif unit1 == "fahrenheit":
        celsius = (value - 32) * 5 / 9
    else:
        celsius = value - 273.15

    if unit2 == "celsius":
        result = celsius
    elif unit2 == "fahrenheit":
        result = (celsius * 9 / 5) + 32
    else:
        result = celsius + 273.15

    return result



#Response Model
class ConversionResponse(BaseModel):
    value:	float
    from_unit:	str
    to_unit:	str
    result:	float



#ENDPOINTS
@unit_converter.get("/convert", response_model= ConversionResponse)
def get_unit(value: float, from_unit: Unit, to_unit: Unit):
    if from_unit in temperature_units and to_unit in temperature_units:
        result = temperature_calc(from_unit, to_unit, value)
    else:
        compatibility = check_compatability(from_unit, to_unit)

        if compatibility != "Successful":
            raise HTTPException(status_code=400, detail=compatibility)

        result = calc(from_unit, to_unit, value)

    return {
        "value": value,
        "from_unit": from_unit,
        "to_unit": to_unit,
        "result": result
    }