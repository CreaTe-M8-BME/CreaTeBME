"""
 This Demo shows a stripped down way to plot live data from the sensor.
 It only supports one sensor to keep the code simple and easy to understand.

 Steps to run this demo:
    1. Change the sensor name in `SensorManager()` to the name of the sensor you want to use.
    2. Run the code and see the live data plot.
"""

# Prevent PyCharm from taking over control of the plot window backend
# Only needed if you want to run this code in PyCharm
import os
import matplotlib
if os.name == 'posix':
    matplotlib.use("macosx")
else:
    matplotlib.use("tkagg")

import matplotlib.animation as animation
import matplotlib.pyplot as plt
import numpy as np
from CreaTeBME import SensorManager

# Sensor data
SAMPLE_RATE = 100
BUFFER_SIZE = SAMPLE_RATE * 5
axis_names = ["X", "Y", "Z"]

# Sensor data
time_data = np.array([0.])
acc_data = np.array([[0, 0, 0]])
gyr_data = np.array([[0, 0, 0]])

# Setup sensor
manager = SensorManager(['0BE6'], SAMPLE_RATE)  # Ensure this line is before the Matplotlib setup

# Matplotlib setup
fig, sub_plots = plt.subplots(1, 2)
fig.tight_layout()  # Ensure the plots don't overlap


def updateSensorData() -> None:
    """
     Retrieves and updates the sensor data
    """
    global time_data, acc_data, gyr_data
    for sensor, data in manager.get_measurements().items():
        for data_point in data:
            # Update sensor data
            acc_data = np.vstack((acc_data[-BUFFER_SIZE:], data_point[:3]))
            gyr_data = np.vstack((gyr_data[-BUFFER_SIZE:], data_point[3:]))
            time_data = np.append(time_data[-BUFFER_SIZE:], time_data[-1] + 1 / SAMPLE_RATE)


def plotGraph() -> None:
    """
     Plot the sensor data on the graph
    """
    # Plain accelerometer data
    sub_plots[0].clear()
    sub_plots[0].plot(time_data, acc_data, label=axis_names)
    sub_plots[0].legend(loc='upper right')

    # Plain gyroscope data
    sub_plots[1].clear()
    sub_plots[1].plot(time_data, gyr_data, label=axis_names)
    sub_plots[1].legend(loc='upper right')


def updateGraph(i):
    # Retrieve new sensor data
    updateSensorData()

    # Plot the data on the graph
    plotGraph()


# Start function
if __name__ == "__main__":
    # Start the sensor manager
    manager.start()

    # Start the animation
    ani = animation.FuncAnimation(fig, updateGraph, interval=1000.0 / SAMPLE_RATE, cache_frame_data=False)
    plt.show()

    # Stop the sensor manager
    manager.stop()
