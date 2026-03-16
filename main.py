from scanner.arp_scanner import ARPScanner

scanner = ARPScanner()
devices = scanner.scan()

for ip, mac in devices:
    print(f"IP: {ip}, MAC: {mac}")