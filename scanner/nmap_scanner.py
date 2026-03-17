'''import nmap
scanner = nmap.PortScanner()
scanner.scan('192.168.0.1', '22-443')
for host in scanner.all_hosts():
    print("Host: ", host)
    for protocol in scanner[host].all_protocols():
        print("Protocol: ", protocol)
        ports = scanner[host][protocol].keys()
        for port in ports:
            state = scanner[host][protocol][port]['state']
            print(f"Port {port}: {state}")'''
