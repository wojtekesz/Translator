# Translator podstawieniowy na bazie klucza 'gaderypoluki'
# pl.wikipedia.org/wiki/Gaderypoluki


class GaDeRyPoLuKi(object):

    # Konstruktor
    def __init__(self):
        self.map = {"g": "a", "a": "g", "d": "e", "e": "d", "r": "y", "y": "r", "p": "o", "o": "p", "l": "u", "u": "l",
                    "k": "i", "i": "k"}

    # Główna metoda translacji
    def translate(self, msg):
        result = ""
        if msg is None:
            raise Exception('Null msg not allowed')
        for c in msg:
            if c in self.map.keys():
                result += self.map[c]
            else:
                result += c

        return result

    # dodatkowa metoda translacji, ignorująca wielkość znaków
    def translate_ignore_case(self, msg):
        return self.translate(msg.lower())

    # sprawdza czy znak zostanie przetłumaczony dla danego klucza
    def is_translatable(self, c):
        return c in self.map.keys()

    # pobiera aktualną długość klucza szyfrującego
    def get_code_length(self):
        return len(self.map.keys())

    # dodatkowa metoda translacji, uwzględniająca wielkość znaków
    def translate_consider_case(self, msg):
        result = ""
        if msg is None:
            raise Exception('Null msg not allowed')
        for c in msg:
            if c.isupper():
                c_lower = c.lower()
                if c_lower in self.map.keys():
                    result += self.map[c_lower].upper()
                else:
                    result += c
            elif c in self.map.keys():
                result += self.map[c]
            else:
                result += c

        return result