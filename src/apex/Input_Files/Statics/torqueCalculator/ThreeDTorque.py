from src.apex.Helper.TopicFactory import TopicFactory

class torque(TopicFactory):
    def __init__(self):
        self.input_dict = {
            "FVector": ["", [1,2,3], "length", "", ""],
            "rVector": ["", [2,3,4], "length", "", ""],
            "Torque": ["", "", "length", "", ""],
                      }

        self.info = {
             "input": self.input_dict,
             "formula": "",
             "Note": "This is a one dimensional torque calculator",
             "solve_method": "",
             "plot_method": False,
             "Bonus": self.Bonus
             }

    def giveInfo(self):
        return self.info

    def Bonus(self, info):
        return self.selfSolve(info["input"]["FVector"][0], info["input"]["rVector"][0])

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