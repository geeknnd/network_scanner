from scapy.all import ARP, Ether, srp
from tools.utils import get_network

class ARPScanner: 
    def scan(self): 
        devices = []

        target = get_network()
        
        arp = ARP(pdst=target)
        
        ether = Ether(dst="ff:ff:ff:ff:ff:ff")
        packet = ether/arp
        result = srp(packet, timeout=3, verbose=1)[0]
        for sent, received in result:
            devices.append({
                "ip": received.psrc,
                "mac": received.hwsrc,
                "ports": [],
                "services": [],
                "type": None
            })
            #devices.append((received.psrc, received.hwsrc)) #ip + mac ////old version
        return devices


