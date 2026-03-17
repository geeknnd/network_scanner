from tools.utils import get_network
import nmap

class NmapScanner:
    def scan_ports(self):
        target = get_network()
        scanner = nmap.PortScanner()
        scanner.scan(target, "1-100", "-T4")
        result = []

        for host in scanner.all_hosts():
            #print(f"Host: {host}")

            for protocol in scanner[host].all_protocols():
                #print(f"Protocol: {protocol}")
                ports = scanner[host][protocol].keys()

                for port in ports:
                    state = scanner[host][protocol][port]['state']
                    result.append((host, port, state))
        return result
