import socket

def scan_port(ip, port):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(1)
    result = s.connect_ex((ip, port))
    s.close()

    if result == 0:
        return True
    else:
        return False
    
def scan_ports(ip, firstPort, lastPort):
    for i in range(firstPort, lastPort + 1):
        if (scan_port(ip, i)):
            print(f"Port {i} is open")
        else:
            print(f"Port {i} is closed")