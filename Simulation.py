from AC import AC
from AP import AP
from Client import Client


class Simulation:
    def __init__(self):
        self.clients = []
        self.aps = []
        self.ac = None
        self.steps = 0

    def load_input(self, filename):
        with open(filename, 'r') as file:
            for line in file:
                parts = line.split()
                if not parts:  # Skip blank lines
                    continue
                if parts[0] == 'AP':
                    self._create_ap(parts)
                elif parts[0] == 'CLIENT':
                    self._create_client(parts)
                elif parts[0] == 'MOVE':
                    self._move_client(parts)

    def _create_ap(self, parts):
        ap_name = parts[1]
        x, y = int(parts[2]), int(parts[3])
        channel = int(parts[4])
        power_level = float(parts[5])
        frequency = self._parse_frequency(parts[6])
        standard = parts[7]
        supports_11k = parts[8].lower() == 'true'
        supports_11v = parts[9].lower() == 'true'
        supports_11r = parts[10].lower() == 'true'
        coverage_radius = float(parts[11])
        device_limit = int(parts[12])
        minimal_rssi = float(parts[13]) if len(parts) > 13 else None

        ap = AP(ap_name, x, y, channel, power_level, frequency, standard, supports_11k,
                supports_11v, supports_11r, coverage_radius, device_limit, minimal_rssi)
        self.aps.append(ap)

    def _create_client(self, parts):
        client_name = parts[1]
        x, y = int(parts[2]), int(parts[3])
        standard = parts[4]
        speed = self._parse_speed(parts[5])
        supports_11k = parts[6].lower() == 'true'
        supports_11v = parts[7].lower() == 'true'
        supports_11r = parts[8].lower() == 'true'
        minimal_rssi = float(parts[9])

        client = Client(client_name, x, y, standard, speed, supports_11k,
                        supports_11v, supports_11r, minimal_rssi)
        self.clients.append(client)

    def _move_client(self, parts):
        client_name = parts[1]
        new_x, new_y = int(parts[2]), int(parts[3])
        client = next(c for c in self.clients if c.name == client_name)
        client.move(new_x, new_y)

    def _parse_frequency(self, freq):
        # If the frequency is in the form "2.4/5", split and handle accordingly
        if '/' in freq:
            return max(map(float, freq.split('/')))  # Choose the higher frequency
        return float(freq)

    def _parse_speed(self, speed):
        # If the speed is in the form "2.4/5", split and handle accordingly
        if '/' in speed:
            return max(map(float, speed.split('/')))  # Choose the higher speed
        return float(speed)

    def run_simulation(self):
        self.ac = AC(self.aps)
        self.ac.manage_channels()

        for client in self.clients:
            best_ap = client.evaluate_ap(self.aps)
            if best_ap:
                if client.connect_to_ap(best_ap, self.steps):
                    self.log_action(
                        f"CLIENT {client.name} CONNECT TO {best_ap.name} WITH SIGNAL STRENGTH {best_ap.calculate_rssi(client)}")
                else:
                    self.log_action(f"CLIENT {client.name} FAILED TO CONNECT TO {best_ap.name}")
            self.steps += 1

    def log_action(self, message):
        print(f"Step {self.steps}: {message}")
        self.steps += 1
