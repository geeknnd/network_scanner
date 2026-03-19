from tools.utils import get_network
import nmap

class NmapScanner:
    def scan_ports(self, target, ports, arguments):
        if target == None:
            target = get_network()
        scanner = nmap.PortScanner()
        scanner.scan(hosts=target, ports=ports, arguments=arguments)
        result = []

        for host in scanner.all_hosts():

            for protocol in scanner[host].all_protocols():
                ports = scanner[host][protocol].keys()

                for port in ports:
                    state = scanner[host][protocol][port]['state']
                    result.append((host, port, state))
        return result
