from src.calculations import Calculations


class TestCalc:
    calc= Calculations()

    def test_area_of_square(self):
        res= self.calc.area_of_square(6)
        assert res==36, 'area of square error'

    def test_area_of_rect(self):
        res= self.calc.area_of_rect(3, 5)
        assert res==15, 'area of rect error'