# To jest miejsce od którego należy zacząć zadanie TDD
# Funkcjonalność rozpoznawania / respektowania wielkości znaków

import unittest

from gaderypoluki.gaderypoluki import GaDeRyPoLuKi

# zbiór testów, uwaga na dziedziczenie
class GaDeRyPoLuKiTest(unittest.TestCase):
    # obiekt, który testujemy
    g = None

    # przed kazdym testem
    def setUp(self):
        self.g = GaDeRyPoLuKi()

    # po kazdym teście
    def tearDown(self):
        self.g = None

    # test
    def test_should_translate_case_consideration(self):
        # given
        msg = "wHATEVER"

        # when
        result = self.g.translate_consider_case(msg)

        # then
        self.assertEqual("wHGTDVDY", result)