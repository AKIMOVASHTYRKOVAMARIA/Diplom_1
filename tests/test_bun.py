from praktikum.bun import Bun
from data import Data


class TestBun:
    def test_get_bun_name(self):
        name = Data.BUN
        price = 1255
        bun = Bun(name,price)
        assert bun.get_name() == name


    def test_get_bun_price(self):
        name = Data.BUN
        price = 1255
        bun = Bun(name, price)
        assert bun.get_price() == price


