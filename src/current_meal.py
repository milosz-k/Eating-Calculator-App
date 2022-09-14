from date import DateFile
from product import Product
from product_finder import FindProducts


class CurrentMeal:
    """Class of a meal"""

    def __init__(self) -> None:
        """Init basic variables"""
        self.current_products_list = []
        self.dict = dict()
        self.current_day_file = DateFile()

    def create_meal(self, query) -> None:
        """Create new group of products.

        Args:
            query (str): text contains products with their amount.
        """
        find_product = FindProducts()
        find_product.find_products_eaten(query)
        for n in range(0, find_product.number_of_products):
            find_product.set_product_params(n)
            the_product = Product(
                name=find_product.name,
                grams=find_product.grams,
                proteins=find_product.proteins,
                carbohydrates=find_product.carbohydrates,
                fats=find_product.fats,
            )
            self.current_products_list.append(the_product)

            the_product.create_product_dict()
            self.dict.update(the_product.current_product)
        self.info = find_product.info

    def save_meal_to_current_day(self) -> None:
        """Save meal to the current day's json file."""
        self.current_day_file.read_current_day()
        self.current_day_file.update_current_day(self.dict)
