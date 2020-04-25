import unittest

from gaderypoluki.gaderypoluki import GaDeRyPoLuKi


class GaDeRyPoLuKiToolTest(unittest.TestCase):
    g = None

    def setUp(self):
        self.g = GaDeRyPoLuKi()
        pass

    def tearDown(self):
        self.g = None
        pass

    # definicja tablicy krotek, które stanowią wejście do jednego testu
    # każda krotka zawiera wiadomość do przetłumaczenia i oczekiwaną wartość
    test_cases = [
        ("ala", "gug"),
        ("gala", "agug"),
        ("kot", "ipt"),
        ("wonsz", "wpnsz"),
    ]

    # iteracja i kolejne wywołania testów
    def test_should_translate(self):
        for msg, expected in self.test_cases:
            with self.subTest(name=str(msg)):
                result = self.g.translate(msg)
                self.assertEqual(result, expected)
