import socket 
import ipaddress
import fcntl, struct, platform, os

def get_network(): #Localisation
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    try:
        s.connect(("8.8.8.8", 80))
        ip = s.getsockname()[0]
    finally:
        s.close()

    netmask = None
    if platform.system() == "Linux":
        try:
            iface = "eth0"
            s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            netmask = socket.inet_ntoa(fcntl.ioctl(
                s.fileno(),
                0x891b,
                struct.pack('256s', iface.encode('utf-8')[:15])
            )[20:24])
        except:
            netmask = None
    if not netmask:
        netmask = "255.255.255.0"
    network = ipaddress.IPv4Network(f"{ip}/{netmask}", strict=False)
    return str(network)