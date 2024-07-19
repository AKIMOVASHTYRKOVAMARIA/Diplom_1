import pytest
from praktikum.burger import Burger
from unittest.mock import Mock
from data import Data


class TestBurger:

    def test_set_buns(self):
        burger = Burger()
        bun_mock = Mock()
        burger.set_buns(bun_mock)
        assert burger.bun == bun_mock


    @pytest.mark.parametrize('ingredient',[Data.SAUCE_1,Data.FILLING_1])
    def test_add_ingredient(self,ingredient):
        burger = Burger()
        burger.add_ingredient(ingredient)
        assert ingredient in burger.ingredients


    @pytest.mark.parametrize('index', [0,1])
    def test_remove_ingredient(self,index):
        burger = Burger()
        sauce = Mock()
        filling = Mock()
        burger.ingredients = [sauce,filling]
        component = burger.remove_ingredient(index)
        assert component not in burger.ingredients


    def test_move_ingredient(self):
        burger = Burger()
        burger.ingredients = [Data.SAUCE_1,Data.SAUCE_2,Data.FILLING_1,Data.FILLING_2]
        burger.move_ingredient(0,1)
        assert burger.ingredients.index(Data.SAUCE_2) == 0


    def test_get_price(self):
        burger = Burger()
        bun_mock = Mock()
        sauce_mock = Mock()
        filling_mock = Mock()
        bun_mock.get_price.return_value = 25
        sauce_mock.get_price.return_value = 3
        filling_mock.get_price.return_value = 90
        burger.ingredients = [sauce_mock,filling_mock]
        burger.bun = bun_mock
        expected_price = 25*2 + 90 + 3
        assert burger.get_price() == expected_price


    def test_get_receipt(self):
        burger = Burger()
        bun_mock = Mock()
        bun_mock.get_name.return_value = 'bun_name'
        bun_mock.get_price.return_value = 100
        sauce_mock = Mock()
        sauce_mock.get_type.return_value = 'sauce'
        sauce_mock.get_name.return_value = 'sauce_name'
        filling_mock = Mock()
        filling_mock.get_type.return_value = 'filling'
        filling_mock.get_name.return_value = 'filling_name'
        burger.ingredients = [sauce_mock, filling_mock]
        burger.bun = bun_mock
        burger.get_price = Mock(return_value=500)
        expected_receipt = ('(==== bun_name ====)\n'
                            '= sauce sauce_name =\n'
                            '= filling filling_name =\n'
                            '(==== bun_name ====)\n'
                            '\n'
                            'Price: 500')
        assert burger.get_receipt() == expected_receipt






