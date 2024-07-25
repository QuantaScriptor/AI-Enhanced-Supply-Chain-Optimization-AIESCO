
import unittest
import numpy as np
from aiesco import SupplyChainOptimization

class TestAIESCO(unittest.TestCase):
    def setUp(self):
        self.data = np.random.rand(100, 10)
        self.target = np.random.randint(2, size=100)
        self.aiesco = SupplyChainOptimization()

    def test_train_model(self):
        self.aiesco.train_model(self.data, self.target)
        self.assertIsNotNone(self.aiesco.model)

    def test_optimize_supply_chain(self):
        self.aiesco.train_model(self.data, self.target)
        optimization = self.aiesco.optimize_supply_chain(self.data[:5])
        self.assertEqual(len(optimization), 5)

if __name__ == '__main__':
    unittest.main()
