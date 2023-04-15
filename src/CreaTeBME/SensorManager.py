from threading import Thread
import asyncio
from .connect import connect
from typing import Callable


class SensorManager:
    def __init__(self, sensor_names: list[str], callback: Callable[[str, list[float]], None], sample_rate: int = 100) -> None:
        self._sensors = []
        self._sample_rate = sample_rate
        self._stopping = False
        self._thread = None
        self._loop = asyncio.new_event_loop()

        # Connect sensors
        self._loop.run_until_complete(self._create_sensors(sensor_names))
        self.set_callback(callback)

    def start(self) -> None:
        if not self._thread:
            self._thread = Thread(target=self._run)
        self._thread.start()

    def stop(self) -> None:
        if self._loop.is_running():
            self._loop.stop()

    def _run(self) -> None:
        if not self._loop:
            self._loop = asyncio.new_event_loop()
        self._loop.create_task(self._connect_sensors())
        self._loop.run_forever()

    async def _connect_sensors(self) -> None:
        for sensor in self._sensors:
            await sensor.connect()
        await self._set_sample_rate()

    async def _create_sensors(self, sensor_names) -> None:
        self._sensors.extend(await connect(sensor_names))

    def set_callback(self, callback: Callable[[str, list[float]], None]) -> None:
        for sensor in self._sensors:
            sensor.set_callback(callback)

    async def _set_sample_rate(self) -> None:
        for sensor in self._sensors:
            await sensor.set_sample_rate(self._sample_rate)

    def set_sample_rate(self, sample_rate: int = None) -> None:
        if sample_rate:
            self._sample_rate = sample_rate
        self._loop.create_task(self._set_sample_rate())

    def __del__(self):
        self._loop.stop()
