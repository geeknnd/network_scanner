from scanner.arp_scanner import ARPScanner
from scanner.port_scanner import NmapScanner

print("Chose the command: 1-3\n1)ARP Scanner\n2)Port Scanner")
command = int(input())


if command == 1:    #ARP SCANNER
    scanner = ARPScanner()
    devices = scanner.scan()

    for ip, mac in devices:
        print(f"IP: {ip}, MAC: {mac}")
elif command == 2:
    scaner = NmapScanner()
    result = scaner.scan_ports()

    for host, port, state in result:
        print(f"{host} : {port} : {state}")
