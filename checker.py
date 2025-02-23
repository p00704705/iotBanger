import requests

class Checker:
    def __init__(self):
        self.vulnerabilities = []

    def check(self, ip, port):
        # Check for weak default passwords
        if self._check_password(ip, port):
            self.vulnerabilities.append("Weak default password found")

        # Check for unpatched firmware
        if self._check_firmware(ip, port):
            self.vulnerabilities.append("Unpatched firmware found")

        # Additional checks for common IoT vulnerabilities
        if self._check_default_credentials(ip, port):
            self.vulnerabilities.append("Default credentials found")

        if self._check_unsecured_communication(ip, port):
            self.vulnerabilities.append("Unsecured communication detected")

        return self.vulnerabilities

    def _check_password(self, ip, port):
        try:
            response = requests.post(f"http://{ip}:{port}/login", data={"username": "admin", "password": "123456"})
            if response.status_code == 200:
                return True
        except:
            pass

        return False

    def _check_firmware(self, ip, port):
        try:
            response = requests.get(f"http://{ip}:{port}/firmware_update")
            if "X-Frame-Options" not in response.headers:
                return True
        except:
            pass

        return False

    def _check_default_credentials(self, ip, port):
        # Replace with actual default credentials for specific devices
        try:
            response = requests.get(f"http://{ip}:{port}/admin", auth=('admin', 'admin'))
            if response.status_code == 200:
                return True
        except:
            pass

        return False

    def _check_unsecured_communication(self, ip, port):
        # Check for unencrypted communication
        try:
            response = requests.get(f"http://{ip}:{port}", verify=False)
            if "https" not in response.text.lower():
                return True
        except:
            pass

        return False
