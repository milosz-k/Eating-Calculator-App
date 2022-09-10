import json

class CaloriesGoal:
    """Class of the user's daily eating goal."""

    def set(self, proteins, carbohydrates, fats) -> None:
        """Save user's daily eating goal to the json file.

        Args:
            proteins (int): amount of proteins
            carbohydrates (int): amount of carbohydrates
            fats (int): amount of fats

        """
        self.dictionary = {
            "proteins": proteins,
            "carbohydrates": carbohydrates,
            "fats": fats,
            "calories": proteins * 4 + carbohydrates * 4 + fats * 9
        }
        with open("my_makro.json", "w") as makro:
            makro.write(json.dumps(self.dictionary))

    def read(self) -> None:
        """Read the user's daily eating goal file."""
        self.reading_complete = False
        try:
            with open("my_makro.json", "r") as makro:
                self.dictionary = json.load(makro)
        except json.JSONDecodeError:
            self.info = "Incomplete macronutrients data"
        except FileNotFoundError:
            self.info = "Please set your daily macronutrients goal instead"
        except KeyError:
            self.info = "Incomplete macronutrients data"
        else:
            self.proteins = self.dictionary["proteins"]
            self.carbohydrates = self.dictionary["carbohydrates"]
            self.fats = self.dictionary["fats"]
            self.calories = self.dictionary["calories"]
            self.reading_complete = True
            self.info = "File read successfully"