import testSocket

if __name__ == "__main__":
    while True:
        testSocket.runUserInput()
        anotherScan = input("Would you like to scan more ports (y/n)").lower()
        if anotherScan != "y" or anotherScan != "yes":
            break;