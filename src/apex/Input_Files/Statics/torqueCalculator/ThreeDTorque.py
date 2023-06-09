from apex.Helper.TopicFactory import TopicFactory


class ThreeDTorque(TopicFactory):
    def __init__(self):
        self.input_dict = {
            "FVector": {
                "default_value": [1, 2, 3],
                "dimension": "length",
            },

            "rVector": {
                "default_value": [2, 3, 4],
                "dimension": "length",
            },

            "Torque": {
                "default_value": None,
                "dimension": "length",
            },
        }

        self.info = {
             "input": self.input_dict,
             "formula": None,
             "Note": "This is a one dimensional torque calculator",
             "solve_method": "",
             "plot_method": False,
             "Bonus": self.Bonus
             }

    def giveInfo(self):
        return self.info

    def Bonus(self, info):
        return self.selfSolve(info["input"]["FVector"]["value"], info["input"]["rVector"]["value"])

    def selfSolve(self, forceV, radiusV):
        import numpy as np

        # Define force and radius vectors
        force_list = [float(num) for num in forceV.split()]
        radius_list = [float(num) for num in radiusV.split()]
        print(force_list)
        force_vec = np.array(force_list)
        radius_vec = np.array(radius_list)

        # Calculate torque vector
        torque_vec = np.cross(radius_vec, force_vec)
        return {"Torque": [torque_vec, "", "length", "", ""]}
