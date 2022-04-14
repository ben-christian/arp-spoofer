import scapy.all as scapy

packet = scapy.ARP(op=2, pdst="10.0.0.0", hwdst="00:00:00:00:00:00", psrc="10.10.0.1") #op is set to 2 to for response
#use scapy.ls(scapy.ARP()) will list all fields we can set for scapy.ARP class

