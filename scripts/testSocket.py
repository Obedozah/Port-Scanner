import ipaddress
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

def runUserInput():
    # Input for IPv4 address #
    while True:
        ip = input("Please enter the IPv4 address you would like to scan:")
        try:
            ip = ipaddress.ip_address(ip)
            break
        except ValueError:
            print("Invalid IPv4 address. Try Again. (X.X.X.X)")
    # Input for first port #
    while True:
        firstPort = input("Please enter the first port you would like to scan:")
        try:
            firstPort = int(firstPort)
            if 0 <= firstPort <= 65535:
                break
            else:
                print("Invalid Range. 0 - 65535")
        except ValueError:
            print("Invalid Type. Try Again.")
    # Input for last port #
    while True:
        lastPort = input("Please enter the last port you would like to scan:")
        try:
            lastPort = int(lastPort)
            if firstPort > lastPort:
                print("Invalid Range. Must be Equal or Greater than first port")
            elif 0 <= lastPort <= 65535:
                print("Invalid Range. 0 - 65535")
            else:
                break
        except ValueError:
            print("Invalid Type. Try Again.")
    
    scan_ports(str(ip), firstPort, lastPort)