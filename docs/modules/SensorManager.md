# SensorManager

## Table of Contents

* [SensorManager](#SensorManager)
  * [SensorManager](#SensorManager.SensorManager)
    * [\_\_init\_\_](#SensorManager.SensorManager.__init__)
    * [start](#SensorManager.SensorManager.start)
    * [stop](#SensorManager.SensorManager.stop)
    * [is\_running](#SensorManager.SensorManager.is_running)
    * [set\_callback](#SensorManager.SensorManager.set_callback)
    * [set\_sample\_rate](#SensorManager.SensorManager.set_sample_rate)
    * [get\_measurements](#SensorManager.SensorManager.get_measurements)
    * [record](#SensorManager.SensorManager.record)

<a id="SensorManager"></a>

# SensorManager

<a id="SensorManager.SensorManager"></a>

## SensorManager Objects

```python
class SensorManager()
```

Wrapper class for ImuSensor objects

<a id="SensorManager.SensorManager.__init__"></a>

#### \_\_init\_\_

```python
def __init__(sensor_names: List[str], sample_rate: int = 100)
```

Construct a SensorManager object

**Arguments**:

- `sensor_names`: List of sensor names
- `sample_rate`: The sample frequency

<a id="SensorManager.SensorManager.start"></a>

#### start

```python
def start() -> None
```

Start the SensorManager

Blocks until all sensors are sending data.


<a id="SensorManager.SensorManager.stop"></a>

#### stop

```python
def stop() -> None
```

Stop the SensorManager


<a id="SensorManager.SensorManager.is_running"></a>

#### is\_running

```python
def is_running() -> bool
```

Check whether the SensorManager is running.

**Returns**:

Boolean representing the running state of the SensorManager.

<a id="SensorManager.SensorManager.set_callback"></a>

#### set\_callback

```python
def set_callback(callback: Callable[[str, List[float]], None]) -> None
```

Set a callback to be run when a sensor measurement comes in.

**Arguments**:

- `callback`: A callback function that takes the sensor name and sensor measurement

<a id="SensorManager.SensorManager.set_sample_rate"></a>

#### set\_sample\_rate

```python
def set_sample_rate(sample_rate: int) -> None
```

Set the sample frequency of the sensors.

**Arguments**:

- `sample_rate`: The sample frequency

<a id="SensorManager.SensorManager.get_measurements"></a>

#### get\_measurements

```python
def get_measurements() -> Dict[str, List[List[float]]]
```

Get the measurements since the last time this method was called.

**Returns**:

A dictionary containing a list of measurements for each sensor

<a id="SensorManager.SensorManager.record"></a>

#### record

```python
def record(filename: str, seconds: int) -> None
```

Record the measurements of the sensors and save it to a file.

**Arguments**:

- `filename`: The name of the recording file to be saved
- `seconds`: The amount of seconds to record

