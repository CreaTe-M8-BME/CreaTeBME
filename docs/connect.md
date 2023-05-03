# Table of Contents

* [CreaTeBME.connect](#CreaTeBME.connect)
  * [connect](#CreaTeBME.connect.connect)

<a id="CreaTeBME.connect"></a>

# CreaTeBME.connect

<a id="CreaTeBME.connect.connect"></a>

#### connect

```python
async def connect(sensor_names: List[str])
```

Find the specified sensors and create ImuSensor objects for them.

**Arguments**:

- `sensor_names`: The names of the sensors to connect to

**Returns**:

A list of ImuSensor objects

