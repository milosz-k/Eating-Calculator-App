from sqlite3 import DatabaseError
from current_meal import CurrentMeal
from calories_goal import CaloriesGoal
from remaining_calc import RemainingCalculator
from date import DateFile

class AppBrain:
    """Class of connection between logical classes."""

    def set_calories_goal(self, proteins, carbohydrates, fats) -> str:
        """Save user's daily eating goal to the file.

        Args:
            proteins (int): amount of proteins
            carbohydrates (int): amount of carbohydrates
            fats (int): amount of fats

        Return:
            str: information about user's daily goal setting attempt.
        """
        my_goal = CaloriesGoal()
        variables_correct = False
        while variables_correct == False:
            try:
                int(proteins) == proteins
                int(carbohydrates) == carbohydrates
                int(fats) == fats
                assert 0 <= int(proteins) and int(carbohydrates) and int(fats)
                variables_correct = True
            except ValueError:
                return "Please write your goal by numeric numbers"
            except AssertionError:
                return "Negative numbers not allowed"
            else:
                proteins = int(proteins)
                carbohydrates = int(carbohydrates)
                fats = int(fats)
        my_goal.set(proteins, carbohydrates, fats)
        return "Setup completed successfully"

    def add_meal(self, query) -> str:
        """Add a meal to the current day file.
        
        Args:
            query (str): text contains products with their amount.

        Return: 
            str: information about adding a meal attempt.
        """
        meal = CurrentMeal()
        try:
            meal.create_meal(query)
            meal.save_meal_to_current_day()
        except KeyError:
            return "No one product found"
        else:
            return f"{meal.info}\n{meal.current_day_file.info}"
            

    def else_to_eat(self, query) -> str:
        """Calculates amount of given products separately to fill up proteins, carbohydrates and fats to reach the daily goal.
        
        Args:
            query (str): text contains products with their amount.

        Return: 
            str: information about calculation attempt.
        """
        calculator = RemainingCalculator()
        calculator.create_available_products_list(query)
        try:
            calculator.calculate_remaining_makro()
            if "File read successfully" in calculator.info:
                calculator.calculate()
        except DatabaseError:
            pass
        info = ""
        for n in calculator.info:
            info += str(n)+"\n"
        return info

    def already_eaten_today(self) -> str:
        """Return daily eaten proteins, carbohydrates and fats."""
        today = DateFile()
        today.read_current_day()
        today.sum_daily_makros()

        return f"{today.info}\nYou have eaten today:\n{today.proteins}g proteins\n{today.carbohydrates}g carbohydrates\n{today.fats}g fats"

    def print_daily_eaten_products(self) -> str:
        """Return daily eaten products."""
        today = DateFile()
        today.read_current_day()
        today.print_daily_eaten_products()

        info = today.info+"\n"
        for product in today.list_of_products:
            info += product+"\n"
        return info

    def adjust_last_meal_solver(self, query) -> str:
        """Optimize amount of every given product to fill up proteins, carbohydrates and fats to reach the daily goal.
        
        Args:
            query (str): text contains products with their amount.
        
        Return:
            str: information about calculation attempt.
        """
        calculator = RemainingCalculator()
        try:
            calculator.solver(query)
        except KeyError:
            return "No one product found"
        else:
            info = ""
            for n in calculator.info:
                info += str(n)+"\n"
        return info