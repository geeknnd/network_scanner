from scanner.arp_scanner import ARPScanner
from scanner.port_scanner import NmapScanner
from tools.by_banner_grabbing import grab_banner, detect_device
import json
from tools.logger import logger
import shutil
import os
import sys

print("Chose the command: ")
print("1)Start Scan")
print("2)Exit")
command = input("> ")

devices = []

with open("data/vulns.json", "r") as f:
    VULNS = json.load(f)


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
    print("4 - Agressive (1000 ports) {not recommend}\n")

    speed = input("> ")
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
        device_type = None

        for port_info in device["ports"]:
            ip, port, status = port_info

            if status != "open":
                continue
            
            banner = grab_banner(device["ip"], port)

            services.append({
                "port": port,
                "banner": banner   
            })

            if banner and not device_type:
                device_type = detect_device(banner)

        device["services"] = services
        device["type"] = device_type

def get_vulns(port):
    for item in VULNS:
        if item["port"] == port:
            return item["vulnerabilities"]
    return []

def clean_banner(banner):
    if not banner:
        return None
    
    lines = banner.split("\n")
    clean = lines[:2]

    return " | ".join(line.strip() for line in clean)

def beauty_print(devices):
    for i, device in enumerate(devices, 1):
        print(f"\nDevice {i}:")
        print(f"  IP: {device['ip']}")
        print(f"  MAC: {device['mac']}")
        print(f"  Type: {device['type'] or 'Unknown'}")

        if device['ports']:             #ports
            print("  Ports:")
            for port_info in device['ports']:
                ip, port, status = port_info
                print(f"    - Port {port}: {status}")

                if status == "open":
                    vulns = get_vulns(port) #vulns.json
                    if vulns:
                        print("  [!] Possible vulnerabilities (based on service):")
                        for v in vulns:
                            print(f"     - {v['name']} [{v['severity']}] ({v['cve']})")
        else:
            print("    Ports: None")

        if device.get('services'):              #services
            print("  Services:")
            for service in device['services']:
                banner = clean_banner(service['banner'])
                if banner:
                    print(f"  - Port {service['port']}: {banner}")
                    print("    Status: Responding")
        else:
            print(":  Services: None")
            
        print("-" * 40)


#LOGS 
if not shutil.which("nmap"): #nmap
    logger.critical("Nmap is not installed. Please install nmap.")
    sys.exit(1)

if os.geteuid() != 0: #root/admin privileges
    logger.error("running without administrator privileges. Some scans may not work.")

target_network = "192.168.1.0/24" #start scanning
logger.info(f"Starting network scan: {target_network}")

devices = [{'ip': '192.168.1.10', 'mac': 'AA:BB:CC:DD:EE:FF', 'services': []}] #example devices found
for device in devices:
    logger.info(f"Device found: IP {device['ip']}, MAC {device['mac']}")

for device in devices:
    for service in device['services']:
        logger.info(f"Device {device['ip']} - Port {service['port']}, Status {service['status']}")



if command == "1":
    devices = SCANARP()
    print("\n", "-" * 40)
    SCANPORT(devices)
    DETECTGRABBANNER(devices)
    beauty_print(devices)
elif command == "2":
    exit