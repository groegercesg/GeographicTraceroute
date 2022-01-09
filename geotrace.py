# TODO: Check if is in sudo

from scapy.all import *

# This support either IP or Domain
    # 172.67.195.197
    # callumgroeger.com
hostname = "quantumcore.com.au"

ip_list = []

for i in range(1, 32):
    pkt = IP(dst=hostname, ttl=i) / UDP(dport=33434)
    # Send the packet and get a reply
    reply = sr1(pkt, verbose=0)
    if reply is None:
        # No reply, this is bad
        break
    elif reply.type == 3:
        # We've reached our destination
        print("Done!", reply.src)
        ip_list.append(reply.src)
        break
    else:
        # We're in the middle somewhere
        print("%d hops away: " % i , reply.src)
        ip_list.append(reply.src)
        
print(ip_list)

# Use ip info