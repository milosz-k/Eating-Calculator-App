from product_finder import FindProducts
from product import Product
from date import DateFile

class CurrentMeal:

    def __init__(self):
        self.current_products_list = []
        self.dict = dict() #current products dict in fact
        self.current_day_file = DateFile()

    def create_meal(self, query):
        find_product = FindProducts()
        find_product.find_products_eaten(query)
        for n in range(0, find_product.number_of_products):
            find_product.set_product_params(n)
            the_product = Product(name=find_product.name, grams=find_product.grams, proteins=find_product.proteins, carbohydrates=find_product.carbohydrates, fats=find_product.fats)
            self.current_products_list.append(the_product)

            the_product.create_product_dict()
            self.dict.update(the_product.current_product)
        self.info = find_product.info

    def save_meal_to_current_day(self):
        self.current_day_file.read_current_day()
        self.current_day_file.update_current_day(self.dict)