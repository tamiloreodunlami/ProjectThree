import unittest
from AC import AC
from AP import AP
from Client import Client


class TestAC(unittest.TestCase):
    def test_manage_channels(self):
        ap1 = AP('AP1', 0, 0, 6, 20, 2.4, 'WiFi6', 'true', 'true', 'true', 50, 10)
        ap2 = AP('AP2', 100, 100, 7, 20, 5, 'WiFi6', 'true', 'true', 'true', 50, 10)
        ac = AC([ap1, ap2])

        ac.manage_channels()
        self.assertIn(ap1.channel, [1, 6, 11])
        self.assertIn(ap2.channel, [1, 6, 11])

    def test_request_roam(self):
        ap = AP('AP1', 0, 0, 6, 20, 2.4, 'WiFi6', 'true', 'true', 'true', 50, 10)
        ac = AC([ap])
        client = Client('Client1', 0, 0, 'WiFi6', 2, 'true', 'true', 'true', 73)

        ac.request_roam(client, ap)
        # Check the output or log the action in your main system


if __name__ == '__main__':
    unittest.main()
