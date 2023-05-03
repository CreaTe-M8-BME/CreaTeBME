"""
 This demo shows how to record data using the recorder in the sensor manager.
 The recorded data will be saved in a .tb file and can be used to emulate data in via the emulator
 EmulatorDemo.py show how to emulate the data that is recorded in this demo.

 Recording and emulating data makes it easier to work with multiple people on a single sensor
 because it makes sure you do not have to connect and move the sensor to test your code.
"""

# Import the CreaTeBME package after installing it with: `pip install CreaTeBME`
from CreaTeBME import SensorManager

# Constants:
sample_rate = 100

# Create a sensor manager for the given sensor names using the given callback
manager = SensorManager(['68FE'])  # Change the 68FE to the code of your sensor!!
manager.set_sample_rate(sample_rate)
manager.start()

# Create a recording for 10 seconds and save it in a new file called demoRecording.
# If the file already exists it will give an error, so if you want to record new data delete the old one first.
print("Recording IMU for 10 seconds...")
manager.record('demoRecording', seconds=10)
print("Done recording IMU saved as 'demoRecording.tb', shutting down")

manager.stop()
