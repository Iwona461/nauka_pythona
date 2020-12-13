import unittest
from calculator import calculate
class TestCalculator(unittest.TestCase):
  def test_dodawanie(self):
    r = calculate(1, 2,'+')
    self.assertEqual(r, 3)

  def test_odejmowanie(self):
    r = calculate(10, 2,'-')
    self.assertEqual(r, 8)

  def test_mnozenie(self):
    r = calculate(1, 2,'*')
    self.assertEqual(r, 2)

  def test_dzielenie(self):
    r = calculate(10, 2,'/')
    self.assertEqual(r, 5)

  def test_dzielenie_w_dol(self):
    r = calculate(10, 3,'//')
    self.assertEqual(r, 3)

  def test_modulo(self):
    r = calculate(15, 6,'%')
    self.assertEqual(r, 3)

  def test_potegowanie(self):
    r = calculate(3, 2,'**')
    self.assertEqual(r, 9)