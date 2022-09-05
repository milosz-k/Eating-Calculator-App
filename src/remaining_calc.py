from product_finder import FindProducts
from product import Product
from current_meal import CurrentMeal
from ortools.linear_solver import pywraplp

meal = CurrentMeal()
solver = pywraplp.Solver_CreateSolver("GLOP")

class RemainingCalculator:
    """Class of calculating remaining nutritional values."""

    def __init__(self) -> None:
        """Init basic variables."""
        self.current_products_list = []
        self.remaining_proteins = 0
        self.remaining_carbohydrates = 0
        self.remaining_fats = 0
        self.remaining_calories = 0
        self.info = []
 
    def create_available_products_list(self, query) -> None:
        """Create a list contains products chosen by the user.
        
        Args:
            query (str): text contains products with their amount.
        """
        find_product = FindProducts()
        find_product.find_products_eaten(query)
        for n in range(0, find_product.number_of_products):
            find_product.set_product_params(n)
            the_product = Product(name=find_product.name, grams=find_product.grams, proteins=find_product.proteins, carbohydrates=find_product.carbohydrates, fats=find_product.fats)
            self.current_products_list.append(the_product)
        self.info.append(find_product.info)

    def calculate_remaining_makro(self) -> None:
        """Calculate remaining proteins, carbohydrates and fats daily."""
        meal.current_day_file.read_current_day()
        meal.current_day_file.sum_daily_makros()
        meal.current_day_file.remaining_makros()
        if meal.current_day_file.my_goal.reading_complete == True:
            self.remaining_proteins = meal.current_day_file.remaining_proteins
            self.remaining_carbohydrates = meal.current_day_file.remaining_carbohydrates
            self.remaining_fats = meal.current_day_file.remaining_fats
            self.remaining_calories = meal.current_day_file.remaining_calories
        self.info.append(meal.current_day_file.info)
        self.info.append(meal.current_day_file.my_goal.info)
    
    def calculate(self) -> None:
        """Calculates amount of each product separately to fill up proteins, carbohydrates and fats to reach the daily goal."""
        for n in range(0, len(self.current_products_list)):
            if self.remaining_proteins >= 0:
                try:
                    self.jeszcze_gramow_produktu_aby_bialko = self.remaining_proteins / self.current_products_list[n].proteins * self.current_products_list[n].grams
                    self.info.append(f"{round(self.jeszcze_gramow_produktu_aby_bialko)} grams of {self.current_products_list[n].name} needed to fill remaining {self.remaining_proteins}g protein")
                except ZeroDivisionError:
                    self.info.append(f"{self.current_products_list[n].name} has no protein, so it is impossible to fill protein by this product.")
            else:
                self.info.append(f"You have exceeded your proteins by {abs(self.remaining_proteins)} grams already")

            if self.remaining_carbohydrates >= 0:
                try:
                    self.jeszcze_gramow_produktu_aby_wegle = self.remaining_carbohydrates / self.current_products_list[n].carbohydrates * self.current_products_list[n].grams
                    self.info.append(f"{round(self.jeszcze_gramow_produktu_aby_wegle)} grams of {self.current_products_list[n].name} needed to fill remaining {self.remaining_carbohydrates}g carbohydrates")
                except ZeroDivisionError:
                    self.info.append(f"{self.current_products_list[n].name} has no carbohydrates, so it is impossible to fill carbohydrates by this product.")
            else:
                self.info.append(f"You have exceeded your carbohydrates by {abs(self.remaining_proteins)} grams already")

            if self.remaining_fats >= 0:
                try:
                    self.jeszcze_gramow_produktu_aby_tluszcze = self.remaining_fats / self.current_products_list[n].fats * self.current_products_list[n].grams
                    self.info.append(f"{round(self.jeszcze_gramow_produktu_aby_tluszcze)} grams of {self.current_products_list[n].name} needed to fill remaining {self.remaining_fats}g fats")
                except ZeroDivisionError:
                    self.info.append(f"{self.current_products_list[n].name} has no fats, so it is impossible to fill fats by this product.")
            else:
                self.info.append(f"You have exceeded your fats by {abs(self.remaining_proteins)} grams already")

    def solver(self, query) -> None:
        """Optimize amount of every given product to fill up proteins, carbohydrates and fats to reach the daily goal.
        
        Args:
            query (str): text contains products with their amount.
        """
        self.create_available_products_list(query)
        self.calculate_remaining_makro()
        if "File read successfully" in self.info:
            self.solver_list = []
            for product in self.current_products_list:
                ratio = 100 / product.grams
                product.grams = product.grams * ratio
                product.proteins = product.proteins * ratio
                product.carbohydrates = product.carbohydrates * ratio
                product.fats = product.fats * ratio
                product.grams = solver.NumVar(0, 1000, "grams")
            ct_p = solver.Constraint(0, self.remaining_proteins, "ct")
            ct_c = solver.Constraint(0, self.remaining_carbohydrates, "ct")
            ct_f = solver.Constraint(0, self.remaining_fats, "ct")
            for product in self.current_products_list:
                ct_p.SetCoefficient(product.grams, product.proteins)
                ct_c.SetCoefficient(product.grams, product.carbohydrates)
                ct_f.SetCoefficient(product.grams, product.fats)
            objective = solver.Objective()
            for product in self.current_products_list:
                objective.SetCoefficient(product.grams, product.proteins + product.carbohydrates + product.fats)
            objective.SetMaximization()
            solver.Solve()
            for product in self.current_products_list:
                self.info.append(f"{product.name}, {round(product.grams.solution_value()*100)} grams")        