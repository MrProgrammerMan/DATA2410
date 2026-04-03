import random
import sys
from socket import *
from datetime import datetime
import time

clientSocket = socket(AF_INET, SOCK_DGRAM)

clientSocket.settimeout(1.0)

rtts = []

print("Pinging server at 127.0.0.1:12000...\n")

try:
    for i in range(1, 11):
        try:
            message = f"Ping {i} {datetime.now()}"

            before = time.time()

            clientSocket.sendto(message.encode("utf-8"), ("127.0.0.1", 12000))
            clientSocket.recvfrom(1024)

            after = time.time()

            rtt = after-before
            rtts.append(rtt)

            print(f"Packet {i}: RTT = {rtt*1000:.3f}ms ✓")
        except timeout:
            print(f"Packet {i}: Request timed out ✗")
            continue
except KeyboardInterrupt:
    print("\nClient shutting down...")
    clientSocket.close()
    sys.exit(0)

print("\n--- Statistics ---")
print(f"10 packets sent, {len(rtts)} received, {(10 - len(rtts))*10}% packet loss")
print(f"Minimum RTT = {min(rtts)*1000:.3f}ms, Maximum RTT: {max(rtts)*1000:.3f}ms, Average RTT: {sum(rtts)*1000 / len(rtts):.3f}ms")