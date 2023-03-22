import threading
import time

from CreaTeBME import connect
import asyncio

import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib import style

sample_rate: int = 100

style.use('seaborn-v0_8-whitegrid')
fig, plots = plt.subplots(2)

time_data = []
axis_names = ["X", "Y", "Z"]

accelerometer_data = [[], [], []]
gyroscope_data = [[], [], []]

sensors = []

data_mutex = threading.Lock()


async def connect_sensors():
    while len(sensors) == 0:
        sensors.extend(await connect())
    print(f"connect_sensors: {sensors = }")
    await setupSensors()


def worker():
    loop = asyncio.new_event_loop()
    task = loop.create_task(connect_sensors())
    loop.run_forever()


def print_measurement(data):
    global i
    print(f"{data = }")

    data_mutex.acquire()
    time_data.append(time.time())
    for i, acc_list in enumerate(accelerometer_data):
        acc_list.append(data[i])
    for i, gyro_list in enumerate(gyroscope_data):
        gyro_list.append(data[i+3])

    if len(time_data) > sample_rate*5:
        time_data.pop(0)
        for acc_list, gyro_list in zip(accelerometer_data, gyroscope_data):
            acc_list.pop(0)
            gyro_list.pop(0)
    data_mutex.release()


def animateGraph(i):
    plots[0].clear()
    plots[1].clear()

    data_mutex.acquire()
    for index, acc_data in enumerate(accelerometer_data):
        plots[0].plot(time_data, acc_data, label=axis_names[index])
    for index,  gyro_data in enumerate(gyroscope_data):
        plots[1].plot(time_data, gyro_data, label=axis_names[index])
    data_mutex.release()

    plots[0].legend()
    plots[1].legend()
    plots[0].set_title("Accelerometer data")
    plots[1].set_title("Gyroscope data")


async def setupSensors():
    print(f"setupSensors: {sensors = }")
    for sensor in sensors:
        await sensor.set_callback(print_measurement)
        await sensor.set_sample_rate(sample_rate)

ani = animation.FuncAnimation(fig, animateGraph, interval=1000/sample_rate)
threading.Thread(target=worker).start()

fig.tight_layout()
plt.show()

