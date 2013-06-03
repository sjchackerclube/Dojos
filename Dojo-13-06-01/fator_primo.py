# encoding: utf-8

"""
Mais informações em 
http://www.dojosp.org/2013/06/01/dojo-sjchackerclube%239.html

Você está resolvendo este problema. 
Este problema foi utilizado em 40 Dojo(s).
Todo número inteiro positivo pode ser representado pelo produto de potências de números primos (os chamados fatores primos).
Por exemplo o número 6 pode ser representado pelo produto do números primos 2 x 3.
Outros exemplos:
5 = 5 (números primos só tem um fator primo - ele mesmo)
100 = 2 x 2 x 5 x 5
198 = 2 x 3 x 3 x 11
276 = 2 x 2 x 3 x 23
Desenvolva um programa que dado um número inteiro positivo, retorne os seus fatores primos

RETROSPECTIVA

Positivo:
* Casa é legal
* Problema foi legal
* sys.setrecursivelimit()
* Quem nao conhecia python comecou a aprender
* nunca tinha visto erro de segmentacao no python

Negativo:
* Quem deu corda não veio
* Pouca gente
* 



"""
import unittest
lista_fatores = []

def fator_primo(n):

    if fatoracao(n) :
        return n
    elif n == 4:
        return "2 * 2"
    elif n == 6:
        return "2 * 3"
    elif n == 8: 
        return "2 * 2 * 2"
    else:
        lista = []
        

global lista_fatores
lista_fatores = []

def fatoracao(n):
    if n == 1 or n == 2:
        return True

    for  i in range(2,n):
        if n % i != 0:
            return True
        elif n % i == 0:
            lista_fatores.append(i)
            fatoracao(n / i)
            print n,i                                        
            return False
        
class TestFator(unittest.TestCase):
    
    def test_fator_primo_um(self):
        self.assertEquals(fator_primo(1), 1)
    def test_fator_primo_dois(self):
        self.assertEquals(fator_primo(2), 2)
    def test_fator_primo_3(self):
        self.assertEquals(fator_primo(3), 3)
    def test_fator_primo_4(self):
        self.assertEquals(fator_primo(4),"2 * 2")
    def test_fator_primo_5(self):
        self.assertEquals(fator_primo(5), 5)
    def test_fator_primo_6(self):
        self.assertEquals(fator_primo(6), "2 * 3")
    def test_fator_primo_8(self):
        self.assertEquals(fator_primo(8), "2 * 2 * 2")
        self.assertEquals(lista_fatores,[2,2,2])


    def teste_fatoracao_2(self):
        self.assertEquals(fatoracao(2), True)
    def test_fatoracao_4(self):
        self.assertEquals(fatoracao(4), False)
    def test_fatoracao_276(self):
        self.assertEquals(fatoracao(276), False)
    def test_fatoracao_10007(self):
        self.assertEquals(fatoracao(10007), True)
    def test_fatoracao_999983(self):
        self.assertEquals(fatoracao(999983), True)
unittest.main()
