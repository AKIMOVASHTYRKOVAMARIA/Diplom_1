from praktikum.ingredient import Ingredient
from data import Data
from praktikum.ingredient_types import INGREDIENT_TYPE_SAUCE,INGREDIENT_TYPE_FILLING


class TestIngredient:

    def test_get_type(self):
        name = Data.SAUCE_2
        price = 800
        ingredient_type = INGREDIENT_TYPE_SAUCE
        ingredient = Ingredient(ingredient_type,name, price)
        assert ingredient.get_type() == ingredient_type


    def test_get_name(self):
        name = Data.SAUCE_2
        price = 1255
        ingredient_type = INGREDIENT_TYPE_FILLING
        ingredient = Ingredient(ingredient_type,name, price)
        assert ingredient.get_name() == name


    def test_get_price(self):
        name = Data.SAUCE_2
        price = 1255
        ingredient_type = INGREDIENT_TYPE_FILLING
        ingredient = Ingredient(ingredient_type,name, price)
        assert ingredient.get_price() == price


