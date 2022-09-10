class Product:
    """Class of a product parameters."""

    def __init__(self, name, grams, proteins, carbohydrates, fats) -> None:
        """Init the product existence.

        Args:
            name (str): name of a product
            grams (int): amount of a product
            proteins (int): amount of proteins in a product
            carbohydrates (int): amount of carbohydrates in a product
            fats (int): amount of fats in a product
        """
        self.name = name
        self.grams = grams
        self.proteins = proteins
        self.carbohydrates = carbohydrates
        self.fats = fats

    def create_product_dict(self) -> None:
        """Create dictionary includes product parameters."""
        self.current_product = {
            self.name: {
                "grams": round(self.grams),
                "proteins": round(self.proteins),
                "carbohydrates": round(self.carbohydrates),
                "fats": round(self.fats),
            }
        }
