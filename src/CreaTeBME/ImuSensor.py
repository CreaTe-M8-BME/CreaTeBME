from bleak import BleakClient

_IMU_SERVICE_UUID = '0ddf5c1d-d269-4b17-bd7f-33a8658f0b89'
_IMU_CHAR_UUID = '64b83770-6b12-4a54-b31a-e007306132bd'
_SAMPLE_RATE_CHAR_UUID = '3003aac7-d843-4e55-9d89-3f93020cc9ee'


class ImuSensor:
    def __init__(self, device, callback=None):
        self.__sample_rate_char = None
        self.__imu_char = None
        self.__imu_service = None
        self.__sens_acc = 2048
        self.__sens_gyro = 16.4
        self.__callback = callback
        self.__reading = None

        # Connect to ble device
        self.__bt_client = BleakClient(device)

    def __del__(self):
        if hasattr(self, 'serial_sensor'):
            self.serial_sensor.close()
        elif hasattr(self, 'bt_sensor'):
            self.__bt_client.disconnect()

    def __receive_reading(self, char, inbytes):
        output = [None] * 6
        for i in range(0, 6):
            input_bytes = inbytes[i * 2:i * 2 + 2]
            num = int.from_bytes(input_bytes, "big", signed=True)
            if i < 3:
                output[i] = self.__convert_acc(num)
            else:
                output[i] = self.__convert_gyro(num)
        self.__reading = output
        if self.__callback:
            self.__callback(output)
        else:
            print(output)

    def __convert_acc(self, data):
        return data / self.__sens_acc

    def __convert_gyro(self, data):
        return data / self.__sens_gyro

    async def connect(self):
        try:
            await self.__bt_client.connect()
        except Exception as e:
            raise RuntimeError('Could not connect to sensor: ', e)

        # Read and store services and characteristics
        self.__imu_service = self.__bt_client.services.get_service(_IMU_SERVICE_UUID)
        self.__imu_char = self.__imu_service.get_characteristic(_IMU_CHAR_UUID)
        self.__sample_rate_char = self.__imu_service.get_characteristic(_SAMPLE_RATE_CHAR_UUID)

        # # Register callback for notify events
        await self.__bt_client.start_notify(self.__imu_char, self.__receive_reading)

    async def set_sample_rate(self, sample_rate):
        delay_val = int(1/sample_rate*1000)
        return await self.__bt_client.write_gatt_char(
            self.__sample_rate_char,
            int.to_bytes(delay_val, 2, "big", signed=False),
            response=True
        )

    def get_reading(self):
        return self.__reading

    async def set_callback(self, callback):
        if not callable(callback):
            return TypeError('Callback should be a function')
        self.__callback = callback