import ipaddress
import runManualScanInput
import runCommonScanInput

def runUserInput():
    while True:
        ip = None
        # Input for IPv4 address #
        while True:
            ip = input("Please enter the IPv4 address you would like to scan:\n")
            try:
                ip = ipaddress.ip_address(ip)
                ip = str(ip)
                break
            except ValueError:
                print("Invalid IPv4 address. Try Again. (X.X.X.X)")
        # Selection for Common Port Scan or Manual Selection #
        while True:
            selection = int(input("Would you like to \n(1) Scan commonly used ports\n(2) Select your own\n"))
            if selection == 1:
                runCommonScanInput.runCommonScanInput(ip)
                break
            elif selection == 2:
                runManualScanInput.runManualInput(ip)
                break
            else:
                print("Invalid Response. (1)/(2)")

        # Asking to continue scanning #
        while True:
            anotherScan = input("Would you like to scan more ports (y/n)\n").lower()
            if anotherScan in ("n", "no"):
                print("Exiting...")
                return
            elif anotherScan in ("y", "yes"):
                break
            else:
                print("Invalid Response. y/n:")