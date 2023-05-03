# Table of Contents

* [CreaTeBME.SensorManager](#CreaTeBME.SensorManager)
  * [SensorManager](#CreaTeBME.SensorManager.SensorManager)
    * [\_\_init\_\_](#CreaTeBME.SensorManager.SensorManager.__init__)
    * [start](#CreaTeBME.SensorManager.SensorManager.start)
    * [stop](#CreaTeBME.SensorManager.SensorManager.stop)
    * [set\_callback](#CreaTeBME.SensorManager.SensorManager.set_callback)
    * [set\_sample\_rate](#CreaTeBME.SensorManager.SensorManager.set_sample_rate)
    * [get\_measurements](#CreaTeBME.SensorManager.SensorManager.get_measurements)
    * [record](#CreaTeBME.SensorManager.SensorManager.record)

<a id="CreaTeBME.SensorManager"></a>

# CreaTeBME.SensorManager

<a id="CreaTeBME.SensorManager.SensorManager"></a>

## SensorManager Objects

```python
class SensorManager()
```

Wrapper class for ImuSensor objects

<a id="CreaTeBME.SensorManager.SensorManager.__init__"></a>

#### \_\_init\_\_

```python
def __init__(sensor_names: List[str], sample_rate: int = 100)
```

Construct a SensorManager object

**Arguments**:

- `sensor_names`: List of sensor names
- `sample_rate`: The

<a id="CreaTeBME.SensorManager.SensorManager.start"></a>

#### start

```python
def start() -> None
```

Start the SensorManager


<a id="CreaTeBME.SensorManager.SensorManager.stop"></a>

#### stop

```python
def stop() -> None
```

Stop the SensorManager


<a id="CreaTeBME.SensorManager.SensorManager.set_callback"></a>

#### set\_callback

```python
def set_callback(callback: Callable[[str, List[float]], None]) -> None
```

Set a callback to be run when a sensor measurement comes in.

**Arguments**:

- `callback`: A callback function that takes the sensor name and sensor measurement

<a id="CreaTeBME.SensorManager.SensorManager.set_sample_rate"></a>

#### set\_sample\_rate

```python
def set_sample_rate(sample_rate: int) -> None
```

Set the sample frequency of the sensors.

**Arguments**:

- `sample_rate`: The sample frequency

<a id="CreaTeBME.SensorManager.SensorManager.get_measurements"></a>

#### get\_measurements

```python
def get_measurements() -> Dict[str, List[List[float]]]
```

Get the measurements since the last time this method was called.

**Returns**:

A dictionary containing a list of measurements for each sensor

<a id="CreaTeBME.SensorManager.SensorManager.record"></a>

#### record

```python
def record(filename: str, seconds: int) -> None
```

Record the measurements of the sensors and save it to a file.

**Arguments**:

- `filename`: The name of the recording file to be saved
- `seconds`: The amount of seconds to record

