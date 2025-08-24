import testSocket

# Input for first port #
def runManualScanInput(ip):
    while True:
        _firstPort = input("Please enter the first port you would like to scan:\n")
        try:
            _firstPort = int(_firstPort)
            if 0 <= _firstPort <= 65535:
                break
            else:
                print("Invalid Range. 0 - 65535")
        except ValueError:
            print("Invalid Type. Try Again.")
    # Input for last port #
    while True:
        _lastPort = input("Please enter the last port you would like to scan:\n")
        try:
            _lastPort = int(_lastPort)
            if _firstPort > _lastPort:
                print("Invalid Range. Must be Equal or Greater than first port")
            elif not 0 <= _lastPort <= 65535:
                print("Invalid Range. 0 - 65535")
            else:
                break
        except ValueError:
            print("Invalid Type. Try Again.")
    testSocket.scan_ports(str(ip), _firstPort, _lastPort)