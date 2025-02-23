"""
iot_banger: A tool for scanning local network devices for potential vulnerabilities.

This module provides a simple interface for scanning local network devices using Nmap,
and checking for common IoT device vulnerabilities.
"""

from .scanner import Scanner
from .checker import Checker
from .reporter import Reporter


class IoTScanner:
    """
    A class to represent an IoT vulnerability scanner.

    Attributes:
        target (str): The IP address or range of addresses to scan.
    """
    def __init__(self):
        """
        Initializes the IOTBanger instance with a target IP address or range.

        Args:
            target (str): The IP address or range of addresses to scan.
        """
        self.scanner = Scanner()
        self.checker = Checker()
        self.reporter = Reporter()

    def scan(self, network_range):
        """
        Scans the target IP address or range for open ports.

        Returns:
            dict: A dictionary containing information about the scanned devices
                  and their vulnerabilities.
        """
        devices = self.scanner.scan(network_range)
        print(f"Number of devices found: {len(devices)}")
        for device in devices:
            ip_addr = device#["addresses"]["ipv4"]
            ports = [80, 443, 8080, 8081]
            for port in ports:
                vulnerabilities = self.checker.check(ip_addr, port)
                if vulnerabilities:
                    self.reporter.add_result(ip_addr, port, vulnerabilities)

        self.reporter.generate_report()
