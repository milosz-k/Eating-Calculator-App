import requests
import os
from dotenv import load_dotenv
load_dotenv("./../.env")
API_NUTRITIONIX = "https://trackapi.nutritionix.com/v2/natural/nutrients"
APP_ID_NUTRITIONIX = os.getenv("APP_ID_NUTRITIONIX")
API_KEY_NUTRITIONIX = os.getenv("API_KEY_NUTRITIONIX")

class FindProducts:
    """Class of API management."""

    def __init__(self) -> None:
        """Init API headers."""
        self.headers_nutritionix = {
            "x-app-id": APP_ID_NUTRITIONIX,
            "x-app-key": API_KEY_NUTRITIONIX,
            "Constent-Type": "json",
        }

    def find_products_eaten(self, query) -> None:
        """Find products parameters.

        Args:
            query (str): text contains products with their amount.
        """
        self.query = query
        self.probably_products = 1
        self.probably_products += self.query.count(",") + self.query.count("and")
        self.body = {
            "query": self.query,
        }

        self.response = requests.post(url=API_NUTRITIONIX, json=self.body, headers=self.headers_nutritionix)
        self.response_json = self.response.json()
        self.number_of_products = len(self.response_json["foods"])
        if self.number_of_products < self.probably_products:
            self.info = "There may be less products found and used then suspected"
        else:
            self.info = "All products found"
    
    def set_product_params(self, ordinal_nr) -> None:
        """Set product parameters.
        
        Args:
            ordinal_nr (int): ordinal number of a product.
        """
        self.name = self.response_json["foods"][ordinal_nr]["food_name"]
        if self.name[-1] == "s":
            self.name = self.name[:-1]
        self.grams = self.response_json["foods"][ordinal_nr]["serving_weight_grams"]
        self.proteins = self.response_json["foods"][ordinal_nr]["nf_protein"]
        self.carbohydrates = self.response_json["foods"][ordinal_nr]["nf_total_carbohydrate"]
        self.fats = self.response_json["foods"][ordinal_nr]["nf_total_fat"]