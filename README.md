# CreaTeBME
Python Package for interfacing the bluetooth IMU module for CreaTe M8 BME.

# Installation
To install the latest stable version simply run
```shell
pip install CreaTeBME
```

# Example
A simple example to connect to a sensor and read and print the data for 10 seconds.
```python
import time
from CreaTeBME import SensorManager

# Define callback with sensor name and received data parameters
def callback(name, value):
    print(name, value)

# Create a sensor manager for the given sensor names using the given callback
manager = SensorManager(['0BE6'], callback)

# Start the sensor manager
manager.start()

time.sleep(10)

# Stop the sensor manager
manager.stop()
```

# Usage

## SensorManager (asyncio wrapper)
This package uses [Bleak](https://github.com/hbldh/bleak) for the bluetooth communication.
Bleak uses asyncio, thus this package has to use this too.
To ease usage, a wrapper has been made for people not experienced with asyncio.
This wrapper also automates the connection of the sensors over bluetooth.

To connect to the sensors, simply initialize a `SensorManager` object with the sensor names and callback.
```python
from CreaTeBME import SensorManager

manager = SensorManager(['A1B2', 'C3D4'], callback)
```

The callback must be a function that takes 2 parameters: the sensor name and the read data.
```python
def callback(name, data):
    print(name, data)
```

The data passed to the callback is a list of floats.
The list is structured like this
- **[0:2]** = x,y,z of accelerometer in (g).
- **[3:5]** = x,y,z of gyroscope in (deg/s).

To start reading data from the sensors call the `start` method of the `SensorManager`.
```python
manager.start()
```

Make sure to also call the `stop` method when exiting your program.
```python
manager.stop()
```
## Manual Connection
⚠️**Understanding of** asyncio **required**⚠️

Another way of connecting IMU sensors is to manually create `ImuSensor` objects.
This can be done by specifying the BLE device that should be connected as a sensor.
```python
from CreaTeBME import ImuSensor

sensor = ImuSensor(device)
```

The device has to be a Bleak _BLEDevice_ object that can be acquired using the `discover` method of `BleakScanner`.
```python
from bleak import BleakScanner
from CreaTeBME import ImuSensor

async def connect():
    devices = await BleakScanner.discover(return_adv=True)
    sensor = ImuSensor(devices[0])
```

# API Reference

## Helpers

### `connect(sensor_names: list[str])`

Finds the IMU devices corresponding with the given list, create a ImuSensor object for each and return a list of ImuSensor objects.

## ImuSensor

Class for IMU sensor communication.

### `ImuSensor(device: BLEDevice, callback: (name: str, data: list[float]) -> None = None, name: str = None)`

Initialize an ImuSensor object.

Calls a callback whenever a sensor measurement is received.
Where name is the friendly name of the sensor and data:
- **[0:2]** = x,y,z of accelerometer in (g).
- **[3:5]** = x,y,z of gyroscope in (deg/s).

#### Parameters

- **device** - The Bleak BLEDevice instance of the sensor that should be connected to.
- **callback** - The callback to be called whenever a measurement from the sensor is received.
- **name** - A friendly name sent to the callback to identify the sensor.

### `ImuSensor.connect() -> None`

Connect to the bluetooth device

### `ImuSensor.set_sample_rate(sample_rate: int) -> None`

Set the sample rate in Hz at which the sensor should take measurements.

#### Parameters

- **sample_rate** - The sample rate in Hz.

### `ImuSensor.set_callback(callback: (name: str, data: list[float]) -> None) -> None`

Set the callback that should be called when a measurement is received from the sensor.

Where name is the friendly name of the sensor and data:
- **[0:2]** = x,y,z of accelerometer in (g).
- **[3:5]** = x,y,z of gyroscope in (deg/s).

#### Parameters

- **callback** - A function to be called when a measurement is received. Takes the sensor name and the measurement data as parameters.

### `ImuSensor.get_reading() -> list[float]`

Return the most recent measurement as a list of floats with:
- **[0:2]** = x,y,z of accelerometer in (g).
- **[3:5]** = x,y,z of gyroscope in (deg/s).

## SensorManager
Class for easy sensor connection without asyncio knowledge.

### `SensorManager(sensor_names: list[str], callback: (name: str, data: list[float]) -> None, sample_rate: int = 100)`

Initialize a SensorManager object.
Connects the given sensors and sets their callback and sample rate.
Holds internal `ImuSensor` objects.

Where name is the friendly name of the sensor and data:
- **[0:2]** = x,y,z of accelerometer in (g).
- **[3:5]** = x,y,z of gyroscope in (deg/s).

#### Parameters

- **sensor_names** - The names of the sensors to connect to.
- **callback** - The callback to be set for the ImuSensor objects.
- **sample_rate** - The sample rate in Hz to be set for the ImuSensor objects.

### `SensorManager.start() -> None`

Start the ImuSensor objects to listen for measurements.

### `SensorManager.stop() -> None`

Stops the ImuSensors from listening for measurements

### `SensorManager.set_callback(callback: (name: str, data: list[float]) -> None) -> None`

Sets the callback for all ImuSensor objects within this SensorManager.

Where name is the friendly name of the sensor and data:
- **[0:2]** = x,y,z of accelerometer in (g).
- **[3:5]** = x,y,z of gyroscope in (deg/s).

#### Parameters

- **callback** - The callback function to set for the ImuSensor objects.

### `SensorManager.set_sample_rate(sample_rate: int) -> None`

Sets the sample rate in Hz for all ImuSensor objects within this SensorManager.

#### Parameters

- **sample_rate** - The sample rate in Hz to set for the ImuSensor objects.