import nmap

class Scanner:
    def __init__(self):
        self.nm = nmap.PortScanner()

    def scan(self, network_range):
        self.nm.scan(network_range, arguments='-p 80,443,8080,8081 -sV')
        return self.nm.all_hosts()
