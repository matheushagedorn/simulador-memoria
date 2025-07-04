import unittest
from src.memoria import MemoriaPrincipal
from src.swap import AreaSwap

class TestMemoriaPrincipal(unittest.TestCase):

    def setUp(self):
        self.memoria = MemoriaPrincipal(capacidade=3)
        self.swap = AreaSwap()

    def test_adicionar_processos(self):
        self.memoria.adicionar_processo('P1')
        self.memoria.adicionar_processo('P2')
        self.memoria.adicionar_processo('P3')
        self.assertEqual(self.memoria.processos, ['P1', 'P2', 'P3'])

    def test_memoria_cheia(self):
        self.memoria.adicionar_processo('P1')
        self.memoria.adicionar_processo('P2')
        self.memoria.adicionar_processo('P3')
        resultado = self.memoria.adicionar_processo('P4')
        self.assertEqual(resultado, 'P1 removido para a swap.')
        self.assertEqual(self.swap.processos, ['P1'])
        self.assertEqual(self.memoria.processos, ['P2', 'P3', 'P4'])

    def test_substituicao_fifo(self):
        self.memoria.adicionar_processo('P1')
        self.memoria.adicionar_processo('P2')
        self.memoria.adicionar_processo('P3')
        self.memoria.adicionar_processo('P4')  # P1 deve ser removido
        self.assertEqual(self.swap.processos, ['P1'])
        self.assertEqual(self.memoria.processos, ['P2', 'P3', 'P4'])

    def test_recuperar_da_swap(self):
        self.memoria.adicionar_processo('P1')
        self.memoria.adicionar_processo('P2')
        self.memoria.adicionar_processo('P3')
        self.memoria.adicionar_processo('P4')  # P1 vai para swap
        self.swap.recuperar_processo('P1')
        self.assertIn('P1', self.memoria.processos)
        self.assertNotIn('P1', self.swap.processos)

if __name__ == '__main__':
    unittest.main()