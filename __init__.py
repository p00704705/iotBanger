from .scanner import Scanner
from .checker import Checker
from .reporter import Reporter

class IoTScanner:
    def __init__(self):
        self.scanner = Scanner()
        self.checker = Checker()
        self.reporter = Reporter()

    def scan(self, network_range):
        devices = self.scanner.scan(network_range)
        print(f"Number of devices found: {len(devices)}")
        for device in devices:
            ip = device#["addresses"]["ipv4"]
            ports = [80, 443, 8080, 8081]
            for port in ports:
                vulnerabilities = self.checker.check(ip, port)
                if vulnerabilities:
                    self.reporter.add_result(ip, port, vulnerabilities)

        self.reporter.generate_report()
