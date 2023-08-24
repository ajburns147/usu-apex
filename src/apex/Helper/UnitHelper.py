def get_all_dimensions():
    return list(master_dict.keys())

def get_all_units(dimension):
    return list(master_dict[dimension].keys())

def get_unit_dict(dimension):
    return master_dict[dimension]

def get_base_unit(dimension):
    return get_all_units(dimension)[0]

def convert(dimension, value, from_unit, to_unit):
    unit_dict = get_unit_dict(dimension)
    converted_value = value*unit_dict[from_unit]/unit_dict[to_unit]
    return converted_value


master_dict = {

    "acceleration": {
        "m/(s)^2": 1,
        "cm/(s)^2": .01,
        "in/(s)^2": 0.0254,
        "ft/(s)^2": 0.3048,
        "g_0": 9.80665
        },

    "angle": {
        "radians": 1,
        "degrees": 0.0174533,
        },

    "area": {
        "m^2": 1,
        "km^2": 1000**2,
        "mm^2": .001**2,
        "ft^2": 0.3048**2,
        "in^2": 0.0254**2,
        "yard^2": 0.9144**2,
    },

    "volume": {
        "m^3": 1,
        "km^3": 1000**3,
        "mm^3": .001**3,
        "ft^3": 0.3048**3,
        "in^3": 0.0254**3,
        "yard^3": 0.9144**3,
        },

    "force": {
        "N": 1,
        "kN": 1e3,
        "MN": 1e6,
        "lb": .45359237,
        "kip": 4448.2216152605,
        },

    "length": {
        "m": 1,
        "km": 1000,
        "mm": .001,
        "ft": 0.3048,
        "in": 0.0254,
        "yard": 0.9144,
        },

    "mass": {
        "kg": 1,
        "g": .001,
        "Mg": 1000,
        "lb": .45359237,
        "kip": 4448.2216152605,
        "oz": 0.0283495,
        "metric_ton": 1000,
        "US_ton" : 907.18474,
        "ozt": 0.0311035,
        },

    "pressure": {
        "Pa": 1,
        "kPa": 1000,
        "psi": 6894.7572931683635,
        "bar": 1e5,
        "atm": 101325,
        "mmHg": 133.322387415,
        },

    "stress": {
            "Pa": 1,
            "kPa": 1000,
            "psi": 6894.7572931683635,
        },

    "time": {
            "sec": 1,
            "min": 60,
            "hour": 60*60,
            "day": 60*60*24,
            "week": 60*60*24*7,
            "year": 31557600,
            "ms": .001,
            "μs": 10**-6,
            "ns": 10**-9,
        },

    "torque": {
            "N*m": 1,
            "ft*lb": 0.138254954376,
            "in*lb": 0.011521246198,
            "mN*m": 0.001,
            "gf*cm": 9.80665e-05,
        },

    "velocity": {
            "m/s": 1,
            "cm/s": .01,
            "ft/s": 0.3048,
            "ft/min": 0.00508,
            "km/h": 0.2777777777777778,
            "mph": 0.44704,
            "knot": 0.514444444,
        },

}



if __name__ == "__main__":
    print(get_all_dimensions())
    print(get_all_units("angle"))
    print(get_base_unit("angle"))

    print(convert(dimension="mass", value=10, from_unit="lb", to_unit="oz"))
