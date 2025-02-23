# IoT Device Vulnerability Scanner Documentation

## Overview

This Python program is designed to scan local network devices for potential vulnerabilities. It utilizes Nmap, a popular network exploration tool, along with custom checks for common IoT device vulnerabilities.

## Features

1. **Network Scanning**: The program uses Nmap to scan specified IP addresses or ranges for open ports.
2. **Vulnerability Checking**: It includes several checks for common IoT device vulnerabilities, such as:
   - Weak default passwords
   - Unpatched firmware
   - Default credentials
   - Unsecured communication protocols
   - Insecure firmware update mechanisms
   - Lack of device identification
   - Poor input validation
   - Outdated software
   - Insecure APIs
3. **Reporting**: The program generates a report detailing the vulnerabilities found during the scan.

## Requirements

1. **Nmap**: Install Nmap on your system.
2. **Python Package**: Ensure `python-nmap` is installed in your Python environment.

```bash
pip3 install python-nmap
```

## Usage

### Step 1: Determine Your Local Network Range

Open Terminal and execute the following command to find your local network range:

```bash
networksetup -getinfo "Wi-Fi"
```

Replace `"Wi-Fi"` with your actual network interface if necessary. Note the IPv4 address and subnet mask from the output.

### Step 2: Run the Program

Execute the program with your determined network range as an argument:

```bash
python3 iot_vulnerability_scanner.py 192.168.1.*
```

Replace `192.168.1.*` with your actual network range.

### Optional: Running as Administrator

Some operations may require administrator privileges. Run the script with sudo:

```bash
sudo python3 iot_vulnerability_scanner.py 192.168.1.*
```

## Contributing

We welcome contributions to enhance the program further! Here are some ideas for improvement:

1. **Additional Vulnerabilities**: Implement checks for more vulnerabilities.
2. **Improved Reporting**: Enhance the report generation with a more user-friendly format.
3. **Device Identification**: Add functionality to identify specific devices based on their characteristics.

## License

This project is distributed under the MIT License. See `LICENSE` for details.

## Acknowledgments

- Thanks to the Nmap team for creating such a versatile and powerful tool.
- A special mention to all contributors who have helped improve this project over time.

---

For more information or assistance, please visit our [GitHub repository](https://github.com/yourusername/iot-vulnerability-scanner). Happy scanning!
