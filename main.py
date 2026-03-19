from scanner.arp_scanner import ARPScanner
from scanner.port_scanner import NmapScanner
from tools.by_banner_grabbing import grab_banner

print("Chose the command: 1-3")
print("1)ARP Scanner")
print("2)Port Scanner")
print("3)Full Scanner")
print("4)Detect Grab Banner")
command = input()

devices = []

def SCANARP():
    scanner = ARPScanner()
    devices = scanner.scan()

    for device in devices:
        ip = device["ip"]
        mac = device["mac"]
    return devices
    

def SCANPORT(devices):
    print("\nChose scanning speed: ")
    print("1 - Fast (100 ports)")
    print("2 - Normal (1000 ports)")
    print("3 - Full (65535 ports)")
    print("4 - Agressive (not recommend)\n")

    speed = input()
    if speed == "1":
        ports = "1-100"
        arguments = "-sS -T4 -Pn"

    elif speed == "2":
        ports = "1-1000"
        arguments = "-sS -T4"

    elif speed == "3":
        ports = "1-65535"
        arguments = "-sS -T3"

    elif speed == "4":
        ports = "1-1000"
        arguments = "-sS -T4 -sV"
    else:
        print("incorrect choice")

    scanner2 = NmapScanner()
    for device in devices:
        device["ports"] = scanner2.scan_ports(device["ip"], ports, arguments)


def DETECTGRABBANNER(devices):
    for device in devices:
        services = []
        
        for port in device["ports"]:
            banner = grab_banner(device["ip"], port)
            services.append({
                "port": port,
                "banner": banner
            })

def beauty_print(devices):
    for i, device in enumerate(devices, 1):
        print(f"Device {i}:")
        print(f"  IP: {device['ip']}")
        print(f"  MAC: {device['mac']}")
        print(f"  Type: {device['type'] or 'Unknown'}")

        if device['ports']:
            print("  Ports:")
            for port_info in device['ports']:
                ip, port, status = port_info
                print(f"    - Port {port}: {status}")
        else:
            print("    Ports: None")

        if device['services']:
            print("  Services:")
            for service in device['services']:
                print(f"    - Port {service['port']}: {service['banner']}")
            else:
                print(":  Services: None")
            
            print("-" * 40)


if command == "1":    #ARP SCANNER
    devices = SCANARP()
    print(devices)
    
elif command == "2":
    SCANPORT()
elif command == "3":
    devices = SCANARP()
    SCANPORT(devices)
    DETECTGRABBANNER(devices)
    beauty_print(devices)
    
elif command == "4":
    DETECTGRABBANNER()