import unittest
from AP import AP
from Client import Client


class TestAP(unittest.TestCase):
    def test_connect_client(self):
        ap = AP('AP1', 0, 0, 6, 20, 2.4, 'WiFi6', True, True, True, 50, 10)
        client = Client('Client1', 10, 10, 'WiFi6', 5, True, True, True, 70)
        self.assertTrue(ap.connect_client(client))
        self.assertIn(client, ap.connected_clients)

    def test_disconnect_client(self):
        ap = AP('AP1', 0, 0, 6, 20, 2.4, 'WiFi6', True, True, True, 50, 10)
        client = Client('Client1', 10, 10, 'WiFi6', 5, True, True, True, 70)
        ap.connect_client(client)
        ap.disconnect_client(client)
        self.assertNotIn(client, ap.connected_clients)

    def test_calculate_rssi(self):
        ap = AP('AP1', 0, 0, 6, 20, 2.4, 'WiFi6', True, True, True, 50, 10)
        client = Client('Client1', 10, 10, 'WiFi6', 5, True, True, True, 70)
        rssi = ap.calculate_rssi(client)
        self.assertIsInstance(rssi, float)


if __name__ == '__main__':
    unittest.main()
