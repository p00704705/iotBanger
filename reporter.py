class Reporter:
    def __init__(self):
        self.results = []

    def add_result(self, ip, port, vulnerabilities):
        self.results.append((ip, port, vulnerabilities))

    def generate_report(self):
        print("Scan Results:")
        for ip, port, vulnerabilities in self.results:
            print(f"\nDevice at {ip}:{port}")
            if not vulnerabilities:
                print("No vulnerabilities found")
            else:
                print("Vulnerabilities:")
                for vulnerability in vulnerabilities:
                    print(f"- {vulnerability}")
