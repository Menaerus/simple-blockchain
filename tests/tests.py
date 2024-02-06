import unittest
import datetime as date
import sys
sys.path.append('..')
from blockchain import Blockchain,Block

class TestBlockchain(unittest.TestCase):

  def test_verify_genesis(self):
    self.assertTrue(Blockchain().is_valid())

  def test_verify_addingblock(self):
    self.assertTrue(Blockchain().add_block(Block(1, date.datetime.now(), "First testing block", "")).is_valid())

if __name__ == '__main__':
    unittest.main()