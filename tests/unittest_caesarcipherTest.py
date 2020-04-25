import unittest

from caesarcipher.caesarcipher import CaesarCipher

# zbiór testów, uwaga na dziedziczenie
class CaesarCipherTest(unittest.TestCase):
    # obiekt, który testujemy
    g = None

    # przed kazdym testem
    def setUp(self):
        self.g = CaesarCipher()

    # po kazdym teście
    def tearDown(self):
        self.g = None

    # test
    def test_should_translate(self):
        # given
        msg = "lokok"
        shift = 2

        # when
        result = self.g.translate(msg, shift)

        # then
        self.assertEqual("nqmqm", result)
    
    def test_should_translate2(self):
        # given
        msg = "whatever"
        shift = 3

        # when
        result = self.g.translate(msg, shift)

        # then
        self.assertEqual("zkdwhyhu", result)

    def test_should_throw_exception(self):
        # given

        # when
        with self.assertRaises(Exception):
            self.g.translate(None, None)

        # then

    
    def test_should_translate_ignore(self):
        # given
        msg = "KOT"
        shift = 2
        
        # when
        result = self.g.translate_ignore_case(msg, shift)

        # then
        self.assertEqual("mqv", result)

    def test_should_check_not_translatable(self):
        # given
        c = "#"

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
        self.assertEqual(26, size)