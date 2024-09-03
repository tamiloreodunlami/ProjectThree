import math


class AP:
    def __init__(self, name, x, y, channel, power_level, frequency, standard, supports_11k, supports_11v, supports_11r,
                 coverage_radius, device_limit, minimal_rssi=None):
        self.name = name
        self.x = int(x)
        self.y = int(y)
        self.channel = int(channel)
        self.power_level = float(power_level)
        self.frequency = float(frequency)
        self.standard = standard
        self.supports_11k = supports_11k
        self.supports_11v = supports_11v
        self.supports_11r = supports_11r
        self.coverage_radius = float(coverage_radius)
        self.device_limit = int(device_limit)
        self.minimal_rssi = float(minimal_rssi) if minimal_rssi is not None else None
        self.connected_clients = []
        self.log = []

    def connect_client(self, client):
        if len(self.connected_clients) < self.device_limit and self.can_connect(client):
            self.connected_clients.append(client)
            return True
        return False

    def disconnect_client(self, client):
        if client in self.connected_clients:
            self.connected_clients.remove(client)

    def calculate_rssi(self, client):
        distance = math.sqrt((self.x - client.x) ** 2 + (self.y - client.y) ** 2)
        if distance > self.coverage_radius:
            return float('-inf')  # Signal is too weak if out of coverage
        rssi = self.power_level - 20 * math.log10(distance) - 20 * math.log10(self.frequency) - 32.44
        return rssi

    def can_connect(self, client):
        rssi = self.calculate_rssi(client)
        return rssi >= client.minimal_rssi and (self.minimal_rssi is None or rssi >= self.minimal_rssi)

    def __str__(self):
        return f"AP {self.name} at ({self.x}, {self.y}) on channel {self.channel} with {len(self.connected_clients)}/{self.device_limit} clients."
