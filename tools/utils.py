import socket
import ipaddress
def get_network(): #Localisation
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(("8.8.8.8", 80))
        ip = s.getsockname()[0]
        s.close()

        network = ipaddress.IPv4Network(ip + "/24", strict=False)
        return str(network)