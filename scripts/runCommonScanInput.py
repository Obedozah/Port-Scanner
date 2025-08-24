import testSocket

def runCommonScanInput(ip):
    common_ports = [21, 22, 23, 25, 53, 80, 110, 139, 143, 443, 445, 3389]

    for i in common_ports:
        testSocket.scan_ports(ip, i, i)