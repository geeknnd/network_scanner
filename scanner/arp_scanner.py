from scapy.all import ARP, Ether, srp
import socket
import ipaddress

class ARPScanner: 
    def get_network(self): #personalisation
        hostname = socket.gethostname()
        local_ip = socket.gethostbyname(hostname)
        network = ipaddress.IPv4Network(local_ip + "/24", strict=False)
        return str(network)
    
    def scan(self): 
        devices = []

        target = self.get_network()
        
        arp = ARP(pdst=target)
        
        ether = Ether(dst="ff:ff:ff:ff:ff:ff")
        packet = ether/arp
        result = srp(packet, timeout=3, verbose=1)[0]
        for sent, received in result:
            devices.append((received.psrc, received.hwsrc))
        return devices


