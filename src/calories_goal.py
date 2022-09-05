import json

class CaloriesGoal:
    
    def set(self, proteins, carbohydrates, fats):
        self.dictionary = {
            "proteins": proteins,
            "carbohydrates": carbohydrates,
            "fats": fats,
            "calories": proteins * 4 + carbohydrates * 4 + fats * 9
        }
        with open("my_makro.json", "w") as makro:
            makro.write(json.dumps(self.dictionary))

    def read(self):
        self.reading_complete = False
        try:
            with open("my_makro.json", "r") as makro:
                self.dictionary = json.load(makro)
        except json.JSONDecodeError:
            self.info = "Incomplete makro data"
        except FileNotFoundError:
            self.info = "No File. Please set your daily makros instead"
        except KeyError:
            self.info = "Incomplete makro data"
        else:
            self.proteins = self.dictionary["proteins"]
            self.carbohydrates = self.dictionary["carbohydrates"]
            self.fats = self.dictionary["fats"]
            self.calories = self.dictionary["calories"]
            self.reading_complete = True
            self.info = "File read successfully"