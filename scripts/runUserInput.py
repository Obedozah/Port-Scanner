import testSocket
import ipaddress

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
            elif not 0 <= lastPort <= 65535:
                print("Invalid Range. 0 - 65535")
            else:
                break
        except ValueError:
            print("Invalid Type. Try Again.")
    testSocket.scan_ports(str(ip), firstPort, lastPort)
    # Asking to continue scanning #
    while True:
        anotherScan = input("Would you like to scan more ports (y/n)").lower()
        if not anotherScan == "y" or not anotherScan == "yes":
            print("Thank you. Goodbye")
            break;