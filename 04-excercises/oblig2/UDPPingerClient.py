import random
import sys
from socket import *
from datetime import datetime
import time

clientSocket = socket(AF_INET, SOCK_DGRAM)

clientSocket.settimeout(1.0)

try:
    for i in range(1, 11):
        try:
            message = f"Ping {i} {datetime.now()}"

            before = time.time()

            clientSocket.sendto(message.encode("utf-8"), ("127.0.0.1", 12000))
            message, _ = clientSocket.recvfrom(1024)

            after = time.time()

            rtt = after-before

            print(f"Response: {message}, RTT: {rtt*1000:.3f}ms")
        except timeout:
            print("Request timed out")
            continue
except KeyboardInterrupt:
    print("\nClient shutting down...")
    clientSocket.close()
    sys.exit(0)