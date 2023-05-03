import time
from CreaTeBME import SensorManager, SensorEmulator


# Define callback with sensor name and received data parameters
def callback(name, value):
    print(name, value)


# Create a sensor manager for the given sensor names using the given callback
# manager = SensorManager(['0BE6'])
manager = SensorEmulator('test')
manager.start()
manager.set_sample_rate(142)
# while len(manager.get_measurements()['2F82']) < 1 or len(manager.get_measurements()['890E']) < 1:
#     print('waiting')

# manager.record('test', 5)
manager.get_measurements()
print('start measurement')
time.sleep(10)
manager.stop()
measurements = manager.get_measurements()

for sensor, data in measurements.items():
    if len(data) > 0:
        print(sensor, len(data))
    print(data)
