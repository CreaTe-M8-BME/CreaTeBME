from CreaTeBME import connect
import asyncio


async def main():
    sensors = await connect()

    while True:
        for sensor in sensors:
            measurement = sensor.take_measurement()
            print(measurement)

asyncio.run(main())