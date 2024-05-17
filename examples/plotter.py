from CreaTeBME import SensorManager
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import time
import numpy as np

# Sensor constants
FREQUENCY       = 60
BUFFER_SIZE     = FREQUENCY * 5
SENSORS_NAMES   = ['1886']
AXIS_NAMES      = ["X", "Y", "Z"]

# Create Datastructures for sensor data
t_stamp    = {name: np.array([0.])       for name in SENSORS_NAMES}
acc        = {name: np.array([[0,0,0]]) for name in SENSORS_NAMES}
gyr        = {name: np.array([[0,0,0]]) for name in SENSORS_NAMES}

# Define animation function used for plotting
def animate(i) -> None:
    # Get the new sensor measurements
    for name, data in manager.get_measurements().items():
        print(data)
        # If no new measurement available, continue
        if not data: continue

        for element in data:
            acc[name]        = np.vstack((acc[name][-BUFFER_SIZE:], element[:3]))
            gyr[name]        = np.vstack((gyr[name][-BUFFER_SIZE:], element[3:]))
            t_stamp[name]    = np.append(t_stamp[name][-BUFFER_SIZE:], t_stamp[name][-1] + 1.0 / FREQUENCY)

    for i, name in enumerate(SENSORS_NAMES):
        if not acc[name][-1, 0]: continue

        axis[i][0].cla()
        # axis[i][0].plot(t_stamp[name], acc[name], label=AXIS_NAMES)
        # axis[i][0].legend()

        axis[i][1].cla()
        # axis[i][1].plot(t_stamp[name], gyr[name], label=AXIS_NAMES)
        # axis[i][1].legend()



        plot1 = np.arctan(-acc[name][:, 2]/np.sqrt(np.power(acc[name][:, 0], 2) + np.power(acc[name][:, 1], 2)))
        plot2 = np.degrees(plot1)

        axis[i][0].plot(plot1)
        axis[i][1].plot(plot2)

# Create a sensor manager for the given sensor names and set sample rate
manager = SensorManager(SENSORS_NAMES)
manager.set_sample_rate(FREQUENCY)

start_time = time.time()

fig, axis = plt.subplots(2,2)
fig.tight_layout()

if __name__ == '__main__':
    # Start the sensor manager
    manager.start()

    # Start the animation plotter
    ani = animation.FuncAnimation(fig, animate, interval=(1000.0 / float(FREQUENCY)), cache_frame_data=False)
    plt.show()

    # Stop the sensor manager
    manager.stop()