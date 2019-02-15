import unittest

class Complejo(object):
    def __init__(self, real, imag=0):
        self.real = real
        self.imag = imag

    def sumar(self, otro):
        result = Complejo(self.real + otro.real,
                            self.imag + otro.imag)
        return result

    def restar(self, otro):
        result = Complejo(self.real - otro.real,
                            self.imag - otro.imag)
        return result

    def multiplicar(self, otro):
        parte_real = self.real * otro.real - self.imag * otro.imag
        parte_imag = self.real * otro.imag + self.imag * otro.real
        result = Complejo(parte_real, parte_imag)
        return result

    def dividir(self, otro):
        parte_real = ((self.real * otro.real + self.imag * otro.imag) / (otro.real ** 2 + otro.imag ** 2))
        parte_imag = ((self.imag * otro.real - self.real * otro.imag)/ (otro.real ** 2 + otro.imag ** 2))
        result = Complejo(parte_real, parte_imag)
        return result

    def igual(self, otro):
        return self.real == otro.real and self.imag == otro.imag


class TestComplejo(unittest.TestCase):

    def test_sumar(self):
        c1 = Complejo(1,2)
        c2 = Complejo(3,4)

        suma = c1.sumar(c2)

        self.assertEqual(suma.real, 4)
        self.assertEqual(suma.imag, 6)

    def test_restar(self):

        c1 = Complejo(6,1)
        c2 = Complejo(8,4)

        restar = c1.restar(c2)

        self.assertEqual(restar.real, -2)
        self.assertEqual(restar.imag, -3)

    def test_multiplicar(self):
        c1 = Complejo(5,2)
        c2 = Complejo(7,1)

        multiplicar = c1.multiplicar(c2)
        self.assertEqual(multiplicar.real, 33)
        self.assertEqual(multiplicar.imag, 19)

    def test_dividir(self):
        c1 = Complejo(5,2)
        c2 = Complejo(7,1)

        dividir = c1.dividir(c2)
        self.assertEqual(dividir.real, 0.74)
        self.assertEqual(dividir.imag, 0.18)

if __name__ == "__main__":
    unittest.main()
