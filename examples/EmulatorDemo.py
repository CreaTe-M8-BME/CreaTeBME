"""
    Adapted PrintSensorDemo to use the emulator or the live data depending on the USE_RECORDED_DATA boolean.
    As shown in this example, the sensor emulator and sensor manager can be swapped.
"""

# Import the CreaTeBME package after installing it with: `pip install CreaTeBME`
from CreaTeBME import SensorManager, SensorEmulator

# Options
USE_RECORDED_DATA = False
RECORDING_FILENAME = 'demoRecording'
SAMPLE_RATE = 100

# Create a sensor manager for the given sensor names using the given callback
SENSORS_NAMES = ['0FD6']  # Change 0FD6 to your sensor name, sensor names do not have an O, only zeros (0)
manager = SensorEmulator(RECORDING_FILENAME) if USE_RECORDED_DATA else SensorManager(SENSORS_NAMES)

# Set the sample rate if not using recorded data
if not USE_RECORDED_DATA:
    manager.set_sample_rate(SAMPLE_RATE)

# Start the sensor manager
manager.start()


def loopFunc():
    """
        This function will loop infinitely or the recording has ended and print the sensor data if available.
    """
    global manager
    while True:
        # Get the new sensor measurements
        measurements = manager.get_measurements()

        for sensor, data in measurements.items():
            # Print the sensor data if available
            if len(data) > 0:
                print(sensor, data)

            # Once the emulation is over close the graph.
            if not manager.is_running():
                print(f"Emulation ended, shutting down...")
                return


loopFunc()

# Stop the sensor manager
# In this example it is unreachable because of the while true,
#  but in real code you need to end with manager.stop() to disconnect the sensor
manager.stop()
