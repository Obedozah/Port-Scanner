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
    
if __name__ == "__main__":
    while True:
        print("")