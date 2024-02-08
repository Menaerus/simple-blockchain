import unittest
import datetime as date
import sys
sys.path.append('..')
from blockchain import Blockchain,Block

class TestBlockchain(unittest.TestCase):

  def test_verify_genesis(self):
    self.assertTrue(Blockchain(date.datetime.now()).is_valid())

  def test_verify_addingblock(self):
    self.assertTrue(Blockchain(date.datetime.now()).add_block(Block(date.datetime.now(), "First testing block")).is_valid())

  def test_equality(self):
    genesistime = date.datetime.now()
    b1 = Blockchain(genesistime)
    dates = [date.datetime.now() for i in range(100)]
    strings = [f'Equality Testing Block number {number}' for number in range(len(dates))]
    blocks = [Block(dates[i], strings[i]) for i in range(len(dates))]
    b2 = Blockchain(genesistime)
    for b in blocks:
      b1.add_block(b)
      b2.add_block(b)
    self.assertEqual(str(b1), str(b2))

  def test_length(self):
    b = Blockchain(date.datetime.now())
    self.assertEqual(b.length(), 0)
    self.assertEqual(b.add_block(Block(date.datetime.now(), "Un bloque")).length(), 1)

if __name__ == '__main__':
    unittest.main()