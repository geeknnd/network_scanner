import socket
from tools.utils import get_network

def grab_banner(target, port=80):
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(3)
        sock.connect((target, port))

        if port == 80:
            sock.send(b"GET / HTTP/1.1\r\nHost: example.com\r\n\r\n")

        banner = sock.recv(1024)
        sock.close()

        if banner:
            return banner.decode(errors="ignore").strip()
        return None
    
    except:
        return None

    '''except Exception as e:
        print(f"[ERROR] {e}")
        return None'''

def detect_device(banner):
    if not banner:
        return None
    
    banner = banner.lower()

    if "apache" in banner or "nginx" in banner:
        return "Web Server"
    elif "ssh" in banner:
        return "SSH Server"
    elif "ftp" in banner:
        return "FTP Server"
    elif "router" in banner or "mikrotik" in banner:
        return "Router"
    
    return "Unknown"