input_filename = "Pythagorean_Theorem"
formula = "a**2 + b**2 == c**2"
note = ""


print_str = f"""
from apex.Helper.TopicFactory import TopicFactory


class {input_filename}(TopicFactory):
    def __init__(self):
        self.input_dict = {{
            "a": {{
                "default_value": 3,
                "dimension": "length",
            }},
            "b": {{
                "default_value": 4,
                "dimension": "length",
            }},
            "c": {{
                "default_value": None,
                "dimension": "length",
            }},
        }}

        self.info = {{
            "input": self.input_dict,
            "formula": "{formula}",
            "Note": "{note}",
            "solve_method": "",
            "plot_method": False,
            "Bonus": self.Bonus
        }}

    def giveInfo(self):
        return self.info
"""
print(print_str)