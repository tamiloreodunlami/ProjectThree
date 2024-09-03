import unittest
from Client import Client
from AP import AP


class TestClient(unittest.TestCase):
    def test_move(self):
        client = Client('Client1', 0, 0, 'WiFi6', 2, 'true', 'true', 'true', 73)
        client.move(20, 20)
        self.assertEqual(client.x, 20)
        self.assertEqual(client.y, 20)

    def test_connect_to_ap(self):
        client = Client('Client1', 0, 0, 'WiFi6', 2, 'true', 'true', 'true', 73)
        ap = AP('AP1', 0, 0, 6, 20, 2.4, 'WiFi6', 'true', 'true', 'true', 50, 10)
        self.assertTrue(client.connect_to_ap(ap))
        self.assertEqual(client.current_ap, ap)

    def test_roaming_to_better_ap(self):
        client = Client('Client1', 0, 0, 'WiFi6', 2, 'true', 'true', 'true', 73)
        ap1 = AP('AP1', 0, 0, 6, 10, 2.4, 'WiFi6', 'true', 'true', 'true', 50, 10)
        ap2 = AP('AP2', 100, 100, 6, 20, 5, 'WiFi6', 'true', 'true', 'true', 60, 10)

        client.connect_to_ap(ap1)
        self.assertEqual(client.current_ap, ap1)

        best_ap = client.evaluate_ap([ap1, ap2])
        self.assertEqual(best_ap, ap2)


if __name__ == '__main__':
    unittest.main()
