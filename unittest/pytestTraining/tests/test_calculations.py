import pytest
from src.calculations import Calculations

class TestCalculations:
    def setup_method(self):
        self.calc = Calculations()

    @pytest.mark.parametrize("n1, n2, ev", [
        (5, 5, 10),
        (10, 10, 20),
        (0, 5, 5)
    ])
    def test_add(self, n1, n2, ev):
        res = self.calc.add(n1, n2)
        assert res == ev, "Addition error"

    def test_sub(self):
        res = self.calc.sub(22, 10)
        assert res == 12, "Subtraction error"

    def test_mul(self):
        res = self.calc.mul(10, 22)
        assert res == 220, "Multiplication error"

    def test_div(self):
        res = self.calc.div(10, 5)
        assert res == 2, "Division error"

    @pytest.mark.skip
    def test_ne(self):
        res = self.calc.ne(10, 10)
        assert res ==True, "NE error"

    @pytest.mark.xfail(reason='Zero division error')
    def test_diver(self):
        res= self.calc.div(10, 0)
        assert res== 0,"div error"
