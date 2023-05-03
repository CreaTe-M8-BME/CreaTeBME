from bleak import BleakScanner
from typing import List
from .ImuSensor import ImuSensor


async def connect(sensor_names: List[str]):
    """
    Find the specified sensors and create ImuSensor objects for them.

    :param sensor_names: The names of the sensors to connect to
    :return: A list of ImuSensor objects
    """
    devices = await BleakScanner.discover(return_adv=True)
    imus = list(filter(lambda x: '0ddf5c1d-d269-4b17-bd7f-33a8658f0b89' in x[1][1].service_uuids, devices.items()))
    chosen_imus = list(filter(lambda x: x[1][1].local_name[-4:] in sensor_names, imus))
    sensors = []
    connected_names = []
    for device in chosen_imus:
        sensor = ImuSensor(device[1][0])
        sensors.append(sensor)
        connected_names.append(device[1][1].local_name[-4:])
    for name in sensor_names:
        if name not in connected_names:
            raise ConnectionError(f"Could not find sensor with name {name}.")
    return sensors
