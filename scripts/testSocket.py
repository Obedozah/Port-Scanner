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
    for i in(firstPort, lastPort):
        try:
            scan_port(ip, i)
        except True:
            print(f"Port {i} is open")
        else:
            print(f"Port {i} is closed")

    
if __name__ == "__main__":
    while True:
        ip = input("Please enter the IPv4 address you would like to scan:")
        firstPort = input("Please enter the first port you would like to scan:")
        lastPort = input("Please enter the last port you would like to scan:")

        break;