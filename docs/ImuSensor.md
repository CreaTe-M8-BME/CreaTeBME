# Table of Contents

* [CreaTeBME.ImuSensor](#CreaTeBME.ImuSensor)
  * [ImuSensor](#CreaTeBME.ImuSensor.ImuSensor)
    * [\_\_init\_\_](#CreaTeBME.ImuSensor.ImuSensor.__init__)
    * [connect](#CreaTeBME.ImuSensor.ImuSensor.connect)
    * [set\_sample\_rate](#CreaTeBME.ImuSensor.ImuSensor.set_sample_rate)
    * [get\_sample\_rate](#CreaTeBME.ImuSensor.ImuSensor.get_sample_rate)
    * [get\_reading](#CreaTeBME.ImuSensor.ImuSensor.get_reading)
    * [set\_callback](#CreaTeBME.ImuSensor.ImuSensor.set_callback)

<a id="CreaTeBME.ImuSensor"></a>

# CreaTeBME.ImuSensor

<a id="CreaTeBME.ImuSensor.ImuSensor"></a>

## ImuSensor Objects

```python
class ImuSensor()
```

An interface for the BLE IMU sensors.

<a id="CreaTeBME.ImuSensor.ImuSensor.__init__"></a>

#### \_\_init\_\_

```python
def __init__(device: BLEDevice,
             callback: Callable[[str, List[float]], None] = None,
             name: str = None)
```

Construct an ImuSensor.

**Arguments**:

- `device`: The BLE device to use as the sensor
- `callback`: [Optional] A callback to run for each measurement
- `name`: [Optional] A readable name for the sensor

<a id="CreaTeBME.ImuSensor.ImuSensor.connect"></a>

#### connect

```python
async def connect() -> None
```

Connect to the BLE device.

<a id="CreaTeBME.ImuSensor.ImuSensor.set_sample_rate"></a>

#### set\_sample\_rate

```python
async def set_sample_rate(sample_rate: int) -> bool
```

Set the sample frequency of the sensor.

**Arguments**:

- `sample_rate`: The sample frequency

**Returns**:

Boolean indicating if the sample rate was correctly set

<a id="CreaTeBME.ImuSensor.ImuSensor.get_sample_rate"></a>

#### get\_sample\_rate

```python
async def get_sample_rate() -> int
```

Read the sample frequency from the sensor.

**Returns**:

The sample frequency

<a id="CreaTeBME.ImuSensor.ImuSensor.get_reading"></a>

#### get\_reading

```python
def get_reading() -> List[float]
```

Get the last measurement received from the sensor.

**Returns**:

A IMU measurement

<a id="CreaTeBME.ImuSensor.ImuSensor.set_callback"></a>

#### set\_callback

```python
def set_callback(
        callback: Callable[[str, List[float]], None]) -> None | TypeError
```

Set a callback to be run when a sensor measurement comes in.

**Arguments**:

- `callback`: A callback function that takes the sensor name and sensor measurement

