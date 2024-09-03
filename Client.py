class Client:
    def __init__(self, name, x, y, standard, speed, supports_11k, supports_11v, supports_11r, minimal_rssi):
        self.name = name
        self.x = int(x)
        self.y = int(y)
        self.standard = standard
        self.speed = float(speed)
        self.supports_11k = supports_11k  # Directly use the boolean value
        self.supports_11v = supports_11v  # Directly use the boolean value
        self.supports_11r = supports_11r  # Directly use the boolean value
        self.minimal_rssi = float(minimal_rssi)
        self.current_ap = None
        self.log = []

    def move(self, new_x, new_y):
        self.x = int(new_x)
        self.y = int(new_y)

    def evaluate_ap(self, ap_list):
        best_ap = None
        best_score = None

        for ap in ap_list:
            if ap.can_connect(self):
                rssi = ap.calculate_rssi(self)
                score = self._calculate_score(ap, rssi)
                if best_score is None or score > best_score:
                    best_ap = ap
                    best_score = score

        return best_ap

    def _calculate_score(self, ap, rssi):
        score = rssi
        if ap.standard >= self.standard:
            score += 20  # Bonus for matching or exceeding WiFi standard
        if ap.supports_11k == self.supports_11k:
            score += 10
        if ap.supports_11v == self.supports_11v:
            score += 10
        if ap.supports_11r == self.supports_11r:
            score += 10
        return score

    def connect_to_ap(self, ap, step):
        if self.current_ap:
            self.disconnect_from_ap(step)
        if ap.connect_client(self):
            self.current_ap = ap
            rssi = ap.calculate_rssi(self)
            log_message = f"Step {step}: CLIENT {self.name} CONNECT TO {ap.name} WITH SIGNAL STRENGTH {rssi}"
            self.log.append(log_message)
            ap.log.append(f"Step {step}: {self.name} CONNECT LOCATION {self.x} {self.y} {self.standard} {self.speed} {self.supports_11k} {self.supports_11v} {self.supports_11r}")
            return True
        else:
            log_message = f"Step {step}: CLIENT {self.name} ROAM DENIED"
            self.log.append(log_message)
            return False

    def disconnect_from_ap(self, step):
        if self.current_ap:
            rssi = self.current_ap.calculate_rssi(self)
            log_message = f"Step {step}: CLIENT {self.name} DISCONNECT FROM {self.current_ap.name} WITH SIGNAL STRENGTH {rssi}"
            self.log.append(log_message)
            self.current_ap.log.append(f"Step {step}: {self.name} DISCONNECTS AT LOCATION {self.x} {self.y}")
            self.current_ap.disconnect_client(self)
            self.current_ap = None

    def roam_to_ap(self, new_ap, step):
        if self.current_ap:
            self.disconnect_from_ap(step)
        success = self.connect_to_ap(new_ap, step)
        if success:
            log_message = f"Step {step}: CLIENT {self.name} ROAM FROM {self.current_ap.name} TO {new_ap.name}"
        else:
            log_message = f"Step {step}: CLIENT {self.name} ROAM DENIED"
        self.log.append(log_message)

    def __str__(self):
        return f"Client {self.name} at ({self.x}, {self.y}) connected to {self.current_ap.name if self.current_ap else 'None'}."
