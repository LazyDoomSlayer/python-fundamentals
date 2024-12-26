import time


class IndoorSensorSimulation:
    def __init__(self, indoor_sensor, mqtt_manager):
        self.indoor_sensor = indoor_sensor
        self.mqtt_manager = mqtt_manager

    def simulate(self):
        """Simulate the indoor sensor and publish its data."""
        while True:
            self.simulate_step()
            time.sleep(3)  # Simulate every 3 seconds

    def simulate_step(self):
        """Simulate one step for the indoor sensor."""
        if self.indoor_sensor.powered:
            data = self.indoor_sensor.generate_data()
            for key, value in data.items():
                topic = f"home/{self.indoor_sensor.group_id}/{self.indoor_sensor.device_type}/{self.indoor_sensor.device_id}/{key}/update"
                self.mqtt_manager.publish(topic, value)
                print(f"Published to {topic}: {value}")
        else:
            print(
                f"{self.indoor_sensor.device_type} {self.indoor_sensor.device_id} is powered OFF."
            )
