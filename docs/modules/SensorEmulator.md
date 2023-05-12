# SensorEmulator

## Table of Contents

* [SensorEmulator](#SensorEmulator)
  * [SensorEmulator](#SensorEmulator.SensorEmulator)
    * [\_\_init\_\_](#SensorEmulator.SensorEmulator.__init__)
    * [start](#SensorEmulator.SensorEmulator.start)
    * [stop](#SensorEmulator.SensorEmulator.stop)
    * [get\_measurements](#SensorEmulator.SensorEmulator.get_measurements)
    * [set\_callback](#SensorEmulator.SensorEmulator.set_callback)
    * [set\_sample\_rate](#SensorEmulator.SensorEmulator.set_sample_rate)
    * [record](#SensorEmulator.SensorEmulator.record)

<a id="SensorEmulator"></a>

# SensorEmulator

<a id="SensorEmulator.SensorEmulator"></a>

## SensorEmulator Objects

```python
class SensorEmulator()
```

An emulator for the SensorManager that reads from a recording file instead.

<a id="SensorEmulator.SensorEmulator.__init__"></a>

#### \_\_init\_\_

```python
def __init__(filename: str)
```

Construct a SensorEmulator

**Arguments**:

- `filename`: The name of the recording file

<a id="SensorEmulator.SensorEmulator.start"></a>

#### start

```python
def start() -> None
```

Start the SensorEmulator

<a id="SensorEmulator.SensorEmulator.stop"></a>

#### stop

```python
def stop() -> None
```

Stop the SensorEmulator

<a id="SensorEmulator.SensorEmulator.get_measurements"></a>

#### get\_measurements

```python
def get_measurements() -> Dict[str, List[List[float]]]
```

Get the measurements since the last time this method was called.

**Returns**:

A dictionary containing a list of measurements for each sensor

<a id="SensorEmulator.SensorEmulator.set_callback"></a>

#### set\_callback

```python
def set_callback(callback: Callable[[str, List[float]], None]) -> None
```

Set a callback to be run when a sensor measurement comes in.

**Arguments**:

- `callback`: A callback function that takes the sensor name and sensor measurement

<a id="SensorEmulator.SensorEmulator.set_sample_rate"></a>

#### set\_sample\_rate

```python
def set_sample_rate(sample_rate: int) -> None
```

Not implemented.

**Arguments**:

- `sample_rate`: The sample frequency

<a id="SensorEmulator.SensorEmulator.record"></a>

#### record

```python
def record() -> None
```

Not implemented

