from CreaTeBME import connect
import asyncio


async def main():
    sensors = await connect()
    print(sensors)
    for sensor in sensors:
        print(await sensor.set_callback(print_measurement))

    while True:
        continue


def print_measurement(data):
    print(data)


task = asyncio.run(main())
