import unittest
from Simulation import Simulation


class TestSimulation(unittest.TestCase):
    def test_load_input(self):
        sim = Simulation()
        sim.load_input('input.txt')
        self.assertEqual(len(sim.aps), 2)
        self.assertEqual(len(sim.clients), 1)

    def test_run_simulation(self):
        sim = Simulation()
        sim.load_input('input.txt')
        sim.run_simulation()
        # You can assert the state of clients and APs after simulation
        client = sim.clients[0]
        self.assertIsNotNone(client.current_ap)


if __name__ == '__main__':
    unittest.main()
