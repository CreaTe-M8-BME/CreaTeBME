import time
from CreaTeBME import SensorManager


# Define callback with sensor name and received data parameters
def callback(name, value):
    print(name, value)


# Create a sensor manager for the given sensor names using the given callback
manager = SensorManager(['0BE6'], callback)

# Start the sensor manager
manager.start()

time.sleep(5)
# Change the sample rate of the connected sensors
manager.set_sample_rate(1)
time.sleep(5)

# Stop the sensor manager
manager.stop()
