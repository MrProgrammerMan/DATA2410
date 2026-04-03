import random
import sys
from socket import *
from datetime import datetime

clientSocket = socket(AF_INET, SOCK_DGRAM)

clientSocket.settimeout(1.0)

try:
    for i in range(1, 11):
        try:
            message = f"Ping {i} {datetime.now()}"

            clientSocket.sendto(message.encode("utf-8"), ("127.0.0.1", 12000))

            message, _ = clientSocket.recvfrom(1024)

            print(f"Response {message}")
        except timeout:
           # This exception occurs when NO packet has arrived within the timeout period
            continue
except KeyboardInterrupt:
    print("\nClient shutting down...")
    clientSocket.close()
    sys.exit(0)