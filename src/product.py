class Product:

    def __init__(self, name, grams, proteins, carbohydrates, fats):
        self.name = name
        self.grams = grams
        self.proteins = proteins
        self.carbohydrates = carbohydrates
        self.fats = fats

    def create_product_dict(self):
        self.current_product = {
            self.name: {"grams": round(self.grams),
            "proteins": round(self.proteins),
            "carbohydrates": round(self.carbohydrates),
            "fats": round(self.fats)
            }
        }