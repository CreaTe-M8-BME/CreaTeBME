import threading
import time

from CreaTeBME import connect
import asyncio

sensors = []


async def connect_sensors():
    sensors.extend(await connect())
    print(sensors)


    # while True:
    #     await asyncio.sleep(1)

def worker():
    loop = asyncio.new_event_loop()
    task = loop.create_task(connect_sensors())
    loop.run_forever()


def print_measurement(data):
    print('het werkt:', data)
    pass


async def main():
    print(sensors)
    for sensor in sensors:
        await sensor.set_callback(print_measurement)
        await sensor.set_sample_rate(100)

    print('yay')


threading.Thread(target=worker).start()

asyncio.run(main())

