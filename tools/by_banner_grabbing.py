import socket
from tools.utils import get_network

def grab_banner(target, port=80):
    if target == None:
            target = get_network()

    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(5)

        sock.connect((target, port))

        banner = sock.recv(1024)
        sock.close()
        if banner:
            return banner.decode(errors="ignore").strip()
        return None
    except Exception as e:
        print(f"[ERROR] {e}")
        return None