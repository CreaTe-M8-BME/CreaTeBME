"""

 This Demo shows how to plot live data from the sensor.
 The data can either be live from the sensor using the SensorManager,
 or it can be recorded data which is emulated like live data using the SensorEmulator.

 This Demo will show the ease of swapping between live and recorded data.

 If you didn't already record a sensor with the RecorderDemo.py yet, do that first because that data is needed for this demo.
"""
import signal
import sys
import time
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib import style

# Import the CreaTeBME package after installing it with: `pip install CreaTeBME`
from CreaTeBME import SensorEmulator, SensorManager

# Change this to be either using live data or emulate it using the recorded file.
live_data_mode = True
repeat_recording = True
recording_file = 'demoRecording'

# Constants:
sample_rate = 100
axis_names = ["Accelerometer x", "Accelerometer y", "Accelerometer z", "Gyroscope x", "Gyroscope y", "Gyroscope z"]
axis_colors = ["red", "green", "blue"]

# Style the graph (optional)
style.use('ggplot')

# Create sub plots for accelerometer data and gyroscope.
title = f"BME IMU {'live' if live_data_mode else 'recorded'} data plotter demo"
fig, sub_plots = plt.subplots(2, 1, num=title)
fig.set_tight_layout(True)
fig.suptitle(title, fontsize=16)

# Data shown of the graph
time_data = []
acc_data = [[], [], []]
gyro_data = [[], [], []]


# Create either a sensor manager or a sensor emulator depending if live data is needed
# Change 68FE to your sensor name
manager = SensorManager(['68FE']) if live_data_mode else SensorEmulator(recording_file)
manager.set_sample_rate(sample_rate)


def updateGraph(i) -> None:
    """
    UpdateGraph updates the graph with the new measurements to show the live data
    """
    global manager
    measurements = manager.get_measurements()
    for sensor, data in measurements.items():
        if len(data) > 0:
            for data_point in data:
                # calculate the new time, which is the old one (0 if there isn't an old one) plus the step between each sample (one over the sample rate)
                new_time = (time_data[-1] if len(time_data) > 0 else 0) + 1.0 / float(sample_rate)
                time_data.append(new_time)

                # Add all the values of the IMU to the corresponding lists
                for i in range(len(acc_data)):
                    acc_data[i].append(data_point[i])
                    gyro_data[i].append(data_point[i+3])

                # If more than `5` seconds have passed delete the old measurements, so only the last 5 seconds are shown.
                if len(time_data) > sample_rate * 5:
                    time_data.pop(0)
                    for i in range(len(acc_data)):
                        acc_data[i].pop(0)
                        gyro_data[i].pop(0)

    # Update the graph to show the new measurements
    for rowIndex, row in enumerate(sub_plots):
        row.clear()
        for i in range(len(acc_data)):
            row.plot(time_data, acc_data[i] if rowIndex == 0 else gyro_data[i], label=axis_names[rowIndex * 3 + i], color=axis_colors[i])
            row.legend()

        # Update the titles
        sub_plots[0].set_ylabel("Acceleration in g (9.81 m/s^2)", fontsize=8)
        sub_plots[0].set_title('Accelerometer', fontsize=12)
        sub_plots[1].set_ylabel("Rotational velocity in degree/second", fontsize=8)
        sub_plots[1].set_title('Gyroscope', fontsize=12)

    # Once the emulation is over close the graph.
    if not manager.is_running():
        print(f"Emulation ended, {'restarting..' if repeat_recording else 'shutting down...'}")
        if repeat_recording and not live_data_mode:
            manager.stop()
            manager = SensorEmulator(recording_file)
            manager.start()
        else:
            plt.close("all")


# This program does not end on it's own, so the user needs to force exit it.
# When they do so the stop function on the manager is called to neatly close the program.
def user_exit(sig, frame):
    print('closing connection...')
    manager.stop()
    sys.exit(0)


# Register the signal
signal.signal(signal.SIGINT, user_exit)

# Start the sensor manager
manager.start()

# Register the animation function that will be ran given milliseconds (in this case it depends on the sample_rate)
ani = animation.FuncAnimation(fig, updateGraph, interval=(1.0 / float(sample_rate)) * 1000)
plt.show()

manager.stop()
