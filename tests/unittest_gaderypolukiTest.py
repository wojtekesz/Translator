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
    def test_should_translate(self):
        # given
        msg = "lok"

        # when
        result = self.g.translate(msg)

        # then
        self.assertEqual("upi", result)

    # uwaga na klauzulę wyłączającą test
    
    def test_should_stay_not_translated(self):
        # given
        msg = "LOK"

        # when
        result = self.g.translate(msg)

        # then
        self.assertEqual("LOK", result)

    
    def test_should_translate2(self):
        # given
        msg = "whatever"

        # when
        result = self.g.translate(msg)

        # then
        self.assertEqual("whgtdvdy", result)

    def test_should_throw_exception(self):
        # given

        # when
        with self.assertRaises(Exception):
            self.g.translate(None)

        # then

    
    def test_should_translate_ignore(self):
        # given
        msg = "KOT"

        # when
        result = self.g.translate_ignore_case(msg)

        # then
        self.assertEqual("ipt", result)

    def test_should_check_not_translatable(self):
        # given
        c = "Z"

        # when
        result = self.g.is_translatable(c)

        # then
        self.assertFalse(result)

    
    def test_should_check_translatable(self):
        # given
        c = "g"

        # when
        result = self.g.is_translatable(c)

        # then
        self.assertTrue(result)

    
    def test_should_check_code_length(self):
        # given

        # when
        size = self.g.get_code_length()

        # then
        self.assertEqual(12, size)
