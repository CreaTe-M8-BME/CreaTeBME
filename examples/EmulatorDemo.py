"""
    Adapted PrintSensorDemo to use the emulator or the live data depending on the live_data_mode boolean.
    As shown in this example, the sensor emulator and sensor manager can be swapped.
"""

# Import the CreaTeBME package after installing it with: `pip install CreaTeBME`
from CreaTeBME import SensorManager, SensorEmulator

# Options
live_data_mode = False
recording_file = 'demoRecording'
sample_rate = 100

# Create a sensor manager for the given sensor names using the given callback
manager = SensorManager(['68FE']) if live_data_mode else SensorEmulator(recording_file)  # Change 68FE to your sensor name. Sensor names do not have an O, only zeros (0)
manager.set_sample_rate(sample_rate)

# Start the sensor manager
manager.start()


def loopFunc():
    """
        This function will loop infinitely or the recording has ended and print the sensor data if availible.
    """
    global manager
    while True:
        measurements = manager.get_measurements()
        for sensor, data in measurements.items():
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
