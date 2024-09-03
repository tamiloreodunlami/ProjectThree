class AC:
    def __init__(self, aps):
        self.aps = aps
        self.step = 0
        self.log = []

    def manage_channels(self):
        preferred_channels = [1, 6, 11]
        for ap in self.aps:
            if ap.channel not in preferred_channels:
                new_channel = preferred_channels[-1]  # Simplified logic for demonstration
                self.log_channel_change(ap, new_channel)
                ap.channel = new_channel

    def log_channel_change(self, ap, new_channel):
        log_message = f"Step {self.step}: AC REQUIRES {ap.name} TO CHANGE CHANNEL TO {new_channel}"
        self.log.append(log_message)
        ap.log.append(log_message)

    def request_roam(self, client, ap):
        log_message = f"Step {self.step}: Requesting {client.name} to roam to {ap.name}"
        self.log.append(log_message)
