import datetime
import json

from calories_goal import CaloriesGoal

TODAY = str(datetime.datetime.today().strftime("%d-%m-20%y"))


class DateFile:
    """Class of the daily file."""

    def __init__(self) -> None:
        "Init variables."
        self.proteins = 0
        self.carbohydrates = 0
        self.fats = 0
        self.whole_day_data = {}

    def create_current_day_file(self, dict) -> None:
        """Create a file.

        Args:
            dict (dict): dictionary contains products eaten during a meal.
        """
        with open(TODAY + ".json", "w") as self.day_of_eating:
            self.day_of_eating.write(f"{json.dumps(dict)}")

    def read_current_day(self) -> None:
        """Read a file."""
        try:
            with open(TODAY + ".json", "r") as self.day_of_eating:
                self.whole_day_data = json.load(self.day_of_eating)
        except FileNotFoundError:
            self.info = "There is no meal history today yet"
        else:
            self.info = "Meal history already exists today"

    def update_current_day(self, dict) -> None:
        """Update current day's file.

        Args:
            dict: dictionary contains products eaten during a meal.
        """
        self.keys_to_remove = []
        for key in dict:
            if key in self.whole_day_data:
                self.whole_day_data[key]["grams"] += dict[key]["grams"]
                self.whole_day_data[key]["proteins"] += dict[key]["proteins"]
                self.whole_day_data[key]["carbohydrates"] += dict[key]["carbohydrates"]
                self.whole_day_data[key]["fats"] += dict[key]["fats"]
                self.keys_to_remove.append(key)
        for key in self.keys_to_remove:
            del dict[key]
        self.whole_day_data.update(dict)
        with open(TODAY + ".json", "w") as self.day_of_eating:
            self.day_of_eating.write(f"{json.dumps(self.whole_day_data)}")

    def sum_daily_makros(self) -> None:
        """Sum proteins, carbohydrates and fats eaten during current day."""
        for key in self.whole_day_data:
            self.proteins += round(self.whole_day_data[key]["proteins"])
            self.carbohydrates += round(self.whole_day_data[key]["carbohydrates"])
            self.fats += round(self.whole_day_data[key]["fats"])

    def remaining_makros(self) -> None:
        """Calculate amount of remaining macronutrients."""
        self.my_goal = CaloriesGoal()
        self.my_goal.read()
        if self.my_goal.reading_complete:
            self.remaining_proteins = self.my_goal.proteins - self.proteins
            self.remaining_carbohydrates = (
                self.my_goal.carbohydrates - self.carbohydrates
            )
            self.remaining_fats = self.my_goal.fats - self.fats
            self.remaining_calories = (
                self.my_goal.calories
                - 4 * self.proteins
                - 4 * self.carbohydrates
                - 9 * self.fats
            )

    def print_daily_eaten_products(self) -> None:
        """Formulate daily eaten products with their amount."""
        self.list_of_products = []
        for key in self.whole_day_data:
            self.list_of_products.append(
                f"{key}: {self.whole_day_data[key]['grams']} grams"
            )
