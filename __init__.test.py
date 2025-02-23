from iotBanger import IoTScanner

class TestIoTScanner:
    def setUp(self):
        self.iot_scanner = IoTScanner()
        self.network_range = "192.168.1.0/24"
