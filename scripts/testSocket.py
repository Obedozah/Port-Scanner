import socket

# Scan individual port #
def scan_port(ip, port):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(1)
    result = s.connect_ex((ip, port))
    s.close()

    if result == 0:
        print(f"Port {port} is open")
    else:
        print(f"Port {port} is closed")
    
#Scan range of ports #
def scan_ports(ip, firstPort, lastPort):
    for i in range(firstPort, lastPort + 1):
        scan_port(ip, i)