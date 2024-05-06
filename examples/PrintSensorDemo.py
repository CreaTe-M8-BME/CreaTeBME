# Import the CreaTeBME package after installing it with: `pip install CreaTeBME`
from CreaTeBME import SensorManager

# Create a sensor manager for the given sensor names using the given callback
manager = SensorManager(['0BE6'])  # Change 0BE6 to your sensor name. Sensor names do not have an O, only zeros (0)
manager.set_sample_rate(120)

# Start the sensor manager
manager.start()

while True:
    measurements = manager.get_measurements()
    for sensor, data in measurements.items():
        if len(data) > 0:
            print(sensor, data)

# Stop the sensor manager
# In this example it is unreachable because of the while true,
#  but in real code you need to end with manager.stop() to disconnect the sensor
manager.stop()
