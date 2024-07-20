import unittest
from funksiya import kattasi_top, juft_top, matn_katta_qil
class KattaTest(unittest.TestCase):
  def test_katta_aniqla(self):
    self.assertEqual(kattasi_top(2, 4, 9), 9)
    self.assertEqual(kattasi_top(4, 4, 9), 9)
    self.assertEqual(kattasi_top(2, 4, 2), 4)
    self.assertEqual(kattasi_top(0.1, -1, -1), 0.1)

class JuftTest(unittest.TestCase):
  def test_juftni_top(self):
    self.assertEqual(juft_top([2,4,6,1,8,9]), [2, 4, 6, 8] )
    self.assertEqual(juft_top([2,-2, 4, 12, 0, 7]), [2, 4, 12, 0])

class MatnTest(unittest.TestCase):
  def test_matn_kattalashtir(self):
    self.assertEqual(matn_katta_qil(['salom qarindosh', 'sarvaR olim', 1, 'QaLaysan jamshid']), ['Salom qarindosh', 'Sarvar olim', 1, 'Qalaysan jamshid'])
unittest.main()
