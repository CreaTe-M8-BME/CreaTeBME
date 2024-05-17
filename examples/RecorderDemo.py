"""
 This demo shows how to record data using the recorder in the sensor manager.
 The recorded data will be saved in a .tb file and can be used to emulate data in via the emulator
 PlotterDemo.py show how to emulate the data that is recorded in this demo as if it is live data.

 Recording and emulating data makes it easier to work with multiple people on a single sensor
 because it makes sure you do not have to connect and move the sensor to test your code.
"""

# Import the CreaTeBME package after installing it with: `pip install CreaTeBME`
from CreaTeBME import SensorManager

# Constants:
SAMPLE_RATE = 100
FILE_NAME = 'demoRecording'
RECORDING_TIME = 10

# Create a sensor manager for the given sensor names using the given callback
manager = SensorManager(['68FE'])  # Change the 68FE to the code of your sensor
manager.set_sample_rate(SAMPLE_RATE)
manager.start()

# Create a recording for given seconds and save it in a new file called demoRecording.
# If the file already exists it will give an error, so if you want to record new data delete the old one first.
print(f"Recording IMU for {RECORDING_TIME} seconds...")
manager.record(FILE_NAME, seconds=RECORDING_TIME)
print(f"Done recording IMU saved as '{FILE_NAME}.tb', shutting down")

manager.stop()
