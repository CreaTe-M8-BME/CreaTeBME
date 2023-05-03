import threading
import time

from CreaTeBME import connect
import asyncio

sensors = []


async def connect_sensors():
    sensors.extend(await connect())
    print(sensors)

def worker():
    loop = asyncio.new_event_loop()
    task = loop.create_task(connect_sensors())
    loop.run_forever()


def print_measurement(data):
    print('Sensor data:', data)
    pass


async def main():
    print(sensors)
    for sensor in sensors:
        await sensor.set_callback(print_measurement)
        await sensor.set_sample_rate(100)



threading.Thread(target=worker).start()

asyncio.run(main())

