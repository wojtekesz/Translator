# Translator podstawieniowy na bazie klucza 'gaderypoluki'
# pl.wikipedia.org/wiki/Gaderypoluki


class CaesarCipher(object):

    # Konstruktor
    def __init__(self):
        self.alphabet = list('abcdefghijklmnopqrstuvwxyz')

    # Główna metoda translacji
    def translate(self, msg, shift):
        result = ""
        
        if msg == None or shift == None or type(shift) == str or type(shift) == float:
            raise Exception('Null message or shift OR string or float shift NOT ALLOWED')
        
        for c in msg:
            if c.isupper():
                if self.alphabet.index(c.lower()) + shift + 1 > len(self.alphabet):
                    if shift >= len(self.alphabet):
                        shift = shift - len(self.alphabet) * (shift // len(self.alphabet))
                    result += self.alphabet[(self.alphabet.index(c.lower()) + shift) - 26].upper()
                else:
                    result += self.alphabet[(self.alphabet.index(c.lower()) + shift)].upper()
            else:
                if self.alphabet.index(c) + shift + 1 > len(self.alphabet):
                    if shift >= len(self.alphabet):
                        shift = shift - len(self.alphabet) * (shift // len(self.alphabet))
                    result += self.alphabet[(self.alphabet.index(c) + shift) - 26]
                else:
                    result += self.alphabet[(self.alphabet.index(c) + shift)]

        return result

    # dodatkowa metoda translacji, ignorująca wielkość znaków
    def translate_ignore_case(self, msg, shift):
        return self.translate(msg.lower(), shift)

    # pobiera aktualną długość klucza szyfrującego
    def get_code_length(self):
        return len(self.alphabet)

    # sprawdza czy znak zostanie przetłumaczony dla danego klucza
    def is_translatable(self, c):
        return c in self.alphabet